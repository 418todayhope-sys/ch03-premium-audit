"""Generate an evidence-validated payroll audit report; never approve OPEN cases."""

from __future__ import annotations

import argparse
import csv
from dataclasses import fields, replace
import hashlib
import io
import json
import os
from pathlib import Path
import sys
from urllib.parse import quote

from audit_questions import (build_question_plan, coverage_gaps, render_questions,
    _markdown_table, _md, _native_refs, _period_text, _refs)
from employer_processing import EmployerFiles, process_employer
from generate_codes import _preflight, _publish, _units, _verify_sources, validate_csv
from input_reader import read_markdown
from payroll_allocation import _money
from preview import employer_preview, run_preview


class ReportGenerationError(ValueError):
    """The supplied evidence and dependent outputs cannot support a report."""


def _total(values):
    return sum(_units(value, "Report money") for value in values)


def _amount(cents):
    return str(_money(cents))


def _controls(entry):
    """Independently resum encoded contributions, using exact integer cents."""
    employees, lines = entry["employee_payroll"], entry["adjustments"]["lines"]
    register = _total(e["register_wages"] for e in employees)
    allocated = open_wages = 0
    for employee in employees:
        parts = employee["parts"]
        if _total(p["wages"] for p in parts) != _units(employee["register_wages"], "Register"):
            raise ReportGenerationError(f"Employee parts do not reconcile: {employee['employee_id']}")
        allocated += _total(p["wages"] for p in parts if p["status"] == "ALLOCATED")
        open_wages += _total(p["wages"] for p in parts if p["status"] == "OPEN")
    basis = _total(line["input_record"]["amount"] for line in lines)
    added = _total(line["payroll_added"] for line in lines)
    nonpay = _total(line["nonpayroll"] for line in lines)
    open_basis = _total(line["unresolved_basis"] for line in lines)
    for line in lines:
        if _units(line["input_record"]["amount"], "Payment") != _total(line[k] for k in ("payroll_added", "nonpayroll", "unresolved_basis")):
            raise ReportGenerationError(f"Adjustment does not reconcile: {line['adjustment_id']}")
    verified = _total(entry["verified_by_code"].values())
    if register != allocated + open_wages or basis != added + nonpay + open_basis or verified != allocated + added:
        raise ReportGenerationError("Independent report payroll/payment reconciliation failed")
    if open_wages != _units(entry["open_wages"], "OPEN wages"):
        raise ReportGenerationError("OPEN wages differ from employee contributions")
    evaluated = entry["adjustments"]["evaluation"] == "EVALUATED"
    if evaluated and open_basis != _units(entry["open_adjustment_basis"], "OPEN adjustment basis"):
        raise ReportGenerationError("OPEN adjustment basis differs from payment contributions")
    return {key: _amount(value) for key, value in {
        "register": register, "allocated": allocated, "open_wages": open_wages,
        "basis": basis, "added": added, "nonpayroll": nonpay, "open_basis": open_basis,
        "verified": verified, "known_payroll": register + added, "cash": register + basis,
    }.items()} | {"adjustments_evaluated": evaluated}


