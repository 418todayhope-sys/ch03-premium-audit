"""Generate verified-only classification CSVs and preserve separate review state."""

from __future__ import annotations

import argparse
import csv
from dataclasses import fields, replace
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import os
from pathlib import Path
import re
import sys
import tempfile

from employer_processing import EmployerFiles
from input_reader import read_markdown
from payroll_allocation import AllocationError, _cents, _money
from preview import run_preview
from rule_evaluator import RuleEvaluator


COLUMNS = ("class_code", "payroll_allocated", "rationale_ref")


class CSVGenerationError(ValueError):
    """A CSV, its evidence or its output destination cannot be verified."""


def _units(value, subject):
    if not isinstance(value, (str, Decimal)):
        raise CSVGenerationError(f"{subject}: money must be a Decimal or its exact string")
    try:
        return _cents(Decimal(value), subject)
    except (AllocationError, InvalidOperation) as exc:
        raise CSVGenerationError(str(exc)) from exc


def _totals(values):
    return {code: _units(amount, code) for code, amount in values.items()
            if _units(amount, code) != 0}


def build_rows(entry, guide):
    """Validate engine contributions/controls and derive rows, without classifying."""
    if entry["status"] == "ERROR":
        raise CSVGenerationError(f"Processing error: {entry['errors']}")
    checks = entry["reconciliation"]
    for required in ("allocation", "independent"):
        if checks.get(required) is None:
            raise CSVGenerationError(f"Missing {required} reconciliation")
    for name, check in checks.items():
        if check is not None and check.get("reconciled") is not True:
            raise CSVGenerationError(f"Failed {name} reconciliation")
    catalog = RuleEvaluator(guide, None)
    sources = {ref["id"]: ref for ref in entry["sources"]}
    if len(sources) != len(entry["sources"]):
        raise CSVGenerationError("Duplicate source citation identifiers")
    guide_path = guide.path.resolve()
    totals, paragraphs = {}, {}

    def contribution(line, decision, amount):
        code, paragraph = line["class_code"], line["rationale_ref"]
        definitions = catalog.code_sources.get(code, [])
        if (len(definitions) != 1 or definitions[0].locator in catalog.ambiguous_paragraphs
                or code in catalog.code_errors):
            raise CSVGenerationError(f"{code}: current guide must have a unique, unchanged code definition")
        definition = definitions[0]
        if paragraph != definition.locator:
            raise CSVGenerationError(f"{code}: unsupported rationale reference {paragraph!r}; expected {definition.locator}")
        if (not decision or decision["status"] != "CLASSIFIED" or decision["class_code"] != code
                or decision["rationale_ref"] != paragraph or decision["required_confirmation"]):
            raise CSVGenerationError(f"{code}: contribution lacks a verified classification/paragraph")
        cited = [sources.get(key) for key in decision["rule_sources"]]
        if not any(ref and Path(ref["source"]).resolve() == guide_path
                   and ref["locator"] == paragraph and ref["sha256"] == definition.sha256
                   and ref["line_start"] == definition.line_start and ref["line_end"] == definition.line_end
                   for ref in cited):
            raise CSVGenerationError(f"{code}: current guide paragraph reference is missing, changed or stale")
        if not decision["evidence_sources"] or any(key not in sources for key in decision["evidence_sources"]):
            raise CSVGenerationError(f"{code}: classification lacks supporting record references")
        totals[code] = totals.get(code, 0) + amount
        paragraphs[code] = paragraph

    register = allocated = pending = 0
    employees, parts, part_sources = set(), set(), set()
    for employee in entry["employee_payroll"]:
        key = employee["employee_id"]
        if key in employees:
            raise CSVGenerationError(f"{key}: duplicate employee")
        employees.add(key)
        wages = _units(employee["register_wages"], key)
        register += wages
        accounted = employee_open = 0
        employee_codes = {}
        for part in employee["parts"]:
            ref = sources.get(part["source"])
            if ref is None:
                raise CSVGenerationError(f"{key}: missing payroll source")
            source_key = (ref["source"], ref["line_start"], ref["locator"])
            if part["part_id"] in parts or source_key in part_sources:
                raise CSVGenerationError(f"{key}: duplicate payroll part or source record")
            parts.add(part["part_id"])
            part_sources.add(source_key)
            amount = _units(part["wages"], part["part_id"])
            accounted += amount
            if part["status"] == "ALLOCATED":
                contribution(part, part["decision"], amount)
                allocated += amount
                code = part["class_code"]
                employee_codes[code] = employee_codes.get(code, 0) + amount
            elif part["status"] == "OPEN" and part["class_code"] is None and part["rationale_ref"] is None:
                pending += amount
                employee_open += amount
            else:
                raise CSVGenerationError(f"{key}: unsupported payroll-part status or OPEN code")
        if accounted != wages or employee_open != _units(employee["open_wages"], key):
            raise CSVGenerationError(f"{key}: source payroll parts do not reconcile to register/OPEN wages")
        if {c: v for c, v in employee_codes.items() if v} != _totals(employee["verified_wages_by_code"]):
            raise CSVGenerationError(f"{key}: verified wage detail disagrees with engine totals")
    for name in ("allocation", "independent"):
        check = checks[name]
        if (register != _units(check["register_total"], name)
                or allocated != _units(check["allocated_total"], name)
                or pending != _units(check["unresolved_total"], name)
                or register != allocated + pending):
            raise CSVGenerationError(f"{name}: wage reconciliation disagrees with source parts")
    if pending != _units(entry["open_wages"], "OPEN wages"):
        raise CSVGenerationError("OPEN wages disagree with register parts")

    basis = added = nonpayroll = unresolved = 0
    adjustment_ids, adjustment_sources = set(), set()
    adjustment_totals = {}
    for line in entry["adjustments"]["lines"]:
        record = line["input_record"]
        identity = (line["kind"], line["adjustment_id"])
        source = sources.get(record["source"])
        if source is None:
            raise CSVGenerationError(f"{identity}: missing adjustment source")
        source_key = (line["kind"], source["source"], source["line_start"], source["locator"])
        if identity in adjustment_ids or source_key in adjustment_sources:
            raise CSVGenerationError(f"{identity}: duplicate adjustment or payment source")
        adjustment_ids.add(identity)
        adjustment_sources.add(source_key)
        amount = _units(record["amount"], str(identity))
        pay, excluded, open_basis = (_units(line[field], str(identity))
                                     for field in ("payroll_added", "nonpayroll", "unresolved_basis"))
        if amount != pay + excluded + open_basis:
            raise CSVGenerationError(f"{identity}: adjustment does not reconcile to original payment")
        if line["status"] == "VERIFIED" and open_basis == 0 and line["proposal"] is None:
            if pay:
                contribution(line, record["decision"], pay)
                code = line["class_code"]
                adjustment_totals[code] = adjustment_totals.get(code, 0) + pay
        elif line["status"] == "OPEN" and pay == excluded == 0 and line["class_code"] is None:
            pass
        else:
            raise CSVGenerationError(f"{identity}: unverified adjustment money cannot enter CSV totals")
        basis += amount
        added += pay
        nonpayroll += excluded
        unresolved += open_basis
    check = checks.get("adjustments")
    if entry["adjustments"]["lines"]:
        if check is None or any(_units(check[field], field) != expected for field, expected in (
                ("basis_total", basis), ("payroll_added", added), ("nonpayroll", nonpayroll),
                ("unresolved_basis", unresolved))):
            raise CSVGenerationError("Adjustment reconciliation disagrees with source payments")
        if unresolved != _units(entry["open_adjustment_basis"], "OPEN adjustment basis"):
            raise CSVGenerationError("OPEN adjustment basis disagrees with source payments")
        if {c: v for c, v in adjustment_totals.items() if v} != _totals(entry["adjustments"]["verified_by_code"]):
            raise CSVGenerationError("Verified adjustment detail disagrees with engine totals")
    totals = {code: amount for code, amount in totals.items() if amount != 0}
    if totals != _totals(entry["verified_by_code"]):
        raise CSVGenerationError("Verified CSV contributions disagree with engine class totals")
    if sum(totals.values()) != allocated + added:
        raise CSVGenerationError("CSV total does not reconcile to verified wages plus additions")
    return [{"class_code": code, "payroll_allocated": format(_money(totals[code]), ".2f"),
             "rationale_ref": paragraphs[code]} for code in sorted(totals)]


