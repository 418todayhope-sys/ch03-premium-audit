"""Electrical duties and travel evidence, bound to freshly read source records."""

from collections import defaultdict
from dataclasses import dataclass, replace
from decimal import Decimal
import re

from contractor_processing import _day
from employer_processing import ClassificationProposal, OpenItem, OwnerAssessment, _pending, _source
from homebuilding_processing import _paragraphs, _WORDING as EXISTING_WORDING
from legal_office_processing import _row_references
from payroll_allocation import _cents, _money
from payroll_adjustments import AdjustmentError, AdjustmentResult, PayrollAdjuster, TravelAllowance, TravelCase, summarize_adjustments
from rule_evaluator import Decision


@dataclass(frozen=True)
class TravelPayrollReconciliation:
    register_total: Decimal
    wage_allocated: Decimal
    wage_open: Decimal
    allowance_total: Decimal
    allowance_added: Decimal
    allowance_excluded: Decimal
    allowance_open: Decimal
    known_payroll: Decimal
    classified_payroll: Decimal
    difference: Decimal
    cash_total: Decimal | None
    cash_difference: Decimal | None
    wage_reconciled: bool
    allowance_reconciled: bool

    @property
    def reconciled(self):
        return self.wage_reconciled and self.allowance_reconciled and self.difference == 0 and self.cash_difference in (None, 0)


@dataclass(frozen=True)
class ElectricalEvaluation:
    decisions: dict
    proposals: dict
    owner: OwnerAssessment
    adjustments: AdjustmentResult | None
    adapted_sources: tuple
    site_visits: dict
    unassigned_site_records: tuple
    separate_from_base: bool | None
    open_items: tuple


_WORDING = {**EXISTING_WORDING,
    "CG-21": "**CG-21. E-510 Electrical wiring.** Installation and repair of electrical wiring and fixtures inside buildings, including service connections."}
_BASE_COLUMNS = {"employee_id", "name", "position", "wages_paid"}
_ALLOWANCE_COLUMNS = {"travel_days", "travel_allowance_paid"}


def _text(document):
    return " ".join(" ".join(line for line in document.text.splitlines() if not line.lstrip().startswith("#")).split()) if document else ""


def _refs(paragraphs, identifiers):
    refs = tuple(ref for key in identifiers for ref in paragraphs.get(key, ()))
    valid = all(len(paragraphs.get(key, ())) == 1 for key in identifiers)
    valid = valid and all(" ".join(ref.excerpt.split()) in (_WORDING[ref.locator], _WORDING[ref.locator] + " ## Class codes") for ref in refs)
    return refs, valid


def _direct(code, paragraphs, evaluator, evidence, *, owner=False):
    paragraph = {"E-510": "CG-21", "C-110": "CG-04"}[code]
    refs, valid = _refs(paragraphs, ("CG-02", paragraph, *(("CG-05",) if owner else ())))
    if not valid or code in evaluator.code_errors:
        return _pending("The current complete guide definitions are missing, changed or ambiguous; obtain auditor review.", evidence, refs)
    return Decision("electrical_actual_duties", "CLASSIFIED", code, paragraph,
        "Documented wiring business and corroborated actual duties support electrical field payroll under CG-21." if code == "E-510" else
        "Named field observations establish office-only duties, corroborated by the examined sign-ins, under CG-04.", (), refs, tuple(evidence),
        ("electrical employer", "corroborated actual duties", "included owner evidence under CG-05" if owner else "documented employee work"), "whole_audit_period")


def _incomplete(text, nouns):
    issues = r"(?:missing|incomplete|unavailable|lost|omit\w*|not recorded|unrecorded|not complete|unconfirmed|estimated|approximate)"
    return bool(re.search(r"\b(?:" + nouns + r")\b[^.!?]{0,120}\b" + issues + r"\b|\b" + issues + r"\b[^.!?]{0,120}\b(?:" + nouns + r")\b", text, re.I))


