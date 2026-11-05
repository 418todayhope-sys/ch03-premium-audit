"""Build source-validated employer confirmation questions without changing decisions."""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, fields, replace
from decimal import Decimal
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path
import re
import sys

from employer_processing import EmployerFiles, process_employer
from generate_codes import _preflight, _publish, _units, _verify_sources, validate_csv
from input_reader import read_csv, read_markdown
from payroll_allocation import _money
from preview import employer_preview, run_preview
from rule_evaluator import _MESSAGE, _reference


class QuestionGenerationError(ValueError):
    """Questions cannot be supported by the supplied engine state and evidence."""


def _sum_money(values):
    """Sum displayed amounts exactly, retaining sub-cent conditional proposals."""
    values = [Decimal(value) for value in values if value is not None]
    if any(not value.is_finite() for value in values):
        raise QuestionGenerationError("Non-finite amount in question details")
    places = max([2, *(-value.as_tuple().exponent for value in values)])
    total = sum((Fraction(value) for value in values), Fraction())
    scaled = total * 10 ** places
    if scaled.denominator != 1:
        raise QuestionGenerationError("Non-decimal proposal total")
    units = scaled.numerator
    whole, fraction = divmod(abs(units), 10 ** places)
    return f"{'-' if units < 0 else ''}{whole}.{fraction:0{places}d}"


def _period_text(period):
    return f"{period['start']} through {period['end']}" if period is not None else "unconfirmed audit dates"


def _refs(value, sources):
    """Read encoded citation fields, rather than mistaking employee IDs for refs."""
    found = set()
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"source", "sources", "rule_sources", "evidence_sources", "route_sources", "days_source", "rate_source"}:
                items = item if isinstance(item, list) else [item]
                found.update(ref for ref in items if isinstance(ref, str) and ref in sources)
            if isinstance(item, (dict, list)):
                found.update(_refs(item, sources))
    elif isinstance(value, list):
        for item in value:
            found.update(_refs(item, sources))
    return found


def _native_refs(refs, sources):
    keys = {(r["source"], r["locator"], r["line_start"], r["line_end"], r["sha256"]): r["id"]
            for r in sources.values()}
    result = set()
    for ref in refs:
        key = ref.source, ref.locator, ref.line_start, ref.line_end, ref.sha256
        if key not in keys:
            raise QuestionGenerationError(f"Native evidence is absent from review state: {ref.source} {ref.locator}")
        result.add(keys[key])
    return result


def _title(native, files):
    document = next(doc for doc in native.inputs.records
                    if str(doc.path.relative_to(native.inputs.records_root)) == files.business)
    match = re.search(r"(?m)^#\s+(.+)$", document.text)
    title = match.group(1).strip() if match else native.inputs.records_root.name
    return re.sub(r":\s*business description\s*$", "", title, flags=re.I)


def _records(entry, prefix):
    """Index physical CSV records, including rows cited through whole-file refs."""
    records = []
    for manifest in entry["source_manifest"]:
        if manifest["kind"] != "csv":
            continue
        document = read_csv(manifest["path"])
        if hashlib.sha256(document.text.encode("utf-8")).hexdigest() != manifest["sha256"]:
            raise QuestionGenerationError(f"Source changed while indexing: {document.path}")
        for index, row in enumerate(document.rows):
            start = row.line_number
            end = document.rows[index + 1].line_number - 1 if index + 1 < len(document.rows) else len(document.text.splitlines())
            refs = [ref["id"] for ref in entry["sources"] if ref["source"] == str(document.path)
                    and ref["line_start"] <= end and start <= ref["line_end"]]
            if not refs:
                continue
            identifier = f"{prefix}-R{len(records) + 1:04d}"
            records.append({"id": identifier, "source": str(document.path), "line_start": start,
                "line_end": end, "values": {key: str(value) for key, value in row.values.items()},
                "source_ids": refs, "questions": []})
    return records


def _expected(entry, records):
    expected = {f"source:{ref['id']}" for ref in entry["sources"]}
    expected.update(f"record:{row['id']}" for row in records)
    expected.update(f"file:{manifest['path']}" for manifest in entry["source_manifest"])
    for employee in entry["employee_payroll"]:
        expected.add(f"employee:{employee['employee_id']}")
        expected.update(f"part:{part['part_id']}" for part in employee["parts"])
    expected.update(f"adjustment:{line['adjustment_id']}" for line in entry["adjustments"]["lines"])
    expected.update(f"finding:{index}" for index, _ in enumerate(entry["questions"]))
    expected.update(f"proposal:{index}" for index, _ in enumerate(entry["proposals"]))
    expected.update(f"control:{name}" for name, check in entry["reconciliation"].items() if check is not None)
    expected.update(f"csv:{code}" for code, amount in entry["verified_by_code"].items() if _units(amount, code))
    if entry["owner"] is not None:
        expected.add("owner")
    if entry["receipts"] is not None:
        expected.add("receipts")
    if entry["governing_field"] is not None:
        expected.add("governing_field")
    return expected