def validate_csv(text, entry, guide):
    """Read CSV independently and compare exact schema/rows with verified results."""
    try:
        reader = csv.DictReader(io.StringIO(text, newline=""), strict=True)
        rows = list(reader)
    except csv.Error as exc:
        raise CSVGenerationError(f"Malformed generated CSV: {exc}") from exc
    if reader.fieldnames != list(COLUMNS) or rows != build_rows(entry, guide):
        raise CSVGenerationError("CSV schema, cent formatting, code totals or paragraph references differ from verified results")


def _verify_sources(processing, entry, cache):
    manifests = [*processing["shared_sources"], *entry["source_manifest"]]
    for manifest in manifests:
        path = Path(manifest["path"])
        if path not in cache:
            raw = path.read_bytes()
            cache[path] = (hashlib.sha256(raw).hexdigest(), len(raw.decode("utf-8").splitlines()))
        if cache[path][0] != manifest["sha256"]:
            raise CSVGenerationError(f"Source changed since processing: {path}")
    for source in entry["sources"]:
        path = Path(source["source"])
        if path not in cache or cache[path][0] != source["sha256"]:
            raise CSVGenerationError(f"Unsupported or stale source citation: {path}")
        if not 1 <= source["line_start"] <= source["line_end"] <= cache[path][1]:
            raise CSVGenerationError(f"Invalid source line reference: {path}")


