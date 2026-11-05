"""Evidence-bound roofing/siding and contractor-office orchestration."""

from dataclasses import dataclass, replace
from collections import Counter
from datetime import date
from decimal import Decimal, InvalidOperation
import itertools
import re

from employer_processing import (
    EmployeeClassComparison, GoverningFieldEvidence, OpenItem,
    _adjustment_evidence, _pending, _source,
)
from legal_office_processing import _row_references
from payroll_allocation import _cents, _money
from rule_evaluator import RuleFacts


@dataclass(frozen=True)
class ContractorEvaluation:
    decisions: dict
    roofing_days: dict
    site_visits: dict
    governing_field: GoverningFieldEvidence
    unassigned_site_records: tuple
    open_items: tuple[OpenItem, ...]


_GUIDE_WORDING = {
    "CG-02": "**CG-02. Assigning codes.** An employer is assigned the class code that describes its principal business. An employee whose work is described by another code in this guide is reported under that code. An employer may carry several codes.",
    "CG-04": "**CG-04. C-110 Clerical office employees.** Employees whose duties are confined to an office: correspondence, bookkeeping, dispatching by telephone or radio, drafting and estimating at a desk, and professional staff who work in the office.",
    "CG-07": "**CG-07. Division of payroll.** When an employee performs work in more than one classification and the employer keeps records of the time spent in each, the employee's payroll may be divided between the codes.",
    "CG-11": "**CG-11. R-310 Roofing.** Installation, repair and removal of roofs and roof coverings on any building, including work on scaffolds and ladders at the roof line.",
    "CG-12": "**CG-12. R-320 Siding and gutters.** Installation and repair of exterior siding, gutters, downspouts and exterior trim below the roof line. Roofing work is described by CG-11.",
}


def _guide_valid(evaluator, rule, identifiers):
    refs = [ref for ref in evaluator.rule_sources[rule] if ref.locator in identifiers]
    return all(sum(ref.locator == key for ref in refs) == 1 for key in identifiers) and all(
        " ".join(ref.excerpt.split()) in (_GUIDE_WORDING[ref.locator], _GUIDE_WORDING[ref.locator] + " ## Class codes") for ref in refs)


def _day(text, period):
    day = date.fromisoformat(text)
    if day.isoformat() != text or period is None or not period.start <= day <= period.end:
        raise ValueError("date is outside the audit period or not canonical")
    return day