def build_report_plan(question_plan, native_results):
    """Project existing decisions/questions, preserving every coverage obligation."""
    if coverage_gaps(question_plan):
        raise ReportGenerationError("Question plan has uncovered evidence")
    plan = {**question_plan, "employers": []}
    for original in question_plan["employers"]:
        employer = {**original, "items": list(original["questions"])}
        entry = employer["entry"]
        native = native_results[entry["directory"]]
        employer["controls"] = _controls(entry)
        application = entry["application"]
        employer["comparison_rows"] = []
        if application is not None:
            reported = {row["class_code"]: row["payroll"] for row in application["reported"]}
            references = {row["class_code"]: row["rationale_ref"] for row in employer["csv"]["rows"]}
            for code in sorted(set(reported) | set(entry["verified_by_code"])):
                old, new = reported.get(code, "0.00"), entry["verified_by_code"].get(code, "0.00")
                difference = _amount(_units(new, code) - _units(old, code))
                if difference != application["verified_differences"].get(code, "0.00"):
                    raise ReportGenerationError(f"Application difference does not reconcile: {code}")
                employer["comparison_rows"].append([code, old, new, difference,
                    references.get(code, "— no verified allocation")])
        employer["reported_headcount_conflict"] = application is not None and sum(row["employees"] for row in application["reported"]) != len(entry["employee_payroll"])
        unresolved = application is None or not application["definitive"] or employer["reported_headcount_conflict"] or any(
            _units(employer["controls"][key], key) for key in ("open_wages", "open_basis"))
        changed = application is not None and any(_units(row[3], "Difference") for row in employer["comparison_rows"])
        employer["disposition"] = "PARTIALLY UNRESOLVED" if unresolved else "CORRECTED" if changed else "ACCEPTED"
        employer["employee_comparisons"] = []
        sources = {ref["id"]: ref for ref in employer["sources"]}
        for comparison in native.employee_comparisons.values():
            employer["employee_comparisons"].append({
                "employee_id": comparison.employee_id, "wages": str(comparison.wages),
                "reported_code": comparison.reported_code, "calculated_code": comparison.calculated_code,
                "status": comparison.status, "inferred": comparison.reported_inferred,
                "reason": comparison.reason, "sources": _native_refs(comparison.sources, sources)})
        plan["employers"].append(employer)
    return plan


def load_report_plan(review_state, *, codes_dir, questions, files=EmployerFiles()):
    """Read-only validation: current sources, engine state, CSVs and question bytes."""
    try:
        review_state, codes_dir, questions = (Path(p).expanduser().resolve() for p in (review_state, codes_dir, questions))
        review_bytes, question_bytes = review_state.read_bytes(), questions.read_bytes()
        state = json.loads(review_bytes)
        if state["schema_version"] != 1 or state["allocation_scope"] != "VERIFIED_ONLY" or state["status"] == "ERROR" or state["errors"]:
            raise ReportGenerationError("A complete error-free verified-only review state is required")
        processing = state["processing"]
        if processing["mode"] not in {"single", "all"} or not processing["employers"]:
            raise ReportGenerationError("Review state must select one or more employers")
        selection = {"employer" if processing["mode"] == "single" else "all_employers": processing["discovery"]["root"]}
        if run_preview(processing["guide"], processing["interview"], files=files, **selection) != processing:
            raise ReportGenerationError("Current source/engine results differ from review state; regenerate dependent outputs")
        guide, interview = read_markdown(processing["guide"]), read_markdown(processing["interview"])
        outputs = {item["directory"]: item for item in state["outputs"]}
        if len(outputs) != len(state["outputs"]) or set(outputs) != {entry["directory"] for entry in processing["employers"]}:
            raise ReportGenerationError("Every selected employer must have exactly one CSV")
        filenames = {Path(item["path"]).name for item in outputs.values()}
        if len(filenames) != len(outputs) or {p.name for p in codes_dir.glob("*.csv")} != filenames:
            raise ReportGenerationError("Missing or unexpected employer CSV files")
        protected = {review_state: hashlib.sha256(review_bytes).hexdigest(), questions: hashlib.sha256(question_bytes).hexdigest()}
        cache, natives = {}, {}
        for entry in processing["employers"]:
            _verify_sources(processing, entry, cache)
            native = process_employer(processing["guide"], entry["directory"], processing["interview"], files=files)
            if employer_preview(Path(entry["directory"]), native) != entry:
                raise ReportGenerationError("Sources changed during native report processing")
            natives[entry["directory"]] = native
            item = outputs[entry["directory"]]
            path = (codes_dir / Path(item["path"]).name).resolve()
            payload = path.read_bytes()
            if hashlib.sha256(payload).hexdigest() != item["sha256"]:
                raise ReportGenerationError(f"CSV hash mismatch: {path}")
            text = payload.decode("utf-8")
            validate_csv(text, entry, guide)
            if list(csv.DictReader(io.StringIO(text, newline=""))) != item["rows"] or _total(row["payroll_allocated"] for row in item["rows"]) != _units(item["verified_total"], "CSV total"):
                raise ReportGenerationError(f"Review-state CSV rows/total mismatch: {path}")
            protected[path] = item["sha256"]
        protected.update({path.resolve(): digest for path, (digest, _) in cache.items()})
        question_plan = build_question_plan(state, natives, guide, interview, files=files)
        question_plan["review_state"] = str(review_state)
        for employer in question_plan["employers"]:
            employer["csv"] = {**employer["csv"], "path": str((codes_dir / Path(employer["csv"]["path"]).name).resolve())}
        if render_questions(question_plan).encode("utf-8") != question_bytes:
            raise ReportGenerationError("Supplied audit questions differ from current validated questions; resolve/regenerate questions before report")
        plan = build_report_plan(question_plan, natives)
        plan.update({"questions_path": str(questions), "protected": protected,
            "source_roots": [Path(processing["discovery"]["root"]).resolve(),
                             *(Path(e["directory"]).resolve() for e in processing["employers"])]})
        return plan
    except ReportGenerationError:
        raise
    except (OSError, ValueError, KeyError, TypeError, StopIteration) as exc:
        raise ReportGenerationError(f"Cannot prepare supported audit report: {exc}") from exc