def _question(kind, subject, status="VERIFIED CALCULATION / EMPLOYER CONFIRMATION", *, employee_ids=(), payees=()):
    return {"id": "", "kind": kind, "subject": subject, "status": status, "confirm": [],
        "why": [], "tables": [], "sources": set(), "covers": set(),
        "employee_ids": set(employee_ids), "payees": set(payees)}


def _table(question, columns, rows):
    question["tables"].append({"columns": columns, "rows": rows})


def _add_finding(question, finding, index, sources):
    question["covers"].add(f"finding:{index}")
    question["sources"].update(_refs(finding, sources))
    question["confirm"].extend(re.split(r"(?<=\.)\s*;\s+", finding["required_confirmation"]))
    question["why"].append(finding["reason"])
    if question["status"] == "VERIFIED CALCULATION / EMPLOYER CONFIRMATION":
        question["status"] = "VERIFIED CALCULATION + OPEN FINDING / HUMAN CONFIRMATION REQUIRED"


def _proposals(question, proposals, sources):
    for index, proposal in proposals:
        treatment = proposal["treatment"]
        question["status"] = "OPEN / HUMAN APPROVAL REQUIRED"
        question["covers"].add(f"proposal:{index}")
        question["sources"].update(_refs(proposal, sources))
        question["why"].append(f"UNAPPROVED PROPOSAL for {proposal['subject']}: {treatment['reason']}")
        if proposal["kind"] == "classification":
            question["confirm"].extend(treatment["required_confirmation"])
            _table(question, ["Proposal subject", "Candidate code", "Wage basis", "Approval"],
                [[proposal["subject"], treatment["class_code"] or "unconfirmed", treatment["wages"], "UNAPPROVED; excluded from CSV"]])
        else:
            question["confirm"].extend(proposal["required_confirmation"])
            _table(question, ["Proposal payment", "Candidate work code", "Proposed payroll", "Proposed nonpayroll", "Approval"],
                [[proposal["subject"], proposal["work_code"] or "unconfirmed", treatment["payroll_added"],
                  treatment["nonpayroll"], "UNAPPROVED; excluded from CSV"]])
    monetary = [p["treatment"]["payroll_added"] for _, p in proposals if p["kind"] == "adjustment"]
    if monetary:
        question["why"].append(f"UNAPPROVED PROPOSAL total payroll addition: ${_sum_money(monetary)}; not in verified CSV totals.")


def _match_record(question, record, sources):
    refs = [sources[ref] for ref in set(record["source_ids"]) & question["sources"]]
    if any(ref["line_start"] == record["line_start"] and ref["line_end"] <= record["line_end"] for ref in refs):
        return True
    if not refs:
        return False
    values = record["values"]
    if values.get("employee_id") in question["employee_ids"]:
        return True
    if values.get("subcontractor") in question["payees"]:
        return True
    return question["kind"] in {"receipts", "record_review"}


def _finish_coverage(employer):
    sources = {source["id"]: source for source in employer["sources"]}
    questions = employer["questions"]
    # Remaining evidence is turned into an explicit record-review request, never
    # silently marked covered or used to assign an employee identity.
    used = set().union(*(q["sources"] for q in questions))
    for filename in sorted({ref["source"] for ref in sources.values() if ref["id"] not in used}):
        refs = {ref["id"] for ref in sources.values() if ref["source"] == filename and ref["id"] not in used}
        question = _question("record_review", f"Additional evidence in {Path(filename).name}", "OPEN / HUMAN CONFIRMATION REQUIRED")
        question["sources"] = refs
        question["confirm"].append("Confirm the listed source records, identities, dates and completeness; explain their relevance to actual duties or payment treatment.")
        question["why"].append("These cited records require explicit confirmation rather than an assumed identity or classification.")
        questions.append(question)
    remaining = [record for record in employer["records"] if not any(_match_record(q, record, sources) for q in questions)]
    for filename in sorted({record["source"] for record in remaining}):
        question = _question("record_review", f"Unmatched records in {Path(filename).name}", "OPEN / HUMAN CONFIRMATION REQUIRED")
        question["sources"] = {ref for record in remaining if record["source"] == filename for ref in record["source_ids"]}
        question["confirm"].append("Identify and explain every unmatched row in the record index, including its date and original identifiers; confirm whether it belongs to payroll personnel or a nonpayroll visitor.")
        question["why"].append("Unmatched evidence cannot establish an employee identity or zero activity by assumption.")
        questions.append(question)
    for index, question in enumerate(questions, 1):
        question["id"] = f"{employer['prefix']}-Q{index:03d}"
        question["confirm"] = list(dict.fromkeys(question["confirm"]))
        question["why"] = list(dict.fromkeys(question["why"]))
        question["covers"].update(f"source:{ref}" for ref in question["sources"])
        question["covers"].update(f"file:{sources[ref]['source']}" for ref in question["sources"])
        for record in employer["records"]:
            if _match_record(question, record, sources):
                question["covers"].add(f"record:{record['id']}")
                record["questions"].append(question["id"])


