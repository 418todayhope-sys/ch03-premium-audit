"""Run source-bound employer previews on stdout; never write audit deliverables."""

from __future__ import annotations

import argparse
from dataclasses import fields, is_dataclass, replace
from datetime import date
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import sys

from employer_processing import EmployerFiles, process_employer
from input_reader import InputError, read_markdown
from payroll_allocation import _cents, _money
from rule_evaluator import SourceReference


class SourceCatalog:
    """Deduplicate citations without duplicating entire source documents in output."""

    def __init__(self):
        self.entries = []
        self.identifiers = {}

    def reference(self, ref):
        key = ref.source, ref.locator, ref.line_start, ref.line_end, ref.sha256
        if key not in self.identifiers:
            identifier = f"S{len(self.entries) + 1:04d}"
            self.identifiers[key] = identifier
            self.entries.append(dict(id=identifier, source=ref.source, locator=ref.locator,
                line_start=ref.line_start, line_end=ref.line_end, sha256=ref.sha256))
        return self.identifiers[key]

    def encode(self, value):
        if isinstance(value, SourceReference):
            return self.reference(value)
        if isinstance(value, Decimal):
            return str(value)
        if isinstance(value, (date, Path)):
            return value.isoformat() if isinstance(value, date) else str(value)
        if is_dataclass(value):
            result = {field.name: self.encode(getattr(value, field.name)) for field in fields(value)}
            if hasattr(value, "reconciled"):
                result["reconciled"] = bool(value.reconciled)
            return result
        if isinstance(value, dict):
            if all(isinstance(key, str) for key in value):
                return {key: self.encode(item) for key, item in value.items()}
            return [{"key": self.encode(key), "value": self.encode(item)} for key, item in sorted(value.items(), key=lambda pair: repr(pair[0]))]
        if isinstance(value, (list, tuple)):
            return [self.encode(item) for item in value]
        if value is None or isinstance(value, (str, bool, int)):
            return value
        raise TypeError(f"Unsupported preview value type: {type(value).__name__}")


def _manifest(document):
    return {"path": str(document.path), "sha256": hashlib.sha256(document.text.encode("utf-8")).hexdigest(),
            "kind": "csv" if hasattr(document, "columns") else "markdown"}


def _error(kind, message):
    return {"type": kind, "message": str(message)}


def _unavailable(directory, errors):
    return {"employer": directory.name, "directory": str(directory), "status": "ERROR", "errors": errors,
        "verified_by_code": None, "open_wages": None, "open_adjustment_basis": None,
        "employee_payroll": [], "proposals": [], "questions": [], "reconciliation": {},
        "application": None, "source_manifest": [], "sources": []}