def evaluate_contractor(inputs, business, notes, crew, log, payroll, register, period, evaluator, files):
    employees = {row.employee_id: row for row in register}
    context = tuple(_source(doc, "business description" if doc is business else "auditor field notes") for doc in (business, notes) if doc)
    business_text = " ".join(business.text.lower().split())
    note_text = " ".join(" ".join(line for line in notes.text.lower().splitlines() if not line.lstrip().startswith("#")).split()) if notes else ""
    observed_estimator = bool(re.search(r"(?:^|[.!?]\s+|\band )the estimator was measuring a house for a quote\.", note_text))
    observed_bookkeeper = bool(re.search(r"(?:^|[.!?]\s+)the bookkeeper works in the office\.", note_text))
    mapped = {files.business, files.notes, files.payroll, files.application, files.crew_timesheets, files.site_signins}
    extra = [doc for doc in inputs.records if str(doc.path.relative_to(inputs.records_root)) not in mapped and not _adjustment_evidence(doc)]
    global_errors = []
    if extra or set(payroll.columns) != {"employee_id", "name", "position", "wages_paid"}:
        global_errors.append("Unmapped source files or payroll columns require duty-evidence review.")
        context += tuple(_source(doc, "unmapped evidence") for doc in extra)
    if notes is None or period is None:
        global_errors.append("Confirm field observations and the exact audit period.")
    if re.search(r"\b(?:actual duties|misleading|exclusively|contrary|instead)\b", business_text + " " + note_text):
        global_errors.append("Exceptional or conflicting duty prose is outside this adapter's supported observations; obtain duty review.")
    context_text = business_text + " " + note_text
    if re.search(r"\b(?:timesheets?|sign[- ]in|crew time|records?|pages)\b[^.!?]{0,150}\b(?:missing|incomplete|unavailable|lost|unconfirmed|not complete)\b|\b(?:missing|incomplete|unavailable|lost|unconfirmed)\b[^.!?]{0,100}\b(?:timesheets?|sign[- ]in|crew time|records?|pages)\b", context_text):
        global_errors.append("Explicit missing or incomplete audit-period records prevent a complete-evidence assertion; obtain the missing pages and confirmation.")
    if re.search(r"\b(?:bookkeeper|estimator)\b[^.!?]{0,80}\b(?:install\w*|repair\w*|roof\w*|field work)\b", context_text):
        global_errors.append("Physical-work statements conflict with the supported office-role observations; confirm employee duties and rule scope.")
    role_counts = Counter(str(row.raw_record.values.get("position", "")).lower() for row in register)
    dual = bool(re.search(r"\b(?:replaces roofs|performs roofing|installs roofing)\b", business_text) and re.search(r"\binstalls siding\b", business_text))
    if re.search(r"\b(?:no|not|never|unconfirmed|unknown)\b[^.!?]{0,60}\b(?:roof\w*|siding|field work|crew time)\b", business_text + " " + note_text):
        dual = False
    field_rows = {key: [] for key in employees}
    roof_dates = {key: set() for key in employees}
    field_errors = {key: [] for key in employees}
    field_global = []
    field_global_refs = []
    crew_valid = crew is not None and set(crew.columns) == {"date", "employee_id", "name", "job_id", "work_type", "hours"}
    work_types = set()
    if not crew_valid:
        field_global.append("Crew timesheets are missing or have an unsupported schema; missing records cannot establish zero roofing days.")
    else:
        for row, ref in _row_references(crew):
            key = row.values["employee_id"]
            if key not in employees or row.values["name"] != employees[key].name:
                field_global.append("A crew timesheet identity conflicts with the register; confirm identity without assuming an alias.")
                global_errors.append("Conflicting crew identities may implicate office staff; resolve the actual employee identity before classification.")
                field_global_refs.append(ref)
                if key in employees:
                    field_rows[key].append(ref)
                continue
            field_rows[key].append(ref)
            try:
                day = _day(row.values["date"], period)
                hours = Decimal(row.values["hours"])
                kind = row.values["work_type"]
                if not hours.is_finite() or not Decimal(0) < hours <= Decimal(24) or not row.values["job_id"].strip() or kind not in {"roofing", "siding", "gutters"}:
                    raise ValueError("unsupported work or invalid hours/job evidence")
                work_types.add(kind)
                if kind == "roofing":
                    roof_dates[key].add(day)
            except (ValueError, TypeError, InvalidOperation):
                field_errors[key].append(f"{ref.locator}: invalid date, work type, hours or job evidence; obtain corrected actual-duty records.")
    dual = dual and {"roofing", "siding"}.issubset(work_types)
    field_ids = tuple(key for key in employees if field_rows[key])
    decisions = {}
    issues = []
    field_guide = _guide_valid(evaluator, "roofing_siding", ("CG-02", "CG-07", "CG-11", "CG-12"))
    for key in field_ids:
        errors = global_errors + field_global + field_errors[key]
        role = str(employees[key].raw_record.values.get("position", "")).lower()
        if (role == "estimator" and observed_estimator) or (role == "bookkeeper" and observed_bookkeeper):
            errors = errors + ["Physical-work timesheets conflict with the observed office role; confirm actual duties and rule scope."]
        evidence = tuple(dict.fromkeys((employees[key].source, *context, *field_rows[key], *field_global_refs)))
        facts = RuleFacts(key, "contractor", "field", period.start if period else None, period.end if period else None,
                          complete=not errors, evidence_sources=evidence, days=tuple(sorted(roof_dates[key])), roofing_and_siding=dual)
        decision = evaluator.evaluate("roofing_siding", facts)
        if errors or not field_guide:
            decision = _pending(" ".join(errors) if errors else "The guide's complete roofing/siding definitions changed; obtain source review.", evidence, evaluator.rule_sources["roofing_siding"])
        decisions[key] = decision
    office_roles = {}
    for key, employee in employees.items():
        if key in field_ids:
            continue
        role = str(employee.raw_record.values.get("position", "")).lower()
        if role == "estimator" and observed_estimator and role_counts[role] == 1:
            office_roles[key] = role
        elif role == "bookkeeper" and observed_bookkeeper and role_counts[role] == 1:
            office_roles[key] = role
    unknown_ids = set(employees) - set(field_ids) - set(office_roles)
    totals = {}
    for key in field_ids:
        if decisions[key].status == "CLASSIFIED":
            code = decisions[key].class_code
            totals[code] = totals.get(code, 0) + _cents(employees[key].wages, key)
    field_complete = bool(field_ids) and not unknown_ids and not field_global and not global_errors and all(decisions[key].status == "CLASSIFIED" for key in field_ids)
    leaders = [code for code, amount in totals.items() if amount == max(totals.values()) and amount > 0] if totals else []
    governing_code = leaders[0] if field_complete and len(leaders) == 1 else None
    governing_refs = tuple(dict.fromkeys(ref for key in field_ids for ref in decisions[key].evidence_sources))
    governing_rules = tuple(dict.fromkeys(ref for key in field_ids for ref in decisions[key].rule_sources))
    governing = GoverningFieldEvidence(governing_code, {code: _money(value) for code, value in sorted(totals.items())}, field_ids,
        "Unique largest verified field-worker payroll; office wages are excluded from this first stage to avoid circular classification." if governing_code else "The governing field code is OPEN: field membership/payroll is incomplete, unresolved or tied.", governing_rules, governing_refs + context)
    visits = {key: set() for key in office_roles}
    visit_refs = {key: [] for key in employees}
    visit_errors = {key: [] for key in employees}
    log_errors = []
    unassigned = []
    unassigned_days = set()
    log_valid = log is not None and set(log.columns) == {"date", "employee_id", "name", "site", "signed_in_at"}
    if not log_valid:
        log_errors.append("Site sign-ins are missing or have an unsupported schema; missing evidence cannot establish zero visits.")
    else:
        for row, ref in _row_references(log):
            key = row.values["employee_id"]
            if key not in employees:
                unassigned.append(ref)
                try:
                    unassigned_days.add(_day(row.values["date"], period))
                except (ValueError, TypeError):
                    log_errors.append("An unattributed site record has an invalid date; office visit counts cannot be bounded.")
                continue
            visit_refs[key].append(ref)
            if row.values["name"] != employees[key].name:
                log_errors.append("A sign-in ID/name conflict makes office visit identities unreliable; obtain confirmation.")
            try:
                day = _day(row.values["date"], period)
                if not row.values["site"].strip() or not row.values["signed_in_at"].strip():
                    raise ValueError
                if key in visits:
                    visits[key].add(day)
            except (ValueError, TypeError):
                visit_errors[key].append("A sign-in record has invalid or outside-period date/site evidence.")
    if unassigned:
        issues.append(OpenItem("Unattributed site sign-ins", "Site rows lack a matching payroll identity. No employee identity or exact employee day count is inferred; their dates bound possible additional office visits.", "Confirm whether the unmatched entries are nonpayroll visitors and correct any missing employee identities.", tuple(unassigned)))
    office_guide = _guide_valid(evaluator, "contractor_office_visits", ("CG-02", "CG-04"))
    for key in office_roles:
        errors = global_errors + log_errors + visit_errors[key]
        evidence = (employees[key].source, *context, *visit_refs[key], *unassigned, *field_global_refs, *governing.evidence_sources)
        facts = RuleFacts(key, "contractor", "office", period.start if period else None, period.end if period else None,
                          complete=not errors, evidence_sources=tuple(dict.fromkeys(evidence)), days=tuple(sorted(visits[key])),
                          governing_field_code=governing_code, governing_code_confirmed=governing_code is not None)
        lower = evaluator.evaluate("contractor_office_visits", facts)
        upper = evaluator.evaluate("contractor_office_visits", replace(facts, days=tuple(sorted(visits[key] | unassigned_days))))
        if errors or not office_guide:
            decision = _pending(" ".join(errors) if errors else "The guide's complete contractor-office definitions changed; obtain source review.", facts.evidence_sources, evaluator.rule_sources["contractor_office_visits"])
        elif lower.status == upper.status == "CLASSIFIED" and lower.class_code == upper.class_code:
            decision = replace(lower, reason=f"Between {len(visits[key])} confirmed and {len(visits[key] | unassigned_days)} possible site days; the existing contractor rule returns {lower.class_code} at both bounds. " + lower.reason,
                               rule_sources=tuple(dict.fromkeys((*lower.rule_sources, *governing.rule_sources))))
        else:
            decision = _pending("Office visit bounds or the governing field code do not establish one verified classification. " + lower.reason + " " + upper.reason, facts.evidence_sources, tuple(dict.fromkeys((*lower.rule_sources, *upper.rule_sources))))
        decisions[key] = decision
    for key in unknown_ids:
        decisions[key] = _pending("Actual-duty records do not establish field or office membership; supply this employee's work records rather than assuming zero roofing days or classifying by title.", (employees[key].source, *context), evaluator.rule_sources["roofing_siding"])
    for key, decision in decisions.items():
        if decision.status == "OPEN":
            issues.append(OpenItem(f"{employees[key].name} [{key}]", decision.reason, "; ".join(decision.required_confirmation), decision.evidence_sources + decision.rule_sources))
    return ContractorEvaluation(decisions, {key: tuple(sorted(roof_dates[key])) for key in field_ids},
        {key: tuple(sorted(days)) for key, days in visits.items()} if log_valid else {}, governing, tuple(unassigned), tuple(issues))