def _sites(log, register, period, issues, source_text):
    employees = {employee.employee_id: employee for employee in register}
    days = {key: set() for key in employees}
    refs = defaultdict(list)
    errors = []
    unassigned = []
    if _incomplete(source_text, r"site(?: sign[- ]in)?|sign[- ]in|pages|site records?"):
        errors.append("Disclosed missing or incomplete site records prevent complete office/site confirmation.")
    if log is None or set(log.columns) != {"date", "employee_id", "name", "site", "signed_in_at"} or not log.rows:
        errors.append("Site records are missing, empty or have an unsupported schema; absence does not establish zero activity.")
    else:
        for row, ref in _row_references(log):
            key = row.values["employee_id"]
            if key not in employees:
                unassigned.append(ref)
                errors.append("An unattributed site identity needs confirmation; no employee is inferred.")
            else:
                refs[key].append(ref)
                if row.values["name"] != employees[key].name:
                    errors.append("A site employee ID/name conflict requires identity confirmation without assuming an alias.")
            try:
                day = _day(row.values["date"], period)
                if not row.values["site"].strip() or not row.values["signed_in_at"].strip():
                    raise ValueError
                if key in employees:
                    days[key].add(day)
            except (ValueError, TypeError):
                errors.append("A site record has invalid or outside-period date/site details.")
    if errors:
        issues.append(OpenItem("Electrical site evidence", " ".join(dict.fromkeys(errors)), "Provide complete, consistent site identities and dates; resolve unmatched visitors.",
            ((_source(log, "examined site sign-in log"),) if log else ())))
    return days, refs, errors, tuple(unassigned)


def _travel_facts(note_text, business_text):
    text = note_text.casefold()
    all_text = (business_text + " " + note_text).casefold()
    separate = bool(re.search(r"(?:^|[.!?;]\s+)they were paid [^.!?]{0,130} on top of wages, shown in its own column of the payroll register\.", text))
    contradiction = re.search(r"\balready included\b|\b(?:not|never)\s+(?:paid|on top|additional|separate)\b|\bincluded in (?:regular |base )?wages\b|\bincluded in wages_paid\b", all_text)
    if contradiction:
        separate = False
    flat = bool(re.search(r"(?:^|[.!?;]\s+)they were paid a flat amount per day away on top of wages, shown in its own column of the payroll register\.", text))
    if re.search(r"\b(?:variable|varied|vary)\b|\b(?:not|never|no)\b[^.!?]{0,40}\b(?:flat|uniform|fixed)\b", all_text):
        flat = False
    days_complete = not _incomplete(all_text, r"travel[- ]days?|travel days?|day counts?|trips?|travel records?")
    return (True if separate else None), flat, days_complete


def _allowances(inputs, business, payroll, register, period, notes, decisions, interview, interview_errors, issues):
    if not _ALLOWANCE_COLUMNS.issubset(payroll.columns):
        issues.append(OpenItem("Travel allowance columns", "Original travel-day and allowance columns are missing; no complete zero adjustment set is inferred.",
            "Supply travel_days and travel_allowance_paid for every register employee.", (_source(payroll, "payroll travel schema"),)))
        return None, (), None
    separate, flat, days_context_complete = _travel_facts(_text(notes), _text(business))
    if not days_context_complete:
        issues.append(OpenItem("Travel day completeness", "Disclosed missing or incomplete travel counts cannot substantiate a daily exclusion.",
            "Provide complete audited-period travel counts and resolve omitted or estimated days.",
            tuple(_source(doc, "travel count context") for doc in (business, notes) if doc)))
    cases = []
    by_id = {employee.employee_id: employee for employee in register}
    for row, source in _row_references(payroll):
        key = row.values["employee_id"]
        raw_days = row.values["travel_days"]
        days = int(raw_days) if re.fullmatch(r"[0-9]+", raw_days) else None
        amount = row.values["travel_allowance_paid"]
        rate = None
        if flat and days and days > 0:
            per_day, remainder = divmod(_cents(amount, key), days)
            if not remainder:
                rate = _money(per_day)
        allowance = TravelAllowance(f"travel:{key}", key, by_id[key].name, amount, days, source, source,
            days_complete=days is not None and days_context_complete, separate_from_base=separate, decision=decisions[key], raw_record=row,
            uniform_daily_amount=rate,
            rate_source=_source(notes, "documented flat daily allowance and additional wage basis") if notes and flat else None)
        cases.append(TravelCase(period, allowance))
    try:
        engine = PayrollAdjuster(inputs.guide, interview, source_errors=interview_errors)
        result = engine.evaluate_batch(travel=cases)
        lines = []
        for line in result.lines:
            record = line.input_record
            if line.status == "OPEN" and record.travel_days == 0 and _cents(record.amount, record.employee_id) > 0:
                line = replace(line, required_confirmation=(*line.required_confirmation,
                    "Confirm whether zero recorded out-of-town days is correct and provide any missing travel dates.",
                    "Explain the allowance's purpose and supply supporting payment/travel documentation.",
                    "Confirm this payment is not already included in wages_paid before approving an addition.",
                    "Approve or revise the separate proposed inclusion under the verified work code; no zero-day treatment is assumed."),
                    rule_sources=tuple(dict.fromkeys((*line.rule_sources, *record.decision.rule_sources))))
            lines.append(line)
        result = summarize_adjustments(lines, expected_cases=cases)
    except AdjustmentError as exc:
        issues.append(OpenItem("Travel adjustment sources", str(exc), "Correct the original monetary evidence before confirming adjustments.", (_source(payroll, "travel monetary rows"),)))
        return None, (), separate
    return result, (str(payroll.path),), separate