def report_coverage_gaps(plan):
    return {employer["employer"]: sorted(missing) for employer in plan["employers"]
            if (missing := set(employer["required"]) - set().union(*(item["covers"] for item in employer["items"])))}


def _question_link(plan, identifier):
    return f"[{identifier}]({plan['questions_link']}#{identifier.lower()})"


def _refs_text(employer, references):
    sources = {ref["id"]: ref for ref in employer["sources"]}
    refs = sorted(set(references))
    if any(ref not in sources for ref in refs):
        raise ReportGenerationError("Unknown report citation identifier")
    return "; ".join(f"{key} {Path(sources[key]['source']).name}:{sources[key]['line_start']}-{sources[key]['line_end']} ({sources[key]['locator']})" for key in refs)


def _code_amounts(values):
    return "; ".join(f"{code} {value}" for code, value in sorted(values.items())) or "—"


def _render_controls(controls, *, evaluated):
    c = controls
    lines = ["Employee reconciliation (original register + verified additions = verified classified payroll + OPEN wages):", "",
        f"`{c['register']} + {c['added']} = {c['verified']} + {c['open_wages']}`; difference 0.00.", "",
        f"Known payroll basis (includes OPEN wages): ${c['known_payroll']}. Verified classified payroll: ${c['verified']}.", ""]
    if evaluated:
        lines.extend(["Payment reconciliation (evaluated payment basis = verified addition + nonpayroll + OPEN payment basis):", "",
            f"`{c['basis']} = {c['added']} + {c['nonpayroll']} + {c['open_basis']}`; difference 0.00.", "",
            "Cash reconciliation (original wages + evaluated payments = verified payroll + OPEN wages + excluded/nonpayroll payments + OPEN payment basis):", "",
            f"`{c['cash']} = {c['verified']} + {c['open_wages']} + {c['nonpayroll']} + {c['open_basis']}`; difference 0.00.", ""])
    else:
        lines.extend(["Other payment adjustments: **NOT EVALUATED**. No verified assertion of zero additional exposure is made; the wage reconciliation covers supplied employee records only.", ""])
    return lines