def compare_employee_application(result, *, search_limit=100_000):
    """Attribute aggregate application groups only when a complete mapping is unique."""
    register = result.register
    assigned = {}
    used = set()
    scanned = 0
    valid = result.application is not None
    if valid:
        for group in result.application.reported:
            matches = []
            if not 0 <= group.employees <= len(register):
                valid = False
                break
            for subset in itertools.combinations(register, group.employees):
                scanned += 1
                if scanned > search_limit:
                    valid = False
                    break
                if sum(_cents(row.wages, row.employee_id) for row in subset) == _cents(group.payroll, group.class_code):
                    matches.append(subset)
                    if len(matches) > 1:
                        break
            if len(matches) != 1 or not valid:
                valid = False
                break
            keys = {row.employee_id for row in matches[0]}
            if keys & used:
                valid = False
                break
            used.update(keys)
            assigned.update((key, group.class_code) for key in keys)
        valid = valid and used == {row.employee_id for row in register}
    if not valid:
        assigned = {}
    source_refs = tuple(group.source for group in result.application.reported) if result.application else ()
    comparisons = {}
    for employee in register:
        reported = assigned.get(employee.employee_id)
        calculated = result.decisions[employee.employee_id].class_code
        status = "OPEN" if reported is None or calculated is None else "UNCHANGED" if reported == calculated else "CHANGE"
        comparisons[employee.employee_id] = EmployeeClassComparison(employee.employee_id, employee.wages, reported, calculated, status, bool(reported),
            "Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required." if valid else "Aggregate application evidence does not uniquely identify employee assignments within the bounded search; no title-based attribution is made.", (employee.source, *source_refs))
    issue = OpenItem("Application employee attribution", "Employee assignments are not explicitly listed on the application. " + ("A unique exact count/wage partition supports the inferred comparison." if valid else "No complete unique partition was established."),
                     "Confirm the employer's employee-level reported codes; classification decisions remain based on work records.", source_refs)
    return comparisons, (issue,)