def _preflight(path, payload):
    if path.is_symlink() or (path.exists() and (not path.is_file() or path.read_bytes() != payload)):
        raise CSVGenerationError(f"Refusing to overwrite differing existing output: {path}; use a new output location")
    for parent in path.parents:
        if parent.exists() and not parent.is_dir():
            raise CSVGenerationError(f"Output parent is an existing file: {parent}")


def _publish(path, payload):
    """Publish one complete file without overwriting existing operator work."""
    _preflight(path, payload)
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".classification-", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError:
            _preflight(path, payload)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def generate_csvs(guide, interview, *, output_dir, review_state, employer=None,
                  all_employers=None, files=EmployerFiles()):
    """Reread sources, export verified CSVs, and retain the entire engine preview."""
    if (employer is None) == (all_employers is None):
        raise CSVGenerationError("Select exactly one employer or all-employers directory")
    if Path(review_state).expanduser().is_symlink():
        raise CSVGenerationError("Review-state output must not be a symbolic-link file")
    guide, interview, output_dir, review_state = (
        Path(path).expanduser().resolve() for path in (guide, interview, output_dir, review_state))
    root = Path(employer if employer is not None else all_employers).expanduser().resolve()
    if (output_dir.is_relative_to(root) or review_state.is_relative_to(root)
            or review_state in (guide, interview) or output_dir in (guide, interview)):
        raise CSVGenerationError("Output destinations must be separate from original input sources")
    if output_dir.is_relative_to(review_state):
        raise CSVGenerationError("Review-state file cannot be an ancestor of the CSV output directory")
    processing = run_preview(guide, interview, employer=employer, all_employers=all_employers, files=files)
    report = {"schema_version": 1, "allocation_scope": "VERIFIED_ONLY", "status": processing["status"],
        "review_state": str(review_state), "processing": processing, "outputs": [], "errors": []}
    candidates, collisions = {}, {}
    for entry in processing["employers"]:
        source_directory = Path(entry["directory"]).resolve()
        if output_dir.is_relative_to(source_directory) or review_state.is_relative_to(source_directory):
            raise CSVGenerationError(f"Output destinations overlap actual employer sources: {source_directory}")
        slug = re.sub(r"[^a-z0-9]+", "-", entry["employer"].lower()).strip("-")
        path = output_dir / f"{slug}.csv"
        if path.resolve() in (guide, interview) or review_state.is_relative_to(path):
            raise CSVGenerationError(f"CSV output path collides with a source or review-state file: {path}")
        candidates[entry["directory"]] = (slug, path)
        collisions.setdefault(path, []).append(entry["directory"])
    if review_state in collisions:
        raise CSVGenerationError("Review-state path collides with an employer CSV")
    plans, cache = [], {}
    document = read_markdown(guide) if processing["employers"] else None
    for entry in processing["employers"]:
        try:
            slug, path = candidates[entry["directory"]]
            if not slug or len(collisions[path]) != 1:
                raise CSVGenerationError(f"Invalid filename or employer filename collision: {path}")
            _verify_sources(processing, entry, cache)
            rows = build_rows(entry, document)
            stream = io.StringIO(newline="")
            writer = csv.DictWriter(stream, fieldnames=COLUMNS, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
            text = stream.getvalue()
            validate_csv(text, entry, document)
            payload = text.encode("utf-8")
            plans.append((path, payload))
            report["outputs"].append({"employer": entry["employer"], "directory": entry["directory"],
                "path": str(path), "sha256": hashlib.sha256(payload).hexdigest(), "rows": rows,
                "verified_total": str(_money(sum(_units(row["payroll_allocated"], "CSV") for row in rows)))})
        except (CSVGenerationError, OSError, ValueError, KeyError) as exc:
            report["errors"].append({"employer": entry["employer"], "type": type(exc).__name__, "message": str(exc)})
    if report["errors"]:
        report["status"] = "ERROR"
    # Recheck source content immediately before publishing; sources are never locked.
    for path, (digest, _) in cache.items():
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise CSVGenerationError(f"Source changed before publication: {path}")
    payload = (json.dumps(report, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    plans.append((review_state, payload))
    for path, content in plans:
        _preflight(path, content)
    for path, content in plans:
        _publish(path, content)
        if path.read_bytes() != content:
            raise CSVGenerationError(f"Output verification failed: {path}")
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guide", required=True, type=Path)
    parser.add_argument("--interview", required=True, type=Path)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--employer", type=Path)
    mode.add_argument("--all-employers", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory for verified-only employer CSVs")
    parser.add_argument("--review-state", required=True, type=Path, help="Separate JSON retaining OPEN evidence and controls")
    parser.add_argument("--file", action="append", default=[], metavar="FIELD=RELATIVE_PATH")
    args = parser.parse_args(argv)
    filenames = {}
    allowed = {field.name for field in fields(EmployerFiles)}
    for value in args.file:
        field, separator, path = value.partition("=")
        if not separator or field not in allowed or not path or Path(path).is_absolute() or ".." in Path(path).parts or field in filenames:
            parser.error(f"Invalid or duplicate EmployerFiles filename override: {value!r}")
        filenames[field] = str(Path(path))
    try:
        report = generate_csvs(args.guide, args.interview, employer=args.employer,
            all_employers=args.all_employers, output_dir=args.output_dir, review_state=args.review_state,
            files=replace(EmployerFiles(), **filenames))
    except (CSVGenerationError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Verified-only CSV generation: {report['status']}")
    for output in report["outputs"]:
        print(f"{output['path']}: verified payroll {output['verified_total']}; SHA-256 {output['sha256']}")
    for entry in report["processing"]["employers"]:
        print(f"{entry['employer']}: OPEN wages {entry['open_wages']}; OPEN adjustment basis {entry['open_adjustment_basis'] if entry['open_adjustment_basis'] is not None else 'NOT EVALUATED'}")
    for error in [*report["processing"]["errors"], *report["errors"]]:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"Review state: {report['review_state']}; OPEN findings and proposals require human review.")
    return 1 if report["status"] == "ERROR" else 0


if __name__ == "__main__":
    raise SystemExit(main())