def render_report(plan):
    """Render supported results, review obligations and proposals as separate facts."""
    if report_coverage_gaps(plan):
        raise ReportGenerationError("Cannot render report with uncovered obligations")
    plan = {**plan, "questions_link": plan.get("questions_link", quote(plan["questions_path"], safe="/:"))}
    lines = ["# Classification and payroll audit report", "",
        "VERIFIED describes evidence-supported calculations, not final audit approval. OPEN wages and unresolved payment basis remain separate. UNAPPROVED PROPOSED treatments are excluded from every verified CSV and total. All linked questions remain unanswered.", "",
        "Responsible policy reviewer: auditor assigned to this file. Employer payroll/records contact confirms duties, identities, payment purposes and source completeness; the auditor decides rule applicability and approves any proposed treatment. Named policy authorities retain their original interview citations below; those citations do not appoint a reviewer for a new audit. No stakeholder has been contacted by this generator.", "",
        f"Review state: {_md(plan['review_state'])}. SHA-256 {plan['protected'][Path(plan['review_state'])]}.", "",
        f"Question document: [{_md(Path(plan['questions_path']).name)}]({plan['questions_link']}); SHA-256 {plan['protected'][Path(plan['questions_path'])]}.", "",
        "## Employer conclusions", ""]
    lines.extend(_markdown_table(["Employer", "Submitted split", "Verified CSV payroll", "OPEN wages", "OPEN payment basis"],
        [[e["name"], e["disposition"], e["controls"]["verified"], e["controls"]["open_wages"],
          e["controls"]["open_basis"] if e["controls"]["adjustments_evaluated"] else "NOT EVALUATED"] for e in plan["employers"]]))
    lines.extend(["## Recorded priority calls", "", "The interview records a first-call group; it establishes no order between its members and no universal ranking rule.", ""])
    if not plan["priorities"]:
        lines.extend(["No source-bound first-call choices fully match this run; the auditor must confirm the current priorities.", ""])
    for priority in plan["priorities"]:
        ref = priority["source"]
        lines.extend([f"- **{_md(priority['name'])}**: {_md(priority['reason'])} Recorded acknowledgement: {_md(ref['locator'])}, {_md(ref['source'])}:{ref['line_start']}-{ref['line_end']}; SHA-256 {ref['sha256']}.", ""])
    combined = {key: _amount(_total(e["controls"][key] for e in plan["employers"]))
                for key in ("register", "allocated", "open_wages", "basis", "added", "nonpayroll", "open_basis", "verified", "known_payroll", "cash")}
    lines.extend(["## Portfolio arithmetic controls", "", "Payment controls include only the evaluated adjustment records. NOT EVALUATED employer adjustments are outside that control; amounts are never estimates of missing exposure.", ""])
    lines.extend(_render_controls(combined, evaluated=any(e["controls"]["adjustments_evaluated"] for e in plan["employers"])))
    for employer in plan["employers"]:
        entry, c = employer["entry"], employer["controls"]
        sources = {ref["id"]: ref for ref in employer["sources"]}
        lines.extend([f"<a id=\"{employer['prefix'].lower()}\"></a>", f"## {_md(employer['name'])} ({_md(employer['employer'])})", "",
            f"Audit period: {_period_text(entry['audit_period'])}. Submitted split: **{employer['disposition']}**.", ""])
        if employer["disposition"] == "PARTIALLY UNRESOLVED":
            lines.extend(["Verified corrections and supported components are shown below; the full submitted split cannot yet be accepted. Differences are a **provisional comparison** of verified CSV payroll minus reported payroll. An OPEN wage omission is **not a verified payroll reduction**; unresolved payment basis may change the final allocation after evidence and approval.", ""])
        elif employer["disposition"] == "CORRECTED":
            lines.extend(["The submitted split requires the verified class transfers/additions below. This arithmetic correction remains subject to the linked employer confirmations and auditor sign-off.", ""])
        else:
            lines.extend(["The submitted monetary split is accepted for the evidenced classifications: verified amounts match the application. This is not approval of unanswered evidence questions or unevaluated payment exposure.", ""])
        lines.extend([f"Verified-only CSV: {_md(employer['csv']['path'])}; SHA-256 {employer['csv']['sha256']}.", ""])
        if entry["application"] is not None:
            application = entry["application"]
            lines.extend(_markdown_table(["Code", "Reported payroll", "Verified payroll", "Difference (verified minus reported)", "Verified code paragraph"], employer["comparison_rows"]))
            lines.extend([f"Reported total ${application['reported_total']}; original register ${application['register_total']}; register-minus-reported difference ${application['register_difference']}. Comparison definitive for current classifications: {application['definitive']} (not human approval).", "",
                "Application reported employee counts: " + "; ".join(f"{row['class_code']}: {row['employees']}" for row in application["reported"]) + f". Register employees: {len(entry['employee_payroll'])}.", "",
                "Application sources: " + _md(_refs_text(employer, _refs(application, sources))) + ".", ""])
            if employer["reported_headcount_conflict"]:
                lines.extend(["The total reported employee count conflicts with the register; the employer must confirm the reporting population before the submitted split can be accepted, even if dollar totals match.", ""])
        else:
            lines.extend(["Reported application split is unavailable; obtain the employer's submission before accepting a comparison.", ""])
        lines.extend(["### Employee payroll — VERIFIED and OPEN", ""])
        lines.extend(_markdown_table(["Employee ID", "Name", "Original wages", "VERIFIED wage allocation", "VERIFIED additions", "OPEN wages", "Register source"],
            [[e["employee_id"], e["name"], e["register_wages"], _code_amounts(e["verified_wages_by_code"]),
              _code_amounts(e["verified_adjustment_by_code"]), e["open_wages"], _refs_text(employer, [e["source"]])]
             for e in entry["employee_payroll"]]))
        if employer["employee_comparisons"]:
            names = {e["employee_id"]: e["name"] for e in entry["employee_payroll"]}
            lines.extend(["Employee-level application assignments below are marked inferred where the engine derives them from the submitted counts/payroll; they are not employer-supplied employee coding lists.", ""])
            lines.extend(_markdown_table(["Employee", "Wage basis", "Reported code", "Calculated code", "Status", "Reported attribution", "Reason / records"],
                [[f"{item['employee_id']} {names[item['employee_id']]}", item["wages"], item["reported_code"] or "UNCONFIRMED",
                  item["calculated_code"] or "OPEN", item["status"], "UNCONFIRMED" if item["reported_code"] is None else "INFERRED — confirm" if item["inferred"] else "DOCUMENTED",
                  item["reason"] + " " + _refs_text(employer, item["sources"])] for item in employer["employee_comparisons"]]))
        else:
            lines.extend(["No engine-supported employee-level application coding list is available. Individual results and weekly transfers below are evidenced calculations; only the aggregate submitted split is directly compared.", ""])
        lines.extend(["### Applied rule boundaries", "",
            "Each decision retains the existing evaluator's scope and conditions. OPEN decisions below describe an applicability/evidence gap, not an assigned classification. Payment rule reasons and exact references are also preserved with each adjustment.", ""])
        decisions = [part["decision"] for employee in entry["employee_payroll"] for part in employee["parts"]]
        decisions.extend(line["input_record"].get("decision") for line in entry["adjustments"]["lines"])
        unique = {}
        for decision in decisions:
            if decision:
                key = (decision["rule"], decision["status"], decision["scope"], tuple(decision["applicability"]), tuple(decision["rule_sources"]))
                unique.setdefault(key, decision)
        lines.extend(_markdown_table(["Rule", "Decision status", "Scope", "Applicability boundaries", "Exact rule sources"],
            [[d["rule"], d["status"], d["scope"], "; ".join(d["applicability"]), _refs_text(employer, d["rule_sources"])]
             for d in unique.values()]))
        lines.extend(["### Reconciliation and excluded payments", ""])
        lines.extend(_render_controls(c, evaluated=c["adjustments_evaluated"]))
        lines.extend(_markdown_table(["Engine control", "Reconciled", "Difference"],
            [[key, check["reconciled"], check.get("difference", "see review state")] for key, check in entry["reconciliation"].items() if check is not None]))
        if entry["owner"] is not None:
            owner = entry["owner"]
            lines.extend([f"Owner {_md(owner['name'])}: **{owner['status']}**; removed register wages ${owner['removed_wages']}. {_md(owner['reason'])} Records: {_md(_refs_text(employer, _refs(owner, sources)))}.", ""])
        if entry["governing_field"] is not None:
            field = entry["governing_field"]
            lines.extend([f"Governing field code: {field['class_code'] or 'OPEN'}; supported field payroll {_md(_code_amounts(field['by_code']))}. {_md(field['reason'])} Exact evidence and rule references follow in the review detail and source index.", ""])
        lines.extend(["### OPEN findings and required human resolution", "",
            "Each finding remains unanswered even if its monetary effect is zero. Employer payroll/records contact supplies the requested records; responsible policy reviewer: auditor. Identity issues require documentary confirmation of the exact employee/payee, not an assumed alias.", ""])
        if not entry["questions"]:
            lines.extend(["No additional structured findings were recorded; the linked source and employer confirmations still require human review.", ""])
        for index, finding in enumerate(entry["questions"]):
            linked = [_question_link(plan, item["id"]) for item in employer["items"] if f"finding:{index}" in item["covers"]]
            lines.extend([f"- **OPEN — {_md(finding['subject'])}**: {_md(finding['reason'])} Required evidence/confirmation: {_md(finding['required_confirmation'])} Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: {', '.join(linked)}. Records: {_md(_refs_text(employer, _refs(finding, sources)))}.", ""])
        lines.extend(["### UNAPPROVED PROPOSED treatments", "", "These alternatives are outside all verified totals. They require the specific evidence below and explicit auditor approval, followed by a supported rerun.", ""])
        if not entry["proposals"]:
            lines.extend(["No supported conditional treatment is recorded; do not invent one for the OPEN cases.", ""])
        for index, proposal in enumerate(entry["proposals"]):
            treatment = proposal["treatment"]
            linked = [_question_link(plan, item["id"]) for item in employer["items"] if f"proposal:{index}" in item["covers"]]
            if proposal["kind"] == "classification":
                detail = f"Candidate {treatment['class_code'] or 'UNCONFIRMED'}; wage basis ${treatment['wages']}; paragraph {treatment['rationale_ref'] or 'UNCONFIRMED'}."
                confirmations = treatment["required_confirmation"]
            else:
                detail = f"Candidate {proposal['work_code'] or 'UNCONFIRMED'}; proposed payroll ${treatment['payroll_added']}; proposed nonpayroll ${treatment['nonpayroll']}."
                confirmations = proposal["required_confirmation"]
            lines.extend([f"- **UNAPPROVED — {_md(proposal['subject'])}**: {detail} {_md(treatment['reason'])} Required confirmation: {_md('; '.join(confirmations))} Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: {', '.join(linked)}.", ""])
        lines.extend(["### Allocation, payment and evidence review detail", "",
            "The following entries preserve each employee/pay week, adjustment/payment, deciding reason and record confirmation. VERIFIED calculations, OPEN findings and UNAPPROVED alternatives retain their original labels. Exact dated record fields and all confirmation prompts are in the linked question document.", ""])
        for item in employer["items"]:
            lines.extend([f"#### {item['id']} — {_md(item['subject'])}", "", f"**{item['status']}**. Follow-up: {_question_link(plan, item['id'])}.", ""])
            for reason in item["why"]:
                lines.extend([_md(reason), ""])
            for table in item["tables"]:
                rows = table["rows"]
                if "Code" in table["columns"] and "Status" in table["columns"] and "Verified payroll" in table["columns"]:
                    code, status, payroll = (table["columns"].index(name) for name in ("Code", "Status", "Verified payroll"))
                    rows = [list(row) for row in rows]
                    for row in rows:
                        if row[code] == "OPEN" and row[status] == "VERIFIED" and not _units(row[payroll], "Verified payment payroll"):
                            row[code] = "— no payroll allocation"
                lines.extend(_markdown_table(table["columns"], rows))
            lines.extend(["Supporting source IDs (local to this employer; exact locators below): " + ", ".join(sorted(item["sources"])) + ".", "",
                "Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.", ""])
        lines.extend(["<details>", f"<summary>Source and rule index — {len(employer['sources'])} exact citations</summary>", "",
            "Original Classification Guide paragraph identifiers and interview timestamps/line spans are preserved here. Rule applicability is bounded by the recorded decision; a citation is not permission to extend a contractor practice to another business. Physical CSV row identities and confirmation links are preserved in the question document's record index.", ""])
        lines.extend(_markdown_table(["Source ID", "Original document", "Original paragraph / interview / record locator", "Lines"],
            [[ref["id"], ref["source"], ref["locator"], f"{ref['line_start']}-{ref['line_end']}"] for ref in employer["sources"]]))
        hashes = {ref["source"]: ref["sha256"] for ref in employer["sources"]}
        hashes.update({ref["path"]: ref["sha256"] for ref in entry["source_manifest"]})
        lines.extend(_markdown_table(["Original source file", "SHA-256"], sorted(hashes.items())))
        lines.extend(["</details>", ""])
    lines.extend(["## Scope and remaining limitations", "",
        "This report rereads the supplied authoritative paths and requires the current processing, CSVs and unanswered question document to agree. It supports the existing evidence schemas; unsupported duties or incomplete evidence remain OPEN. There is no source locking, atomic multi-file snapshot, approval ledger, external certificate verification, rate calculation or premium quote. Final-source hashes detect changes before publication but do not authenticate source authorship or resolve factual contradictions. Payment proposals may retain fractional cents pending an explicit rounding decision; they never enter verified totals. Future runs need current auditor-supplied locations and regenerated dependent outputs when sources change.", ""])
    return "\n".join(lines).rstrip("\n") + "\n"