def _priorities(interview, employers, natives, files):
    messages = list(_MESSAGE.finditer(interview.text))
    acknowledgements = []
    for index, match in enumerate(messages):
        end = messages[index + 1].start() if index + 1 < len(messages) else len(interview.text)
        body = interview.text[match.end():end]
        choice = re.search(r"I have noted your choices of (.+?), along with your reasoning regarding (.+?)\.", body, re.S)
        if match.group(1) == "Nadia Brennan" and choice:
            acknowledgements.append((match, end, choice))
    if len(acknowledgements) > 1:
        raise QuestionGenerationError("Multiple priority acknowledgements require human confirmation; no ranking is inferred")
    if not acknowledgements:
        return []
    match, end, choice = acknowledgements[0]
    normalize = lambda text: " ".join(text.casefold().split())
    recorded_text = choice.group(1).strip()
    identities = {}
    for employer in employers:
        identities.setdefault(normalize(employer["name"]), []).append(employer)
    # Exact identity matching permits case/spacing variants only. A prefix
    # such as Independent cannot stand for Independent Electric. Preserve a full
    # company name containing 'and' when it matches exactly; otherwise parse the
    # acknowledgement's explicit list separators conservatively.
    recorded_names = [recorded_text] if normalize(recorded_text) in identities else re.split(r",\s*(?:and\s+)?|\s+and\s+", recorded_text)
    selected = []
    seen = set()
    for position, name in enumerate(recorded_names):
        matching = identities.get(normalize(name), [])
        if len(matching) > 1:
            raise QuestionGenerationError(f"Ambiguous recorded priority identity: {name}")
        if not matching:
            # A partial list could instead be a single compound legal name, such
            # as Independent and Sons. Do not revive Independent as an alias.
            return []
        employer = matching[0]
        if employer["directory"] in seen:
            continue
        seen.add(employer["directory"])
        native = natives[employer["directory"]]
        reasons = []
        adjustments = employer["entry"]["adjustments"]["lines"]
        subcontractors = [line for line in adjustments if line["kind"] == "subcontractor"]
        if subcontractors:
            reasons.append("Subcontractor certificate coverage and identity require confirmation: "
                f"verified additions ${_sum_money(line['payroll_added'] for line in subcontractors)}, "
                f"OPEN payment basis ${_sum_money(line['unresolved_basis'] for line in subcontractors)}. "
                + " ".join(dict.fromkeys(line["reason"] for line in subcontractors)))
        changes = [item for item in native.employee_comparisons.values() if item.status == "CHANGE"]
        if changes:
            reasons.append(f"Work-record classification changes affect {len(changes)} employees and ${_sum_money(str(item.wages) for item in changes)} of wages. "
                "The employer's application and employee-attribution questions must be confirmed against actual work records.")
            if native.roofing_days:
                reasons.append(f"{files.crew_timesheets} and {files.site_signins} support substantial field work rather than the reported clerical split; confirm each changed employee's records below.")
        reported = employer["entry"]["application"]
        if reported:
            reasons.append("Reported split: " + "; ".join(f"{row['class_code']}: {row['employees']} employees, ${row['payroll']}" for row in reported["reported"]) + ".")
        selected.append((position, {"employer": employer["employer"], "name": employer["name"],
            "reason": " ".join(reasons) or f"Recorded reason: {choice.group(2).strip()}; confirm the supporting records below.",
            "source": asdict(_reference(interview, match.start(), end, f"Nadia Brennan · {match.group(2)}"))}))
    return [item for _, item in sorted(selected, key=lambda item: item[0])]