def employer_preview(directory, result, errors=()):
    """Project existing decisions; do not evaluate, repair or approve business rules."""
    catalog = SourceCatalog()
    errors = list(errors)
    checks = {
        "allocation": result.allocation.reconciliation if result.allocation else None,
        "independent": result.independent_reconciliation,
        "adjustments": result.adjustments.reconciliation if result.adjustments and result.adjustments.lines else None,
        "weekly": result.weekly_reconciliation,
        "combined": result.combined_reconciliation,
        "travel": result.travel_reconciliation,
    }
    if result.allocation is None or result.independent_reconciliation is None:
        errors.append(_error("ProcessingUnavailable", "; ".join(item.reason for item in result.open_items) or "No verified register/allocation is available."))
    for name, check in checks.items():
        if check is not None and not check.reconciled:
            errors.append(_error("ReconciliationError", f"{name} reconciliation failed; retain the original OPEN findings and controls."))
    weekly = {item.part_id: item for item in result.weekly_results}
    employees = []
    rule_refs = []
    for employee in result.register:
        totals = {}
        pending = 0
        parts = []
        for line in result.allocation.lines if result.allocation else ():
            if line.employee.employee_id != employee.employee_id:
                continue
            if line.status == "OPEN":
                pending += _cents(line.wages, line.part.part_id)
            else:
                totals[line.class_code] = totals.get(line.class_code, 0) + _cents(line.wages, line.part.part_id)
            detail = {"part_id": line.part.part_id, "wages": str(line.wages), "status": line.status,
                "class_code": line.class_code, "rationale_ref": line.rationale_ref, "source": catalog.encode(line.part.source),
                "scope": line.part.scope, "decision": catalog.encode(line.decision),
                "required_confirmation": list(line.required_confirmation)}
            if line.part.part_id in weekly:
                item = weekly[line.part.part_id]
                detail.update(week_start=item.week_start.isoformat(), week_end=item.week_end.isoformat(),
                    ride_days=catalog.encode(item.ride_days), route_sources=catalog.encode(item.route_sources))
            if line.decision:
                rule_refs.extend(catalog.encode(line.decision.rule_sources))
            parts.append(detail)
        additions = {}
        for adjustment in result.adjustments.lines if result.adjustments else ():
            if (adjustment.status == "VERIFIED" and adjustment.class_code and
                getattr(adjustment.input_record, "employee_id", None) == employee.employee_id):
                code = adjustment.class_code
                additions[code] = additions.get(code, 0) + _cents(adjustment.payroll_added, adjustment.adjustment_id)
        combined = dict(totals)
        for code, value in additions.items():
            combined[code] = combined.get(code, 0) + value
        if employee.employee_id in result.employee_totals:
            combined = {code: _cents(value, employee.employee_id) for code, value in result.employee_totals[employee.employee_id].items() if code != "OPEN"}
        employees.append({"employee_id": employee.employee_id, "name": employee.name,
            "register_wages": str(employee.wages), "source": catalog.encode(employee.source),
            "verified_wages_by_code": {code: str(_money(value)) for code, value in sorted(totals.items())},
            "verified_adjustment_by_code": {code: str(_money(value)) for code, value in sorted(additions.items())},
            "verified_by_code": {code: str(_money(value)) for code, value in sorted(combined.items())},
            "open_wages": str(_money(pending)) if result.allocation else None, "parts": parts})
    proposals = [{"kind": "classification", "subject": key, "treatment": catalog.encode(value)}
                 for key, value in sorted(result.proposals.items())]
    for line in result.adjustments.lines if result.adjustments else ():
        rule_refs.extend(catalog.encode(line.rule_sources))
        if line.proposal:
            decision = line.input_record.decision
            proposals.append({"kind": "adjustment", "subject": line.adjustment_id,
                "work_code": decision.class_code if decision and decision.status == "CLASSIFIED" else None, "treatment": catalog.encode(line.proposal),
                "required_confirmation": list(line.required_confirmation), "rule_sources": catalog.encode(line.rule_sources),
                "evidence_sources": catalog.encode(line.evidence_sources)})
    review = bool(result.open_items or proposals or any(line.status == "OPEN" for line in (result.allocation.lines if result.allocation else ())))
    output = {"employer": directory.name, "directory": str(directory),
        "status": "ERROR" if errors else "REVIEW" if review else "OK", "errors": errors,
        "audit_period": catalog.encode(result.period),
        "verified_by_code": catalog.encode(result.by_code) if result.allocation else None,
        "open_wages": str(result.independent_reconciliation.unresolved_total) if result.independent_reconciliation else None,
        "open_adjustment_basis": str(result.adjustments.reconciliation.unresolved_basis) if result.adjustments and result.adjustments.lines else None,
        "employee_payroll": employees, "proposals": proposals,
        "questions": catalog.encode(result.open_items), "reconciliation": catalog.encode(checks),
        "adjustments": {"evaluation": "EVALUATED" if result.adjustments and result.adjustments.lines else "NOT_EVALUATED",
            "verified_by_code": catalog.encode(result.adjustments.by_code) if result.adjustments and result.adjustments.lines else None,
            "lines": catalog.encode(result.adjustments.lines) if result.adjustments else []},
        "application": catalog.encode(result.application), "owner": catalog.encode(result.owner_assessment),
        "governing_field": catalog.encode(result.governing_field), "receipts": catalog.encode(result.receipts),
        "rule_references": list(dict.fromkeys(rule_refs)),
        "source_manifest": [_manifest(document) for document in (result.inputs.guide, *result.inputs.records)] if result.inputs else []}
    output["sources"] = catalog.entries
    return output