def evaluate_electrical(inputs, business, notes, payroll, register, period, evaluator, log, interview, interview_errors, files):
    issues = []
    paragraphs = _paragraphs(inputs.guide)
    context = tuple(_source(doc, "business description" if doc is business else "auditor field notes") for doc in (business, notes) if doc)
    business_text, note_text = _text(business), _text(notes)
    prose = (business_text + " " + note_text).casefold()
    errors = []
    if not notes or period is None or "shop and office" not in note_text.casefold() or not re.search(r"\bsome of the electricians spent weeks on an out-of-town job\b", note_text, re.I):
        errors.append("Confirm the exact audit period and corroborating electrical field/office observations.")
    if re.search(r"\b(?:no longer|not|never)\b[^.!?]{0,80}\b(?:wiring|electrical work|electricians spent)\b", prose):
        errors.append("Negated wiring or field observations require actual-duty review.")
    mapped = {files.business, files.notes, files.payroll, files.application, files.site_signins}
    extra = [doc for doc in inputs.records if str(doc.path.relative_to(inputs.records_root)) not in mapped]
    if extra or set(payroll.columns) - (_BASE_COLUMNS | _ALLOWANCE_COLUMNS):
        errors.append("Unmapped source files or payroll columns require duty and allowance review.")
        context += tuple(_source(doc, "unmapped evidence") for doc in extra)
    days, site_refs, site_errors, unassigned = _sites(log, register, period, issues, prose)
    owner_names = re.findall(r"\bincluding the owner, ([^,]+), who has not filed an election of exclusion\.", business_text, re.I)
    owner_name = owner_names[0] if len(owner_names) == 1 else None
    election_conflict = bool(re.search(r"\b(?:has|have|had) (?:since |now |already )?filed (?:an? )?election of exclusion\b|\belection of exclusion\b[^.!?]{0,30}\b(?:was|is|has been) (?:filed|approved)\b", prose))
    # Strip only supported named observations. Additional named duty statements
    # cannot silently be overridden by the register title or application.
    remaining = note_text.casefold()
    owner_observations = {}
    office_observations = {}
    for employee in register:
        name = re.escape(employee.name.casefold())
        owner_pattern = re.compile(r"\bthe owner, " + name + r", leads a crew on site most days and pulls wire himself;")
        office_pattern = re.compile(r"\bthe office administrator, " + name + r", runs the office and never goes to jobs\.")
        owner_observations[employee.employee_id] = bool(owner_pattern.search(remaining))
        office_observations[employee.employee_id] = bool(office_pattern.search(remaining))
        remaining = owner_pattern.sub(" ", remaining)
        remaining = office_pattern.sub(" ", remaining)
    remaining_business = business_text.casefold()
    if owner_name:
        remaining_business = re.sub(r"\bincluding the owner, " + re.escape(owner_name.casefold()) + r", who has not filed an election of exclusion\.", " ", remaining_business)
    remaining += " " + remaining_business
    if any(employee.name and employee.name.casefold() in remaining for employee in register):
        errors.append("Additional individual duty observations require review; register titles cannot override conflicting prose.")
    if re.search(r"\b(?:misleading|actual duties|instead|contrary|exclusively|warehouse|roofing|siding|incomplete)\b", remaining):
        errors.append("Exceptional or incomplete work evidence is outside this adapter's supported electrical context.")
    if re.search(r"\b(?:electricians?|crew|employees?|staff)\b[^.!?]{0,100}\b(?:work only in the office|office duties|clerical|bookkeep\w*)\b", remaining):
        errors.append("Collective office-duty statements conflict with supported electrical field observations; confirm actual duties.")
    decisions = {}
    owner_key = None
    for employee in register:
        key = employee.employee_id
        role = str(employee.raw_record.values.get("position", "")).casefold()
        evidence = (employee.source, *context, *((_source(log, "examined site sign-in log"),) if log else ()), *site_refs[key])
        owner_role = bool(re.search(r"\bowner\b", role)) or employee.name == owner_name
        decision_errors = list(errors)
        if owner_role:
            owner_key = key
            if employee.name != owner_name or election_conflict or not owner_observations[key] or site_errors or not days[key]:
                decision_errors.append("Confirm the same owner's documented non-exclusion, actual wire-pulling duties and consistent site evidence; do not remove recorded wages or assume management duties.")
            decision = _pending(" ".join(decision_errors), evidence, _refs(paragraphs, ("CG-05", "CG-21"))[0]) if decision_errors else _direct("E-510", paragraphs, evaluator, evidence, owner=True)
        elif role == "office administrator":
            if not office_observations[key] or site_errors or days[key]:
                decision_errors.append("Confirm this named administrator's office-only duties and resolve any contradictory site evidence; a title or absent sign-in alone is insufficient.")
            decision = _pending(" ".join(decision_errors), evidence, _refs(paragraphs, ("CG-02", "CG-04"))[0]) if decision_errors else _direct("C-110", paragraphs, evaluator, evidence)
        elif role in {"master electrician", "journeyman electrician", "electrician", "apprentice electrician"}:
            decision = _pending(" ".join(decision_errors), evidence) if decision_errors else _direct("E-510", paragraphs, evaluator, evidence)
        else:
            decision = _pending("The register role and field observations do not establish supported electrical or office duties; confirm the employee's actual work.", evidence)
        decisions[key] = decision
    owner_employee = next((employee for employee in register if employee.employee_id == owner_key), None)
    owner_refs = tuple(dict.fromkeys((*context, *_refs(paragraphs, ("CG-05",))[0],
        *((owner_employee.source,) if owner_employee else ()))))
    included = owner_key is not None and decisions[owner_key].status == "CLASSIFIED"
    owner = OwnerAssessment(owner_name or (owner_employee.name if owner_employee else None),
        "INCLUDED" if included else "OPEN", "No exclusion is documented, and actual electrical fieldwork supports including the owner's recorded wages under CG-05/CG-21." if included else
        "Confirm the owner's election status, identity and actual duties; all recorded owner wages remain in the register.", _money(0), owner_refs)
    if not included:
        issues.append(OpenItem("Owner inclusion", owner.reason, "Provide the authoritative election status and owner-duty evidence.", owner.sources))
    proposals = {}
    for employee in register:
        decision = decisions[employee.employee_id]
        if decision.status == "OPEN":
            proposal = ClassificationProposal(None, None, employee.wages, "Retain the entire recorded wage OPEN until duties and applicability are confirmed; no code is guessed.",
                decision.required_confirmation, decision.rule_sources, decision.evidence_sources)
            proposals[employee.employee_id] = proposal
            issues.append(OpenItem(f"{employee.name} [{employee.employee_id}]", decision.reason, "; ".join(decision.required_confirmation), decision.evidence_sources + decision.rule_sources, proposal))
    adjustments, consumed, separate = _allowances(inputs, business, payroll, register, period, notes, decisions, interview, interview_errors, issues)
    return ElectricalEvaluation(decisions, proposals, owner, adjustments, consumed,
        {key: tuple(sorted(value)) for key, value in days.items()}, unassigned, separate, tuple(issues))