def build_question_plan(state, native_results, guide, interview, *, files=EmployerFiles()):
    """Build grouped questions and explicit coverage from structured engine results."""
    plan = {"employers": [], "priorities": [], "review_state": state["review_state"],
            "guide": str(guide.path), "interview": str(interview.path)}
    outputs = {output["directory"]: output for output in state["outputs"]}
    for index, entry in enumerate(state["processing"]["employers"], 1):
        native = native_results[entry["directory"]]
        prefix = f"E{index:02d}"
        sources = {source["id"]: source for source in entry["sources"]}
        employer = {"employer": entry["employer"], "directory": entry["directory"], "prefix": prefix,
            "name": _title(native, files), "entry": entry, "csv": outputs[entry["directory"]],
            "sources": entry["sources"], "records": _records(entry, prefix), "questions": []}
        questions = employer["questions"]
        employer["required"] = _expected(entry, employer["records"])
        by_employee, by_adjustment = {}, {}
        for employee in entry["employee_payroll"]:
            key = employee["employee_id"]
            pending = any(part["status"] == "OPEN" for part in employee["parts"])
            question = _question("employee", f"{employee['name']} [{key}]",
                "OPEN / HUMAN APPROVAL REQUIRED" if pending else "VERIFIED CALCULATION / EMPLOYER CONFIRMATION", employee_ids=(key,))
            question["covers"].add(f"employee:{key}")
            question["covers"].update(f"part:{part['part_id']}" for part in employee["parts"])
            question["sources"].update(_refs(employee, sources))
            question["confirm"].append(f"Confirm {employee['name']} [{key}]'s actual duties, original register wages ${employee['register_wages']}, and every listed payroll part or pay week against the cited employer records. Identify any missing work, visit, ride or wage records and any incorrect identity.")
            question["why"].append("Verified base-wage allocation: " + ("; ".join(f"{code} ${amount}" for code, amount in employee["verified_wages_by_code"].items()) or "none") + f". OPEN base wages: ${employee['open_wages']}; OPEN wages are excluded from CSV totals.")
            for part in employee["parts"]:
                if part["decision"]:
                    question["why"].append(part["decision"]["reason"])
                    question["confirm"].extend(part["decision"]["required_confirmation"])
                question["confirm"].extend(part["required_confirmation"])
            comparison = native.employee_comparisons.get(key)
            if comparison:
                question["sources"].update(_native_refs(comparison.sources, sources))
                question["confirm"].append(f"Confirm the employee-level application assignment {comparison.reported_code or 'unconfirmed'} {'(inferred from counts/wages, not explicitly listed)' if comparison.reported_inferred else '(documented)'}, and the calculated result {comparison.calculated_code or 'OPEN'} for ${comparison.wages}; status {comparison.status}.")
            if key in native.site_visits:
                question["why"].append("Confirmed distinct site-visit dates: " + (", ".join(day.isoformat() for day in native.site_visits[key]) or "none recorded") + ". Unattributed rows remain unassigned; confirm completeness separately.")
                unmatched = [record for record in employer["records"] if any(
                    record["source"] == ref.source and record["line_start"] == ref.line_start for ref in native.unassigned_site_records)]
                if unmatched:
                    question["sources"].update(_native_refs(native.unassigned_site_records, sources))
                    question["confirm"].append(f"For each listed unattributed sign-in, identify whether it belongs to {employee['name']} [{key}], another employee, or a nonpayroll visitor. The original blank/unmatched identity is preserved; no visit is attributed to this employee without confirmation.")
                    _table(question, ["Unattributed source record", "Date", "Original employee ID", "Original name", "Site"],
                        [[f"{Path(record['source']).name}:{record['line_start']}", record["values"].get("date", "unknown"),
                          record["values"].get("employee_id") or "BLANK / UNATTRIBUTED", record["values"].get("name", "unknown"),
                          record["values"].get("site", "unknown")] for record in unmatched])
                    proposal = native.proposals.get(key)
                    if pending and proposal and native.governing_field and native.governing_field.class_code:
                        confirmed = {day.isoformat() for day in native.site_visits[key]}
                        possible = confirmed | {record["values"]["date"] for record in unmatched if record["values"].get("date")}
                        question["why"].append(f"UNAPPROVED alternatives from the cited office-visit rule: candidate {proposal.class_code} using only {len(confirmed)} confirmed dates; governing field code {native.governing_field.class_code} only if human confirmation establishes the additional visit evidence (up to {len(possible)} distinct dates) and the rule applies. Both the identity and resulting treatment require approval; the unmatched record is not attributed.")
            if key in native.roofing_days:
                question["why"].append(f"Recorded distinct roofing days: {len(native.roofing_days[key])}; confirm the indexed dated crew records and the rule's applicable business scope.")
            _table(question, ["Payroll part", "Week start", "Week end", "Wages", "Result", "Paragraph", "Ride dates (inside rule only)"],
                [[part["part_id"], part.get("week_start", "audit period"), part.get("week_end", "audit period"), part["wages"],
                  part["class_code"] or "OPEN", part["rationale_ref"] or "OPEN",
                  ", ".join(part.get("ride_days", [])) if part["decision"] and part["decision"]["rule"] == "courier_week" else "—"]
                 for part in employee["parts"]])
            questions.append(question)
            by_employee[key] = question

        groups = {}
        for line in entry["adjustments"]["lines"]:
            record = line["input_record"]
            identity = (line["kind"], record.get("subcontractor") if line["kind"] == "subcontractor" else record["employee_id"])
            groups.setdefault(identity, []).append(line)
        for (kind, subject), lines in groups.items():
            record = lines[0]["input_record"]
            title = subject if kind == "subcontractor" else f"{record['name']} [{subject}] — travel allowance"
            pending = any(line["status"] == "OPEN" for line in lines)
            question = _question("adjustment", title,
                "OPEN / HUMAN APPROVAL REQUIRED" if pending else "VERIFIED CALCULATION / EMPLOYER CONFIRMATION",
                employee_ids=() if kind == "subcontractor" else (subject,), payees=(subject,) if kind == "subcontractor" else ())
            question["sources"].update(_refs(lines, sources))
            question["covers"].update(f"adjustment:{line['adjustment_id']}" for line in lines)
            question["confirm"].append("Confirm every listed payment ID, amount, date or audit-period basis, actual work and original source record, and the verified payroll/nonpayroll treatment. Explain missing or conflicting documentation before any proposed treatment is approved.")
            if kind == "subcontractor":
                question["confirm"].append("Confirm the exact legal payee/certificate identity and full audit-period coverage, including certificate dates and any renewal or replacement. A differently named entity is not assumed identical; a missing certificate inventory must be confirmed complete.")
            else:
                question["confirm"].append("Confirm documented out-of-town dates and the daily payment basis, the allowance purpose, and whether it is already included in regular wages; confirm any exclusion and excess without double-counting. The auditor must approve any zero-day or other OPEN treatment.")
            for line in lines:
                question["why"].append(line["reason"])
                question["confirm"].extend(line["required_confirmation"])
                by_adjustment[line["adjustment_id"]] = question
            question["why"].append(f"Verified payroll addition ${_sum_money(line['payroll_added'] for line in lines)}; verified nonpayroll ${_sum_money(line['nonpayroll'] for line in lines)}; OPEN payment basis ${_sum_money(line['unresolved_basis'] for line in lines)}. OPEN basis is not itself an assigned payroll amount.")
            _table(question, ["Payment / allowance ID", "Date / period", "Original amount", "Days", "Verified payroll", "Nonpayroll", "OPEN basis", "Code", "Status"],
                [[line["adjustment_id"], line["input_record"].get("payment_date") or _period_text(line["period"]),
                  line["input_record"]["amount"], line["input_record"].get("travel_days", "—"), line["payroll_added"], line["nonpayroll"],
                  line["unresolved_basis"], line["class_code"] or "OPEN", line["status"]] for line in lines])
            certificates = {json.dumps(certificate, sort_keys=True): certificate for line in lines for certificate in line["certificates"]}
            if certificates:
                _table(question, ["Certificate entity", "Certificate number", "Coverage from", "Coverage through"],
                    [[c["subcontractor"], c["certificate_no"], c["coverage_from"], c["coverage_to"]] for c in certificates.values()])
            questions.append(question)

        application = _question("application", "Application split, employee attribution and payroll reconciliation")
        application["sources"].update(_refs(entry["application"], sources))
        application["covers"].update(f"control:{name}" for name, check in entry["reconciliation"].items() if check is not None)
        application["covers"].update(f"csv:{row['class_code']}" for row in employer["csv"]["rows"])
        application["confirm"].append("Confirm the reported class payroll and employee assignments, the listed corrections and their supporting records, and that the original wages/payments are complete. Approve application corrections only after the listed OPEN findings and conditional proposals are resolved by the auditor.")
        application["why"].append("Reconciliation verifies arithmetic, not employer confirmation or approval. Verified CSVs exclude OPEN wages and every unapproved proposal.")
        reported = entry["application"]
        if reported:
            application["why"].append(f"Application comparison definitive for current classifications: {reported['definitive']}; this is not audit approval.")
            _table(application, ["Code", "Reported payroll", "Verified CSV payroll", "Difference (verified minus reported)"],
                [[code, next((row["payroll"] for row in reported["reported"] if row["class_code"] == code), "0.00"),
                  entry["verified_by_code"].get(code, "0.00"), reported["verified_differences"].get(code, "0.00")]
                 for code in sorted(reported["verified_differences"])])
        _table(application, ["Control", "Reconciled", "Original basis", "Unresolved amount"],
            [[name, check["reconciled"], check.get("register_total", check.get("basis_total", check.get("employee_register_total", "see review state"))),
              check.get("unresolved_total", check.get("unresolved_basis", check.get("employee_open", "see review state")))]
             for name, check in entry["reconciliation"].items() if check is not None])
        questions.append(application)

        context = _question("context", "Business, actual-duty observations and audit-period completeness")
        context["confirm"].append(f"Confirm the business activities and field observations for {_period_text(entry['audit_period'])}, every listed employee's actual duties and the completeness of the records used. Identify work or payments omitted from the supplied files.")
        context["why"].append("Classification depends on actual work and complete period evidence; job titles and the submitted application alone do not establish a code.")
        for ref in sources.values():
            if Path(ref["source"]).name in {Path(files.business).name, Path(files.notes).name}:
                context["sources"].add(ref["id"])
        questions.append(context)

        policy = _question("policy", "Company-rule applicability — auditor confirmation", "AUDITOR APPROVAL / EMPLOYER FACT CONFIRMATION")
        policy["confirm"].append("Auditor: confirm that the current guide paragraphs and cited interview practices apply to the evidenced duties and period. Employer: confirm the supporting facts and records; policy interpretation remains with the auditor. Keep unsupported or conflicting treatments OPEN.")
        policy["why"].append("Contractor-specific practices cannot be extended to unrelated industries; proposals are not verified rules or allocations.")
        for ref in sources.values():
            if Path(ref["source"]).resolve() in {guide.path.resolve(), interview.path.resolve()}:
                policy["sources"].add(ref["id"])
        policy["covers"].update(f"file:{manifest['path']}" for manifest in entry["source_manifest"] if Path(manifest["path"]).resolve() == guide.path.resolve())
        questions.append(policy)
        for object_name in ("owner", "governing_field", "receipts"):
            value = entry[object_name]
            if value is None:
                continue
            if object_name == "owner":
                question = next((q for key, q in by_employee.items() if next(e for e in entry["employee_payroll"] if e["employee_id"] == key)["name"] == value["name"]), None)
                if question is None:
                    question = _question("owner", f"Owner election — {value['name'] or 'unidentified owner'}")
                    questions.append(question)
                question["confirm"].append(f"Confirm {value['name']}'s election status and period, actual duties and register presence; supply the filed election if exclusion is claimed. Assessment {value['status']}; removed register wages ${value['removed_wages']}.")
                question["why"].append(value["reason"])
            elif object_name == "governing_field":
                question = context
                question["confirm"].append(f"Confirm the evidenced governing field code {value['class_code'] or 'OPEN'} and its payroll basis; it must not be selected by title or assumed industry similarity.")
                question["why"].append(value["reason"])
            else:
                question = _question("receipts", "Receipt audit-period coverage and mixed-duty catering evidence", "OPEN / HUMAN CONFIRMATION REQUIRED" if not value["coverage_confirmed"] else "VERIFIED CALCULATION / EMPLOYER CONFIRMATION")
                question["confirm"].append(f"Confirm every listed monthly receipt row and provide evidence for the exact period ({_period_text(entry['audit_period'])}), including partial months. Confirm mixed duties and timesheet availability before applying the interview's catering practice.")
                percentage = format(Decimal(value["percentage"]), ".2f") if value["percentage"] is not None else "UNAVAILABLE"
                question["why"].append(f"Recorded dine-in ${value['dine_in']}, off-site ${value['offsite']}, total ${value['total']}; diagnostic percentage {percentage}% (rounded for display only); complete period confirmed: {value['coverage_confirmed']}. Exact values remain in review state; an unconfirmed period does not verify a catering allocation.")
                questions.append(question)
            question["covers"].add(object_name)
            question["sources"].update(_refs(value, sources))

        generic = {}
        for finding_index, finding in enumerate(entry["questions"]):
            question = by_adjustment.get(finding["subject"])
            if question is None:
                question = next((q for key, q in by_employee.items() if finding["subject"] == key or f"[{key}]" in finding["subject"]), None)
            if question is None and finding["subject"].startswith("Application"):
                question = application
            if question is None and finding["subject"] == "Receipt audit-period coverage":
                question = next((q for q in questions if q["kind"] == "receipts"), None)
            if question is None:
                signature = (finding["subject"], finding["reason"], finding["required_confirmation"])
                if signature not in generic:
                    generic[signature] = _question("finding", finding["subject"], "OPEN / HUMAN CONFIRMATION REQUIRED")
                    questions.append(generic[signature])
                question = generic[signature]
            _add_finding(question, finding, finding_index, sources)
            if finding["subject"] == "Unattributed site sign-ins":
                records = [record for record in employer["records"] if set(record["source_ids"]) & set(finding["sources"])]
                _table(question, ["Original source record", "Date", "Original employee ID", "Original name", "Site"],
                    [[f"{Path(record['source']).name}:{record['line_start']}", record["values"].get("date", "unknown"),
                      record["values"].get("employee_id") or "BLANK / UNATTRIBUTED", record["values"].get("name", "unknown"),
                      record["values"].get("site", "unknown")] for record in records])
        proposal_groups = {}
        for proposal_index, proposal in enumerate(entry["proposals"]):
            question = by_employee.get(proposal["subject"]) if proposal["kind"] == "classification" else by_adjustment.get(proposal["subject"])
            if question is None:
                raise QuestionGenerationError(f"Proposal has no matching employee/payment question: {proposal['subject']}")
            proposal_groups.setdefault(id(question), (question, []))[1].append((proposal_index, proposal))
        for question, proposals in proposal_groups.values():
            _proposals(question, proposals, sources)
        _finish_coverage(employer)
        plan["employers"].append(employer)
    plan["priorities"] = _priorities(interview, plan["employers"], native_results, files)
    gaps = coverage_gaps(plan)
    if gaps:
        raise QuestionGenerationError(f"Uncovered evidence: {gaps}")
    return plan