def _execute(guide, interview, directory, files):
    try:
        errors = [_error("MissingSource", f"Required employer source is missing: {directory / filename}")
            for filename in (files.business, files.notes, files.payroll, files.application) if not (directory / filename).is_file()]
        result = process_employer(guide, directory, interview, files=files)
        return employer_preview(directory, result, errors)
    except Exception as exc:
        # Isolate unexpected employer failures as well as source failures. Never
        # turn an exception into zero payroll or reuse a previous employer result.
        return _unavailable(directory, [_error(type(exc).__name__, exc)])


def run_preview(guide, interview, *, employer=None, all_employers=None, files=EmployerFiles()):
    """Return a deterministic in-memory preview, rereading sources on every call."""
    if (employer is None) == (all_employers is None):
        raise ValueError("Select exactly one employer directory or all-employers directory")
    guide, interview = (Path(path).expanduser().absolute() for path in (guide, interview))
    root = Path(employer if employer is not None else all_employers).expanduser().absolute()
    report = {"schema_version": 1, "preview_only": True, "status": "ERROR", "mode": "single" if employer is not None else "all",
        "guide": str(guide), "interview": str(interview), "shared_sources": [],
        "discovery": {"root": str(root), "method": "selected_directory" if employer is not None else "immediate_nonhidden_subdirectories", "excluded_entries": []},
        "errors": [], "employers": []}
    try:
        for source in (guide, interview):
            document = read_markdown(source)
            if source == guide and not document.paragraph_ids:
                raise InputError(f"{guide}: no classification paragraph identifiers found")
            report["shared_sources"].append(_manifest(document))
        if not root.is_dir():
            raise InputError(f"Employer input directory is missing or is not a directory: {root}")
        if employer is not None:
            directories = [root]
        else:
            entries = sorted(root.iterdir(), key=lambda path: path.name)
            directories = [path for path in entries if not path.name.startswith(".") and path.is_dir()]
            report["discovery"]["excluded_entries"] = [path.name for path in entries if path not in directories]
            if not directories:
                raise InputError(f"No employer subdirectories were discovered in {root}")
    except (InputError, OSError) as exc:
        report["errors"].append(_error(type(exc).__name__, exc))
        return report
    seen = {}
    for directory in directories:
        try:
            canonical = directory.resolve(strict=True)
            if canonical in seen:
                entry = _unavailable(directory, [_error("DuplicateDirectoryAlias", f"Directory alias duplicates {seen[canonical]}; the same employer sources are not processed twice.")])
            else:
                seen[canonical] = directory
                entry = _execute(guide, interview, directory, files)
        except (OSError, RuntimeError) as exc:
            entry = _unavailable(directory, [_error(type(exc).__name__, exc)])
        report["employers"].append(entry)
    statuses = {entry["status"] for entry in report["employers"]}
    report["status"] = "ERROR" if "ERROR" in statuses else "REVIEW" if "REVIEW" in statuses else "OK"
    return report


