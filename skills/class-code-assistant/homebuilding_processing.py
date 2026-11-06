"""Source-bound homebuilding adapter; uncertain identities never authorize money."""

from collections import Counter
from dataclasses import dataclass, replace
from datetime import date
import re

from contractor_processing import _day, _GUIDE_WORDING as CONTRACTOR_WORDING
from employer_processing import (
    ClassificationProposal, CombinedPayrollReconciliation, GoverningFieldEvidence,
    OpenItem, OwnerAssessment, _pending, _source,
)
from legal_office_processing import _row_references
from payroll_allocation import _cents, _money
from payroll_adjustments import (
    AdjustmentError, AdjustmentResult, Certificate, PayrollAdjuster, ProposedTreatment,
    SubcontractorCase, SubcontractorPayment, summarize_adjustments,
)
from rule_evaluator import Decision, RuleFacts, _reference


@dataclass(frozen=True)
class HomebuildingEvaluation:
    decisions: dict
    proposals: dict
    site_visits: dict
    governing_field: GoverningFieldEvidence
    owner: OwnerAssessment
    adjustments: AdjustmentResult | None
    adapted_sources: tuple
    unassigned_site_records: tuple
    open_items: tuple


_WORDING = {
    **CONTRACTOR_WORDING,
    "CG-05": "**CG-05. Owners and executive officers.** An owner or executive officer who has filed an election of exclusion is not counted. An owner who is included is counted under the code for the work the owner does.",
    "CG-15": "**CG-15. H-420 Residential homebuilding.** Construction and remodeling of dwellings: framing, drywall, interior finish, carpentry and general labor at the building site. Roofing work is described by CG-11 and electrical wiring by CG-21.",
}


def _paragraphs(guide):
    headings = list(re.finditer(r"(?m)^\*\*(CG-[0-9]+)\.", guide.text))
    paragraphs = {}
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(guide.text)
        ref = _reference(guide, heading.start(), end, heading.group(1))
        paragraphs.setdefault(ref.locator, []).append(ref)
    return paragraphs


def _verified_refs(paragraphs, identifiers):
    refs = tuple(ref for key in identifiers for ref in paragraphs.get(key, ()))
    valid = all(len(paragraphs.get(key, ())) == 1 for key in identifiers)
    valid = valid and all(" ".join(ref.excerpt.split()) in
        (_WORDING[ref.locator], _WORDING[ref.locator] + " ## Class codes") for ref in refs)
    return refs, valid


def _work_decision(work, paragraphs, evidence, evaluator):
    # CG-15 explicitly lists framing/drywall; CG-11 covers roofing. No
    # roofing-day threshold is applied to general homebuilding or trade invoices.
    code, paragraph = {"framing": ("H-420", "CG-15"), "drywall": ("H-420", "CG-15"),
                       "carpentry": ("H-420", "CG-15"), "general labor": ("H-420", "CG-15"),
                       "roofing": ("R-310", "CG-11")}.get(work, (None, None))
    refs, valid = _verified_refs(paragraphs, ("CG-02", paragraph)) if paragraph else ((), False)
    if not valid or code in evaluator.code_errors:
        return _pending("The documented work or current guide definition does not establish a verified work code.", evidence, refs)
    return Decision("documented_homebuilding_work", "CLASSIFIED", code, paragraph,
        f"Documented {work} duties fall within the verified {paragraph} definition.", (), refs,
        tuple(evidence), ("documented construction/trade work", "verified current guide definition"), "whole_audit_period")


def _owner(business, register, paragraphs):
    refs, valid = _verified_refs(paragraphs, ("CG-05",))
    text = " ".join(business.text.split())
    names = re.findall(r"\bThe owner, ([^,]+),", text)
    name = names[0] if len(names) == 1 else None
    election = name and f"The owner, {name}, has filed an election of exclusion and is not on the payroll register." in text
    if re.search(r"\b(?:revoked|rescinded|withdrawn|cancelled|canceled|never filed|not filed)\b", text, re.I):
        election = False
    # An election assertion does not authorize silently deleting a conflicting
    # payroll record. No hypothetical owner wage is created or subtracted.
    present = any(row.name.casefold() == name.casefold() or str(row.raw_record.values.get("position", "")).casefold() in
                  {"owner", "executive officer"} for row in register) if name else True
    excluded = bool(valid and election and not present)
    reason = ("The business record documents a filed exclusion election and no owner wage appears in the register."
              if excluded else "Confirm a documented filed election and resolve any owner/register conflict; retain all recorded wages.")
    return OwnerAssessment(name, "EXCLUDED" if excluded else "OPEN", reason, _money(0),
                           (_source(business, "owner election statement"), *refs))