def coverage_gaps(plan):
    gaps = {}
    for employer in plan["employers"]:
        covered = set().union(*(q["covers"] for q in employer["questions"]))
        missing = set(employer["required"]) - covered
        if missing:
            gaps[employer["employer"]] = sorted(missing)
    return gaps


def _md(value):
    text = "UNAVAILABLE" if value is None else str(value)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").replace("\n", " ")


def _markdown_table(columns, rows):
    return ["| " + " | ".join(_md(value) for value in columns) + " |",
            "| " + " | ".join("---" for _ in columns) + " |",
            *("| " + " | ".join(_md(value) for value in row) + " |" for row in rows), ""]


def render_questions(plan):
    if coverage_gaps(plan):
        raise QuestionGenerationError("Cannot render questions with uncovered evidence")
    lines = ["# Employer audit confirmation questions", "",
        "All questions are unanswered. VERIFIED CALCULATION means the existing engine supports the calculation; employer confirmation is still requested. OPEN findings and UNAPPROVED PROPOSALS remain outside verified allocations. The auditor approves policy applicability and proposed treatment; employers confirm actual facts and records. Reconciled amounts alone are not approval.", "",
        "## Recorded priority calls", "",
        "The interview records a first-call group, not a general ranking rule or an order between its members.", ""]
    if not plan["priorities"]:
        lines.extend(["No source-bound first-call choices could be fully matched to the selected employers; ask the auditor to confirm names, scope and priorities.", ""])
    for priority in plan["priorities"]:
        source = priority["source"]
        lines.extend([f"- **{_md(priority['name'])}**: {_md(priority['reason'])} Source: {_md(source['source'])}, {_md(source['locator'])}, lines {source['line_start']}-{source['line_end']}; SHA-256 {source['sha256']}.", ""])
    lines.extend(["Review-state input: " + _md(plan["review_state"]), "",
        "Evidence identifiers are local to each employer. The record index gives original CSV fields, dates, employee/payment identifiers and question links. Rule citations retain their original paragraph/interview locators. A document-level question does not replace individual payroll/payment confirmations.", ""])
    lines.extend(f"- [{_md(employer['name'])}](#{employer['prefix'].lower()})" for employer in plan["employers"])
    lines.append("")
    for employer in plan["employers"]:
        entry = employer["entry"]
        lines.extend([f"<a id=\"{employer['prefix'].lower()}\"></a>", f"## {_md(employer['name'])} ({_md(employer['employer'])})", "",
            f"Verified CSV payroll: ${employer['csv']['verified_total']}. OPEN wages: ${entry['open_wages']}. OPEN adjustment basis: {('$' + entry['open_adjustment_basis']) if entry['open_adjustment_basis'] is not None else 'NOT EVALUATED'}. Proposed amounts are excluded from these verified CSV totals.", "",
            f"CSV: {_md(employer['csv']['path'])}; SHA-256 {employer['csv']['sha256']}. Questions: {len(employer['questions'])}. Uncovered obligations: 0.", ""])
        for question in employer["questions"]:
            lines.extend([f"<a id=\"{question['id'].lower()}\"></a>",
                f"### {question['id']} — {_md(question['subject'])}", "", f"**{question['status']}**", ""])
            for prompt in question["confirm"]:
                lines.extend([f"- **Confirm:** {_md(prompt)}", ""])
            for reason in question["why"]:
                lines.extend([f"**Why it matters:** {_md(reason)}", ""])
            refs = [ref for ref in employer["sources"] if ref["id"] in question["sources"]]
            filenames = sorted({Path(ref["source"]).name for ref in refs})
            lines.extend(["**Source documents:** " + "; ".join(_md(name) for name in filenames) + ". Exact locators and row identities are indexed below under this question ID.", ""])
            for table in question["tables"]:
                lines.extend(_markdown_table(table["columns"], table["rows"]))
        lines.extend(["<details>", f"<summary>Evidence and record coverage index — {len(employer['sources'])} citations, {len(employer['records'])} CSV records</summary>", "",
            "Each cited source and each relied-upon CSV data row has at least one confirmation question. Shared source rows may support several distinct questions.", ""])
        lines.extend(_markdown_table(["Source ID", "Document", "Original locator", "Lines", "Question IDs"],
            [[ref["id"], Path(ref["source"]).name, ref["locator"], f"{ref['line_start']}-{ref['line_end']}",
              ", ".join(f"[{q['id']}](#{q['id'].lower()})" for q in employer["questions"] if f"source:{ref['id']}" in q["covers"])] for ref in employer["sources"]]))
        lines.extend(_markdown_table(["Record ID", "Document / lines", "Original record fields", "Source IDs", "Question IDs"],
            [[record["id"], f"{Path(record['source']).name}:{record['line_start']}-{record['line_end']}",
              "; ".join(f"{key}={value}" for key, value in record["values"].items()), ", ".join(record["source_ids"]), ", ".join(f"[{key}](#{key.lower()})" for key in record["questions"])]
             for record in employer["records"]]))
        lines.extend(_markdown_table(["Original source location", "SHA-256"],
            [[manifest["path"], manifest["sha256"]] for manifest in entry["source_manifest"]]))
        lines.extend(["</details>", ""])
    return "\n".join(lines).rstrip("\n") + "\n"