def render_text(report):
    lines = ["PREVIEW ONLY — no final deliverable files", f"Status: {report['status']}",
        f"Guide: {report['guide']}", f"Interview: {report['interview']}"]
    for error in report["errors"]:
        lines.append(f"ERROR {error['type']}: {error['message']}")
    if report["discovery"]["excluded_entries"]:
        lines.append("Excluded container entries: " + ", ".join(report["discovery"]["excluded_entries"]))
    for employer in report["employers"]:
        lines.extend(["", f"Employer: {employer['employer']} [{employer['status']}]", f"Records: {employer['directory']}"])
        for error in employer["errors"]:
            lines.append(f"ERROR {error['type']}: {error['message']}")
        lines.append("Verified class-code totals: " + ((", ".join(f"{code} ${amount}" for code, amount in employer["verified_by_code"].items()) or "none verified") if employer["verified_by_code"] is not None else "UNAVAILABLE"))
        lines.append(f"OPEN wages: {employer['open_wages'] if employer['open_wages'] is not None else 'UNAVAILABLE'}")
        lines.append(f"OPEN adjustment basis: {employer['open_adjustment_basis'] if employer['open_adjustment_basis'] is not None else 'NOT EVALUATED'}")
        used = set(employer.get("rule_references", ()))
        for employee in employer["employee_payroll"]:
            used.add(employee["source"])
            codes = ", ".join(f"{code} ${amount}" for code, amount in employee["verified_by_code"].items()) or "no verified code"
            lines.append(f"  {employee['employee_id']} {employee['name']}: register ${employee['register_wages']}; verified payroll {codes}; OPEN wages {employee['open_wages']} [{employee['source']}]")
        for name, check in employer["reconciliation"].items():
            if check is not None:
                figures = ", ".join(f"{key}={value}" for key, value in check.items() if isinstance(value, str) and key != "reconciled")
                lines.append(f"Reconciliation {name}: {'PASS' if check['reconciled'] else 'FAIL'}; {figures}")
        application = employer["application"]
        lines.append("Reported differences: " + (", ".join(f"{code} {amount}" for code, amount in application["verified_differences"].items()) + f"; definitive={application['definitive']}" if application else "UNAVAILABLE"))
        for proposal in employer["proposals"]:
            treatment = proposal["treatment"]
            money = f"payroll addition {treatment['payroll_added']}, nonpayroll {treatment['nonpayroll']}, work code {proposal['work_code'] or 'UNCONFIRMED'}" if proposal["kind"] == "adjustment" else f"code {treatment['class_code']}, wage basis {treatment['wages']}"
            lines.append(f"UNAPPROVED proposal {proposal['subject']}: {money}; {treatment['reason']}")
            used.update(proposal.get("rule_sources", treatment.get("rule_sources", ())))
            used.update(proposal.get("evidence_sources", treatment.get("evidence_sources", ())))
            for confirmation in proposal.get("required_confirmation", treatment.get("required_confirmation", ())):
                lines.append(f"  Confirm: {confirmation}")
        for question in employer["questions"]:
            lines.append(f"REVIEW {question['subject']}: {question['reason']}")
            lines.append(f"  Confirm: {question['required_confirmation']}")
            used.update(question["sources"])
        for source in employer["source_manifest"]:
            lines.append(f"Source: {source['path']} SHA-256 {source['sha256']}")
        for ref in employer["sources"]:
            if ref["id"] in used:
                lines.append(f"[{ref['id']}] {ref['source']}:{ref['line_start']}-{ref['line_end']} {ref['locator']} SHA-256 {ref['sha256']}")
        lines.append("Full per-part evidence and controls are available with --format json.")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guide", required=True, type=Path, help="Authoritative Classification Guide Markdown")
    parser.add_argument("--interview", required=True, type=Path, help="Authoritative verified house-practice interview Markdown")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--employer", type=Path, help="One selected employer's record directory")
    mode.add_argument("--all-employers", type=Path, help="Container whose immediate nonhidden employer folders are processed")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="Preview on stdout (default: text)")
    parser.add_argument("--file", action="append", default=[], metavar="FIELD=RELATIVE_PATH", help="Override an EmployerFiles filename; repeat for different fields")
    args = parser.parse_args(argv)
    filenames = {}
    allowed = {field.name for field in fields(EmployerFiles)}
    for value in args.file:
        field, separator, path = value.partition("=")
        if not separator or field not in allowed or not path or Path(path).is_absolute() or ".." in Path(path).parts or field in filenames:
            parser.error(f"Invalid or duplicate filename override {value!r}; use a known EmployerFiles field and a relative path within each employer directory")
        filenames[field] = str(Path(path))
    report = run_preview(args.guide, args.interview, employer=args.employer, all_employers=args.all_employers,
                         files=replace(EmployerFiles(), **filenames))
    print(json.dumps(report, indent=2, ensure_ascii=False) if args.format == "json" else render_text(report), end="\n" if args.format == "json" else "")
    for error in report["errors"]:
        print(f"ERROR {error['type']}: {error['message']}", file=sys.stderr)
    for employer in report["employers"]:
        for error in employer["errors"]:
            print(f"ERROR [{employer['employer']}] {error['type']}: {error['message']}", file=sys.stderr)
    return 1 if report["status"] == "ERROR" else 0


if __name__ == "__main__":
    raise SystemExit(main())