def _iso_day(value):
    try:
        day = date.fromisoformat(value)
        return day if day.isoformat() == value else None
    except (ValueError, TypeError):
        return None


def _related_name(left, right):
    # Candidate retrieval ONLY: the adjustment evaluator still sees both original
    # different names and returns OPEN. This is never an identity/coverage match.
    if left.casefold() == right.casefold():
        return left != right
    left, right = left.casefold(), right.casefold()
    first, second = re.findall(r"[a-z0-9]+", left), re.findall(r"[a-z0-9]+", right)
    shared_leading_name = len(first) >= 2 and len(second) >= 2 and first[:2] == second[:2]
    return left != right and (shared_leading_name or right.startswith(left + " ") or left.startswith(right + " "))


def _subcontractors(payments, inventory, notes, period, paragraphs, evaluator, adjuster, issues):
    if payments is None or not payments.rows or period is None or set(payments.columns) != {"date", "subcontractor", "work", "invoice", "amount_paid"}:
        issues.append(OpenItem("Subcontractor payments", "A complete supported payment table and audit period are required; no combined total is confirmed.", "Provide the complete original payments and exact audit period."))
        return None, (), ()
    certs = []
    inventory_valid = inventory is not None and set(inventory.columns) == {"subcontractor", "certificate_no", "coverage_from", "coverage_to"}
    if inventory_valid:
        seen = set()
        for row, ref in _row_references(inventory):
            values = row.values
            number = values["certificate_no"]
            if not number.strip() or not values["subcontractor"].strip() or number in seen:
                inventory_valid = False
            seen.add(number)
            certs.append(Certificate(number, values["subcontractor"], _iso_day(values["coverage_from"]), _iso_day(values["coverage_to"]), ref, row))
    note_text = " ".join(notes.text.lower().split()) if notes else ""
    search_documented = bool(inventory_valid and re.search(
        r"(?:^|[.!?;]\s+)(?:we )?collected the certificates of insurance the owner could find\.", note_text))
    if not inventory_valid or not search_documented:
        issues.append(OpenItem("Certificate inventory", "The supplied certificate inventory or documented search is missing, malformed or incomplete.",
            "Supply the complete certificate inventory and document the search before treating unprovided proof as genuinely missing.",
            (_source(inventory, "certificate inventory"),) if inventory else ()))
    cases = []
    for row, ref in _row_references(payments):
        values = row.values
        evidence = (ref, *(() if notes is None else (_source(notes, "subcontractor field observations"),)))
        work = _work_decision(values["work"], paragraphs, evidence, evaluator)
        if re.search(re.escape(values["subcontractor"].casefold()) + r"[^.!?]{0,100}\b(?:performed|does|did|works?|duties|only)\b", note_text):
            work = _pending("Individual subcontractor duty prose requires review against the payment work description; no invoice code overrides conflicting actual-work evidence.", evidence, work.rule_sources)
        record = SubcontractorPayment(values["invoice"], values["subcontractor"], _iso_day(values["date"]),
            values["work"], values["amount_paid"], ref, work, row)
        exact = tuple(cert for cert in certs if cert.subcontractor == record.subcontractor)
        candidates = tuple(cert for cert in certs if _related_name(record.subcontractor, cert.subcontractor))
        selected = (exact or candidates) if inventory_valid else None
        cases.append(SubcontractorCase(period, record, selected, search_documented,
            _source(inventory, "complete supplied certificate inventory") if search_documented else None))
    try:
        evaluated = adjuster.evaluate_batch(subcontractors=cases)
        lines = []
        for case, line in zip(cases, evaluated.lines):
            if line.status == "OPEN" and case.certificates and any(cert.subcontractor != case.payment.subcontractor for cert in case.certificates):
                # Ask what would apply WITHOUT full-period coverage, without
                # ever editing the original certificate's identity or accepting it.
                hypothetical = adjuster.subcontractor(replace(case, certificates=()))
                if hypothetical.status == "VERIFIED":
                    proposal = ProposedTreatment(hypothetical.payroll_added, hypothetical.nonpayroll,
                        "Conditional missing-full-period-coverage treatment only; confirm payee/certificate identity and any replacement coverage. This proposal contributes no verified payroll.")
                    line = replace(line, proposal=proposal)
            lines.append(line)
        result = summarize_adjustments(lines, expected_cases=cases)
    except AdjustmentError as exc:
        issues.append(OpenItem("Subcontractor source validation", str(exc), "Correct the original monetary records; no partial combined total is confirmed.", (_source(payments, "subcontractor payment table"),)))
        return None, (), tuple(cases)
    consumed = (str(payments.path),) + ((str(inventory.path),) if inventory_valid else ())
    return result, consumed, tuple(cases)