def generate_questions(review_state, *, codes_dir, output, files=EmployerFiles()):
    """Validate current inputs, render questions, and preserve all upstream files."""
    try:
        review_state, codes_dir = (Path(path).expanduser().resolve() for path in (review_state, codes_dir))
        output_argument = Path(output).expanduser().absolute()
        if output_argument.is_symlink():
            raise QuestionGenerationError("Question output must not be a symbolic-link file")
        output = output_argument.resolve()
        review_bytes = review_state.read_bytes()
        state = json.loads(review_bytes)
        if state["schema_version"] != 1 or state["allocation_scope"] != "VERIFIED_ONLY" or state["status"] == "ERROR" or state["errors"]:
            raise QuestionGenerationError("A complete, error-free verified-only CSV review state is required")
        processing = state["processing"]
        selection = {"employer": processing["discovery"]["root"]} if processing["mode"] == "single" else {"all_employers": processing["discovery"]["root"]}
        fresh = run_preview(processing["guide"], processing["interview"], files=files, **selection)
        if fresh != processing:
            raise QuestionGenerationError("Current source/engine results differ from review state; regenerate CSVs/state before questions")
        guide, interview = read_markdown(processing["guide"]), read_markdown(processing["interview"])
        outputs = {item["directory"]: item for item in state["outputs"]}
        if len(outputs) != len(state["outputs"]) or set(outputs) != {entry["directory"] for entry in processing["employers"]}:
            raise QuestionGenerationError("Every selected employer must have exactly one validated CSV")
        expected_files = {Path(item["path"]).name for item in state["outputs"]}
        if len(expected_files) != len(state["outputs"]) or {path.name for path in codes_dir.glob("*.csv")} != expected_files:
            raise QuestionGenerationError("Missing or unexpected employer CSV files")
        cache, natives, protected = {}, {}, {review_state: hashlib.sha256(review_bytes).hexdigest()}
        source_roots = [Path(processing["discovery"]["root"]).resolve()]
        for entry in processing["employers"]:
            source_roots.append(Path(entry["directory"]).resolve())
            _verify_sources(processing, entry, cache)
            native = process_employer(processing["guide"], entry["directory"], processing["interview"], files=files)
            if employer_preview(Path(entry["directory"]), native) != entry:
                raise QuestionGenerationError("Sources changed during native question processing")
            natives[entry["directory"]] = native
            item = outputs[entry["directory"]]
            csv_path = (codes_dir / Path(item["path"]).name).resolve()
            payload = csv_path.read_bytes()
            if hashlib.sha256(payload).hexdigest() != item["sha256"]:
                raise QuestionGenerationError(f"CSV hash mismatch: {csv_path}")
            validate_csv(payload.decode("utf-8"), entry, guide)
            if item["rows"] != list(csv.DictReader(io.StringIO(payload.decode("utf-8"), newline=""))):
                raise QuestionGenerationError("Review-state CSV rows differ from supplied CSV")
            if _units(item["verified_total"], "CSV total") != sum(_units(row["payroll_allocated"], "CSV row") for row in item["rows"]):
                raise QuestionGenerationError("Review-state CSV total differs from verified rows")
            protected[csv_path] = item["sha256"]
        protected.update({path.resolve(): digest for path, (digest, _) in cache.items()})
        if output in protected or any(output.is_relative_to(root) for root in source_roots):
            raise QuestionGenerationError("Question output must be separate from authoritative inputs, CSVs and review state")
        plan = build_question_plan(state, natives, guide, interview, files=files)
        plan["review_state"] = str(review_state)
        for employer in plan["employers"]:
            employer["csv"] = {**employer["csv"], "path": str((codes_dir / Path(employer["csv"]["path"]).name).resolve())}
        text = render_questions(plan)
        for path, digest in protected.items():
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise QuestionGenerationError(f"Input changed before question publication: {path}")
        payload = text.encode("utf-8")
        _preflight(output, payload)
        _publish(output, payload)
        if output.read_bytes() != payload:
            raise QuestionGenerationError("Published questions failed byte verification")
        return {"path": str(output), "sha256": hashlib.sha256(payload).hexdigest(),
            "counts": {e["employer"]: len(e["questions"]) for e in plan["employers"]},
            "source_counts": {e["employer"]: len(e["sources"]) for e in plan["employers"]},
            "record_counts": {e["employer"]: len(e["records"]) for e in plan["employers"]},
            "uncovered": coverage_gaps(plan), "priorities": plan["priorities"]}
    except QuestionGenerationError:
        raise
    except (OSError, ValueError, KeyError, TypeError, StopIteration) as exc:
        raise QuestionGenerationError(f"Cannot generate supported audit questions: {exc}") from exc


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-state", required=True, type=Path)
    parser.add_argument("--codes-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--file", action="append", default=[], metavar="FIELD=RELATIVE_PATH")
    args = parser.parse_args(argv)
    overrides = {}
    allowed = {field.name for field in fields(EmployerFiles)}
    for argument in args.file:
        name, separator, value = argument.partition("=")
        if not separator or name not in allowed or name in overrides or not value or Path(value).is_absolute() or ".." in Path(value).parts:
            parser.error(f"Invalid or duplicate EmployerFiles override: {argument!r}")
        overrides[name] = str(Path(value))
    try:
        report = generate_questions(args.review_state, codes_dir=args.codes_dir, output=args.output,
                                    files=replace(EmployerFiles(), **overrides))
    except QuestionGenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Questions: {report['path']} SHA-256 {report['sha256']}")
    for employer, count in report["counts"].items():
        print(f"{employer}: {count} questions; {report['source_counts'][employer]} source citations; {report['record_counts'][employer]} CSV records")
    print(f"Uncovered: {report['uncovered']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