def generate_report(review_state, *, codes_dir, questions, output, files=EmployerFiles()):
    """Validate dependencies, publish one report without replacing differing files."""
    try:
        plan = load_report_plan(review_state, codes_dir=codes_dir, questions=questions, files=files)
        argument = Path(output).expanduser().absolute()
        if argument.is_symlink():
            raise ReportGenerationError("Report output must not be a symbolic-link file")
        output = argument.resolve()
        if output in plan["protected"] or any(output.is_relative_to(root) for root in plan["source_roots"]):
            raise ReportGenerationError("Report output must be separate from authoritative inputs and dependent outputs")
        plan["questions_link"] = quote(os.path.relpath(plan["questions_path"], output.parent), safe="/:")
        payload = render_report(plan).encode("utf-8")
        _preflight(output, payload)
        for path, digest in plan["protected"].items():
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise ReportGenerationError(f"Input changed before report publication: {path}")
        _publish(output, payload)
        if output.read_bytes() != payload:
            raise ReportGenerationError("Published report failed byte verification")
        employers = plan["employers"]
        return {"path": str(output), "sha256": hashlib.sha256(payload).hexdigest(),
            "employers": [{"employer": e["employer"], "disposition": e["disposition"], "verified_total": e["controls"]["verified"],
                           "open_wages": e["controls"]["open_wages"], "open_adjustment_basis": e["entry"]["open_adjustment_basis"]} for e in employers],
            "coverage": {"employers": len(employers),
                "employees": sum(len(e["entry"]["employee_payroll"]) for e in employers),
                "payroll_parts": sum(len(employee["parts"]) for e in employers for employee in e["entry"]["employee_payroll"]),
                "adjustments": sum(len(e["entry"]["adjustments"]["lines"]) for e in employers),
                "findings": sum(len(e["entry"]["questions"]) for e in employers),
                "proposals": sum(len(e["entry"]["proposals"]) for e in employers),
                "questions": sum(len(e["items"]) for e in employers), "sources": sum(len(e["sources"]) for e in employers),
                "records": sum(len(e["records"]) for e in employers)},
            "uncovered": report_coverage_gaps(plan), "priorities": plan["priorities"]}
    except ReportGenerationError:
        raise
    except (OSError, ValueError, KeyError, TypeError, StopIteration) as exc:
        raise ReportGenerationError(f"Cannot generate supported audit report: {exc}") from exc


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for argument in ("review-state", "codes-dir", "questions", "output"):
        parser.add_argument(f"--{argument}", required=True, type=Path)
    parser.add_argument("--file", action="append", default=[], metavar="FIELD=RELATIVE_PATH")
    args = parser.parse_args(argv)
    overrides, allowed = {}, {field.name for field in fields(EmployerFiles)}
    for argument in args.file:
        name, separator, value = argument.partition("=")
        if not separator or name not in allowed or name in overrides or not value or Path(value).is_absolute() or ".." in Path(value).parts:
            parser.error(f"Invalid or duplicate EmployerFiles override: {argument!r}")
        overrides[name] = str(Path(value))
    try:
        report = generate_report(args.review_state, codes_dir=args.codes_dir, questions=args.questions,
            output=args.output, files=replace(EmployerFiles(), **overrides))
    except ReportGenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Report: {report['path']} SHA-256 {report['sha256']}")
    for employer in report["employers"]:
        print(f"{employer['employer']}: {employer['disposition']}; verified {employer['verified_total']}; OPEN wages {employer['open_wages']}; OPEN adjustment basis {employer['open_adjustment_basis'] or 'NOT EVALUATED'}")
    print(f"Coverage: {report['coverage']}; uncovered: {report['uncovered']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