def _estimator_measurement_visits(note_text):
    """Recognize stated measurement visits, leaving other duty prose for review."""
    frequency = r"(?:occasionally|sometimes|periodically|now and then)"
    site = r"(?:(?:a|the) )?(?:(?:building|job|construction)[ -])?sites?"
    purpose = r"(?:to (?:measure|take measurements)|for measurements)"
    visit = (rf"(?:the )?estimator (?:{frequency} )?"
             rf"(?:visits|travels to|goes to) {site}(?: {frequency})?")
    observation = rf"(?:{purpose},? {visit}|{visit} {purpose})"
    statements = [sentence.strip() for sentence in re.split(r"[.!?]", note_text)
                  if re.search(r"\bestimator\b", sentence)]
    # A positive clause cannot override another unsupported/uncertain duty
    # statement. Full matches also reject negation, attribution and extra tasks.
    return bool(statements) and all(re.fullmatch(observation, sentence) for sentence in statements)


def evaluate_homebuilding(inputs, business, notes, log, payroll, register, period, evaluator,
                         payments, inventory, interview, interview_errors, files):
    issues = []
    paragraphs = _paragraphs(inputs.guide)
    context = tuple(_source(doc, "business description" if doc is business else "auditor field notes") for doc in (business, notes) if doc)
    business_text = " ".join(business.text.lower().split())
    note_text = " ".join(notes.text.lower().split()) if notes else ""
    mapped = {files.business, files.notes, files.payroll, files.application, files.site_signins, files.subcontractor_payments, files.certificates}
    extra = [doc for doc in inputs.records if str(doc.path.relative_to(inputs.records_root)) not in mapped]
    errors = []
    if extra or set(payroll.columns) != {"employee_id", "name", "position", "wages_paid"}:
        errors.append("Unmapped source files or payroll columns require actual-duty review.")
        context += tuple(_source(doc, "unmapped evidence") for doc in extra)
    if period is None or not notes or not re.search(r"(?:^|[.!?;]\s+)(?:[1-9][0-9]*|one|two|three|four|five|six|seven|eight|nine|ten|several|many) houses under construction\.", note_text):
        errors.append("Confirm the audit period and corroborating construction observations.")
    if not re.search(r"framing, drywall, finish carpentry and site labor with its own crew", business_text):
        errors.append("The supported own-crew homebuilding duties are not documented.")
    prose = business_text + " " + note_text
    if re.search(r"\b(?:actual duties|misleading|contrary|instead|incomplete|unavailable|unconfirmed)\b", prose):
        errors.append("Exceptional, conflicting or incomplete duty/record evidence requires human review.")
    if re.search(r"\b(?:no longer|not|never|doesn't)\b[^.!?]{0,60}\b(?:build\w*|own crew|framing|construction)\b", business_text):
        errors.append("Negated construction-business observations do not establish this adapter's supported duties.")
    office_errors = []
    if re.search(r"\b(?:bookkeeper|estimator|office manager)\b[^.!?]{0,100}\b(?:install\w*|repair\w*|roof\w*|physical work|field work)\b", prose):
        office_errors.append("Physical-work evidence conflicts with supported office observations; confirm actual duties and rule applicability.")
    if re.search(r"\b(?:timesheets?|sign[- ]in|records?|pages)\b[^.!?]{0,100}\b(?:missing|incomplete|unavailable|lost|not complete)\b|\b(?:missing|incomplete|unavailable|lost)\b[^.!?]{0,100}\b(?:timesheets?|sign[- ]in|records?|pages)\b", prose):
        office_errors.append("Explicit missing audit-period records prevent complete office-visit bounds; obtain the missing records.")
    employees = {row.employee_id: row for row in register}
    if any(re.search(re.escape(employee.name.casefold()) + r"[^.!?]{0,100}\b(?:roof\w*|siding|wiring|nurs\w*|landscap\w*|physical work|exclusively)\b", prose) for employee in register):
        errors.append("Named employee duty exceptions require review; register titles cannot override individual actual-work evidence.")
    roles = {key: str(row.raw_record.values.get("position", "")).casefold() for key, row in employees.items()}
    counts = Counter(roles.values())
    office = set()
    field = set()
    for key, role in roles.items():
        if role in {"lead carpenter", "carpenter", "laborer"}:
            field.add(key)
        elif role == "estimator" and counts[role] == 1 and _estimator_measurement_visits(note_text):
            office.add(key)
        elif role == "bookkeeper" and counts[role] == 1 and re.search(r"\bthe bookkeeper stays in the office\.", note_text):
            office.add(key)
        elif role == "office manager" and f"the office manager, {employees[key].name.casefold()}, drives material and paperwork out to the sites and meets inspectors there;" in note_text:
            office.add(key)
    decisions = {}
    for key in field:
        evidence = (employees[key].source, *context)
        decisions[key] = _pending(" ".join(errors), evidence) if errors else _work_decision("carpentry" if "carpenter" in roles[key] else "general labor", paragraphs, evidence, evaluator)
    owner = _owner(business, register, paragraphs)
    if owner.status == "OPEN":
        issues.append(OpenItem("Owner election", owner.reason, "Provide the filed election and reconcile any owner payroll record.", owner.sources))
    adjuster = PayrollAdjuster(inputs.guide, interview, source_errors=interview_errors)
    adjustments, consumed, cases = _subcontractors(payments, inventory, notes, period, paragraphs, evaluator, adjuster, issues)
    field_cents = sum(_cents(employees[key].wages, key) for key in field if decisions[key].status == "CLASSIFIED")
    unknown = set(employees) - field - office
    # Upper bound competing trade exposure by full payment amounts, before any
    # insurance exclusion or 60-percent reduction. If H-420 still dominates, the
    # governing code cannot change while certificate identities are unresolved.
    competing = sum(max(0, _cents(case.payment.amount, case.payment.payment_id)) for case in cases
                    if case.payment.decision.class_code != "H-420")
    complete = adjustments is not None and not unknown and not errors and bool(field) and all(decisions[key].status == "CLASSIFIED" for key in field)
    governing_code = "H-420" if complete and field_cents > competing and field_cents > 0 else None
    governing_refs = tuple(dict.fromkeys(ref for key in sorted(field) for ref in decisions[key].evidence_sources))
    governing_rules = tuple(dict.fromkeys(ref for key in sorted(field) for ref in decisions[key].rule_sources))
    governing = GoverningFieldEvidence(governing_code, {"H-420": _money(field_cents)} if field_cents else {}, tuple(key for key in employees if key in field),
        "Verified own-crew H-420 wages exceed even the full recorded competing trade payment basis; office wages are excluded to avoid circular assignment." if governing_code else
        "The governing field code is OPEN: field membership, monetary sources or potential competing exposure do not establish a unique leader.",
        governing_rules, (*governing_refs, *context, *tuple(case.payment.source for case in cases)))
    visits = {key: set() for key in office}
    visit_refs = {key: [] for key in employees}
    visit_errors = {key: [] for key in employees}
    log_errors = []
    unassigned = []
    external = []
    unidentified = []
    possible_days = set()
    valid_log = log is not None and set(log.columns) == {"date", "employee_id", "name", "site", "signed_in_at"}
    if not valid_log or not log.rows:
        log_errors.append("Site sign-ins are missing or have an unsupported schema; missing evidence is not zero visits.")
    else:
        for row, ref in _row_references(log):
            key = row.values["employee_id"]
            if key not in employees:
                unassigned.append(ref)
                name = " ".join(row.values["name"].casefold().split())
                # An explicit governmental inspector role is external evidence,
                # not an unidentified employee. An ID or a matching register
                # name prevents this exclusion; preserve such ambiguity below.
                external_role = re.fullmatch(r"(?:county|city|municipal|state) (?:building )?inspector", name)
                # Additional visitor/date prose may contradict the role label;
                # interpreting it requires review, not an assumed identity.
                discussed = re.search(r"\b(?:inspector|visitor)\b", prose) or (
                    row.values["date"] and row.values["date"] in prose)
                if external_role and discussed:
                    log_errors.append("An inspector label is also discussed in employer prose; confirm identity and resolve that additional evidence before excluding any employee visits.")
                elif not key.strip() and external_role and not any(
                    name == " ".join(employee.name.casefold().split()) for employee in register
                ):
                    external.append(ref)
                    continue
                unidentified.append(ref)
                try:
                    possible_days.add(_day(row.values["date"], period))
                except (ValueError, TypeError):
                    log_errors.append("An unattributed sign-in has an invalid date; possible employee visits cannot be bounded.")
                continue
            visit_refs[key].append(ref)
            if row.values["name"] != employees[key].name:
                log_errors.append("A sign-in ID/name conflict requires identity confirmation.")
            try:
                day = _day(row.values["date"], period)
                if not row.values["site"].strip() or not row.values["signed_in_at"].strip():
                    raise ValueError
                if key in visits:
                    visits[key].add(day)
            except (ValueError, TypeError):
                visit_errors[key].append("A site record has invalid date/site details or falls outside the audit period.")
    if external:
        issues.append(OpenItem("External site visitors", "The source explicitly records external governmental inspectors with no employee ID or matching payroll name; their visits are excluded from employee site-day bounds, with the original records retained.",
            "Confirm the cited inspectors were external nonpayroll visitors, the recorded roles are accurate, and the employee sign-in records are complete; correct any conflicting identity evidence.", tuple(external)))
    if unidentified:
        issues.append(OpenItem("Unattributed site sign-ins", "No employee identity is assumed for unmatched sign-ins; dates provide possible-visit bounds only.",
            "Confirm whether the unmatched entries are nonpayroll visitors and correct any missing employee identities.", tuple(unidentified)))
    office_refs, office_guide = _verified_refs(paragraphs, ("CG-02", "CG-04"))
    proposals = {}
    for key in office:
        all_errors = errors + office_errors + log_errors + visit_errors[key]
        evidence = tuple(dict.fromkeys((employees[key].source, *context,
            *((_source(log, "examined audit-period site sign-in log"),) if log else ()),
            *visit_refs[key], *unassigned, *governing.evidence_sources)))
        facts = RuleFacts(key, "contractor", "office", period.start if period else None, period.end if period else None,
            complete=not all_errors, evidence_sources=evidence, days=tuple(sorted(visits[key])),
            governing_field_code=governing_code, governing_code_confirmed=governing_code is not None)
        lower = evaluator.evaluate("contractor_office_visits", facts)
        upper = evaluator.evaluate("contractor_office_visits", replace(facts, days=tuple(sorted(visits[key] | possible_days))))
        if all_errors or not office_guide:
            decision = _pending(" ".join(all_errors) if all_errors else "The current guide's office definitions require review.", evidence, office_refs)
        elif lower.status == upper.status == "CLASSIFIED" and lower.class_code == upper.class_code:
            decision = replace(lower, reason=f"Between {len(visits[key])} confirmed and {len(visits[key] | possible_days)} possible distinct site days; both bounds return {lower.class_code}. " + lower.reason,
                rule_sources=tuple(dict.fromkeys((*lower.rule_sources, *governing_rules))))
        else:
            decision = _pending("Office visit bounds or the governing field code do not establish one verified classification. " + lower.reason + " " + upper.reason,
                evidence, tuple(dict.fromkeys((*lower.rule_sources, *upper.rule_sources))))
            if lower.status == "CLASSIFIED":
                proposals[key] = ClassificationProposal(lower.class_code, lower.rationale_ref, employees[key].wages,
                    "Conditional treatment using only confirmed visits, pending identity/completeness confirmation; not a verified allocation.",
                    decision.required_confirmation, lower.rule_sources, evidence)
        decisions[key] = decision
    for key in unknown:
        decisions[key] = _pending("The actual-duty evidence does not establish supported employee duties; retain recorded wages and obtain confirmation.", (employees[key].source, *context))
    for key, decision in decisions.items():
        if decision.status == "OPEN":
            issues.append(OpenItem(f"{employees[key].name} [{key}]", decision.reason, "; ".join(decision.required_confirmation),
                decision.evidence_sources + decision.rule_sources, proposals.get(key)))
    return HomebuildingEvaluation(decisions, proposals, {key: tuple(sorted(days)) for key, days in visits.items()} if valid_log else {},
        governing, owner, adjustments, consumed, tuple(unassigned), tuple(issues))


def combine_payroll(result):
    employee = result.independent_reconciliation
    subcontract = result.adjustments.reconciliation
    confirmed = _cents(employee.register_total, "Register") + _cents(subcontract.payroll_added, "Subcontractor additions")
    classified = sum(_cents(value, code) for code, value in result.by_code.items())
    pending = _cents(employee.unresolved_total, "OPEN employee payroll")
    return CombinedPayrollReconciliation(employee.register_total, employee.allocated_total, employee.unresolved_total,
        subcontract.basis_total, subcontract.payroll_added, subcontract.nonpayroll, subcontract.unresolved_basis,
        _money(confirmed), _money(classified), _money(confirmed - classified - pending), employee.reconciled, subcontract.reconciled)