def combine_travel(result, separate):
    wage, allowance = result.independent_reconciliation, result.adjustments.reconciliation
    known = _cents(wage.register_total, "Register") + _cents(allowance.payroll_added, "Allowance additions")
    classified = sum(_cents(value, code) for code, value in result.by_code.items())
    wage_open = _cents(wage.unresolved_total, "OPEN wages")
    cash = _cents(wage.register_total, "Register") + _cents(allowance.basis_total, "Original allowances") if separate is True else None
    cash_difference = cash - known - _cents(allowance.nonpayroll, "Excluded allowances") - _cents(allowance.unresolved_basis, "OPEN allowances") if cash is not None else None
    return TravelPayrollReconciliation(wage.register_total, wage.allocated_total, wage.unresolved_total,
        allowance.basis_total, allowance.payroll_added, allowance.nonpayroll, allowance.unresolved_basis,
        _money(known), _money(classified), _money(known - classified - wage_open),
        _money(cash) if cash is not None else None, _money(cash_difference) if cash_difference is not None else None,
        wage.reconciled, allowance.reconciled)


def employee_totals(result):
    cents = defaultdict(lambda: defaultdict(int))
    for line in result.allocation.lines:
        cents[line.employee.employee_id][line.class_code or "OPEN"] += _cents(line.wages, line.employee.employee_id)
    for line in result.adjustments.lines:
        if line.status == "VERIFIED" and line.class_code:
            cents[line.input_record.employee_id][line.class_code] += _cents(line.payroll_added, line.adjustment_id)
    return {key: {code: _money(value) for code, value in sorted(codes.items())} for key, codes in cents.items()}
