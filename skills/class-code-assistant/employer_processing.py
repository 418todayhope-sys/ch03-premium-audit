"""Read-only employer workflow; unsupported evidence remains OPEN."""

from __future__ import annotations

import calendar
from dataclasses import dataclass, field, replace
from datetime import date, datetime
from decimal import Decimal, localcontext
from pathlib import Path
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from courier_processing import WeeklyEmployeeResult, WeeklyPayrollReconciliation
    from electrical_processing import TravelPayrollReconciliation

from input_reader import CSVSource, InputError, Inputs, MarkdownSource, read_inputs, read_markdown
from payroll_allocation import (
    AllocationError, AllocationResult, PayrollRecord, Reconciliation, _cents, _money,
    allocate_parts, allocate_payroll, reconcile_payroll, records_from_csv,
)
from payroll_adjustments import AdjustmentResult, AuditPeriod, PayrollAdjuster
from rule_evaluator import Decision, RuleEvaluator, RuleFacts, SourceReference, _reference


@dataclass(frozen=True)
class EmployerFiles:
    business: str = "business-description.md"
    notes: str = "field-notes.md"
    payroll: str = "payroll-register.csv"
    application: str = "application.md"
    receipts: str = "gross-receipts.csv"
    site_signins: str = "site-signin-log.csv"
    crew_timesheets: str = "crew-timesheets.csv"
    subcontractor_payments: str = "subcontractor-payments.csv"
    certificates: str = "insurance-certificates.csv"
    routes: str = "route-log.csv"
    weekly_payroll: str = "weekly-payroll.csv"


@dataclass(frozen=True)
class ClassificationProposal:
    class_code: str | None
    rationale_ref: str | None
    wages: Decimal
    reason: str
    required_confirmation: tuple[str, ...]
    rule_sources: tuple[SourceReference, ...]
    evidence_sources: tuple[SourceReference, ...]


@dataclass(frozen=True)
class OpenItem:
    subject: str
    reason: str
    required_confirmation: str
    sources: tuple[SourceReference, ...] = ()
    proposed_treatment: ClassificationProposal | None = None


@dataclass(frozen=True)
class ReceiptSummary:
    dine_in: Decimal
    offsite: Decimal
    total: Decimal
    percentage: Decimal | None
    months: tuple[str, ...]
    coverage_confirmed: bool
    sources: tuple[SourceReference, ...]


@dataclass(frozen=True)
class ApplicationClass:
    class_code: str
    employees: int
    payroll: Decimal
    source: SourceReference


@dataclass(frozen=True)
class ApplicationComparison:
    reported: tuple[ApplicationClass, ...]
    reported_total: Decimal
    register_total: Decimal
    register_difference: Decimal
    verified_differences: dict[str, Decimal]
    unresolved_payroll: Decimal
    definitive: bool


@dataclass(frozen=True)
class GoverningFieldEvidence:
    class_code: str | None
    by_code: dict[str, Decimal]
    employee_ids: tuple[str, ...]
    reason: str
    rule_sources: tuple[SourceReference, ...]
    evidence_sources: tuple[SourceReference, ...]


@dataclass(frozen=True)
class EmployeeClassComparison:
    employee_id: str
    wages: Decimal
    reported_code: str | None
    calculated_code: str | None
    status: str
    reported_inferred: bool
    reason: str
    sources: tuple[SourceReference, ...]


@dataclass(frozen=True)
class OwnerAssessment:
    name: str | None
    status: str
    reason: str
    removed_wages: Decimal
    sources: tuple[SourceReference, ...]


@dataclass(frozen=True)
class CombinedPayrollReconciliation:
    employee_register_total: Decimal
    employee_allocated: Decimal
    employee_open: Decimal
    subcontractor_payment_total: Decimal
    subcontractor_added: Decimal
    subcontractor_nonpayroll: Decimal
    subcontractor_open_basis: Decimal
    confirmed_payroll: Decimal
    classified_payroll: Decimal
    difference: Decimal
    employee_reconciled: bool
    subcontractor_reconciled: bool

    @property
    def reconciled(self):
        return self.employee_reconciled and self.subcontractor_reconciled and self.difference == 0


@dataclass(frozen=True)
class ProcessingResult:
    inputs: Inputs | None = None
    period: AuditPeriod | None = None
    receipts: ReceiptSummary | None = None
    register: tuple[PayrollRecord, ...] = ()
    decisions: dict[str, Decision] = field(default_factory=dict)
    allocation: AllocationResult | None = None
    adjustments: AdjustmentResult | None = None
    by_code: dict[str, Decimal] = field(default_factory=dict)
    application: ApplicationComparison | None = None
    independent_reconciliation: Reconciliation | None = None
    open_items: tuple[OpenItem, ...] = ()
    proposals: dict[str, ClassificationProposal] = field(default_factory=dict)
    site_visits: dict[str, tuple[date, ...]] = field(default_factory=dict)
    roofing_days: dict[str, tuple[date, ...]] = field(default_factory=dict)
    governing_field: GoverningFieldEvidence | None = None
    employee_comparisons: dict[str, EmployeeClassComparison] = field(default_factory=dict)
    unassigned_site_records: tuple[SourceReference, ...] = ()
    owner_assessment: OwnerAssessment | None = None
    combined_reconciliation: CombinedPayrollReconciliation | None = None
    weekly_results: tuple[WeeklyEmployeeResult, ...] = ()
    weekly_reconciliation: WeeklyPayrollReconciliation | None = None
    employee_totals: dict[str, dict[str, Decimal]] = field(default_factory=dict)
    travel_reconciliation: TravelPayrollReconciliation | None = None


_PERIOD = re.compile(r"\bAudit period\s+([A-Z][a-z]+ \d{1,2}, \d{4}) to ([A-Z][a-z]+ \d{1,2}, \d{4})\b", re.I)
_RESTAURANT_POSITION = re.compile(r"(?:sous chef|chef|(?:line|prep) cook|cook|server|host|dishwasher)", re.I)
_CATERING_POSITION = re.compile(r"(?:catering|event)\b", re.I)
_GUIDE_WORDING = {
    "CG-02": "**CG-02. Assigning codes.** An employer is assigned the class code that describes its principal business. An employee whose work is described by another code in this guide is reported under that code. An employer may carry several codes.",
    "CG-41": "**CG-41. F-710 Restaurants.** Preparation and service of meals: kitchen staff, servers, hosts and dishwashers.",
    "CG-07": "**CG-07. Division of payroll.** When an employee performs work in more than one classification and the employer keeps records of the time spent in each, the employee's payroll may be divided between the codes.",
    "CG-42": "**CG-42. F-720 Off-site caterers.** Preparation of food and its service at events away from the employer's premises, including the catering crew of an employer that also runs a restaurant.",
}


def _source(document, locator):
    return _reference(document, 0, len(document.text), locator)


def _adjustment_evidence(document):
    monetary_columns = set(document.columns) & {"travel_allowance_paid", "amount_paid"} if isinstance(document, CSVSource) else set()
    return bool(monetary_columns or re.search(r"subcontract|certificate|travel|allowance", document.path.stem, re.I))


def _pending(reason, sources=(), rule_sources=()):
    return Decision("employer_evidence", "OPEN", None, None, reason,
                    (f"Auditor or employer must confirm: {reason}",),
                    tuple(rule_sources), tuple(sources), ("documented actual duties and audit period",), "whole_audit_period")


def _period(document, issues):
    if document is not None:
        matches = _PERIOD.findall(document.text)
        if len(matches) == 1:
            try:
                start, end = (datetime.strptime(value, "%B %d, %Y").date() for value in matches[0])
                if start <= end:
                    return AuditPeriod(start, end)
            except ValueError:
                pass
    issues.append(OpenItem("Audit period", "An unambiguous valid audit period is missing from the business description.", "Supply the authoritative start and end dates.", (() if document is None else (_source(document, "business description"),))))
    return None


def _receipts(table, period, issues):
    if table is None:
        return None
    refs = (_source(table, "monthly gross receipts"),)
    needed = {"month", "dine_in_receipts", "offsite_catering_receipts"}
    if not needed.issubset(table.columns):
        issues.append(OpenItem("Gross receipts", "Required monthly receipt columns are missing.", "Provide month, dine_in_receipts and offsite_catering_receipts.", refs))
        return None
    dine = offsite = 0
    months = []
    valid = bool(table.rows)
    for row in table.rows:
        month = row.values["month"]
        try:
            parsed = datetime.strptime(month, "%Y-%m").date()
            if parsed.strftime("%Y-%m") != month or month in months:
                valid = False
        except (ValueError, TypeError):
            valid = False
        a = _cents(row.values["dine_in_receipts"], f"{table.path}:{row.line_number}")
        b = _cents(row.values["offsite_catering_receipts"], f"{table.path}:{row.line_number}")
        valid = valid and a >= 0 and b >= 0
        dine += a
        offsite += b
        months.append(month)
    total = dine + offsite
    percentage = None
    if valid and total > 0:
        with localcontext() as context:
            context.prec = max(50, len(str(abs(total))) + len(str(abs(offsite))) + 10)
            percentage = Decimal(offsite) * Decimal(100) / Decimal(total)
    else:
        valid = False
        issues.append(OpenItem("Gross receipts", "Empty, duplicate, invalid-month, negative or nonpositive-total receipts cannot verify the catering threshold.", "Provide a consistent, nonduplicated receipt summary.", refs))
    expected = []
    if period is not None and period.start.day == 1 and period.end.day == calendar.monthrange(period.end.year, period.end.month)[1]:
        year, month = period.start.year, period.start.month
        while (year, month) <= (period.end.year, period.end.month):
            expected.append(f"{year:04d}-{month:02d}")
            year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    covered = valid and bool(expected) and sorted(months) == expected
    if not covered:
        issues.append(OpenItem("Receipt audit-period coverage", "Monthly receipt labels do not establish the same complete audit period; partial-month boundaries or missing/duplicate months require confirmation.", "Supply receipts for the exact audited dates or authoritative evidence explaining the summary's period boundaries.", refs))
    return ReceiptSummary(_money(dine), _money(offsite), _money(total), percentage, tuple(months), covered, refs)


def _guide_refs(evaluator, identifiers):
    refs = tuple(ref for ref in evaluator.rule_sources["catering_receipts"] if ref.locator in identifiers)
    valid = all(sum(ref.locator == identifier for ref in refs) == 1 for identifier in identifiers)
    # The existing evaluator retains a following section heading in the source
    # excerpt. It is structural context, outside this paragraph's policy text.
    valid = valid and all(" ".join(re.split(r"(?m)^#{1,6}[ \t]+", ref.excerpt, maxsplit=1)[0].split()) == _GUIDE_WORDING.get(ref.locator) for ref in refs)
    return refs, valid


def _direct_restaurant(evaluator, evidence):
    refs, valid = _guide_refs(evaluator, ("CG-02", "CG-41"))
    valid = valid and "F-710" not in evaluator.code_errors
    if not valid:
        return _pending("The current guide does not uniquely retain verified CG-02/CG-41 restaurant definitions; obtain auditor review.", evidence, refs)
    return Decision("restaurant_actual_duties", "CLASSIFIED", "F-710", "CG-41",
                    "Restaurant business and kitchen/dining field observations corroborate this register role as preparation/service of meals under CG-02 and CG-41.", (), refs, evidence,
                    ("restaurant employer", "corroborated restaurant kitchen/dining duties", "whole audit-period register"), "whole_audit_period")


def _application(document, register, allocation, by_code, adjustment_open, issues):
    if document is None:
        return None
    reported = []
    offset = 0
    seen = set()
    in_table = False
    for line in document.text.splitlines(keepends=True):
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        is_table = line.lstrip().startswith("|")
        if is_table and cells[0].startswith("Class code"):
            in_table = True
        elif is_table and in_table and not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            if len(cells) != 3 or not re.fullmatch(r"[A-Z]-\d+", cells[0]) or not re.fullmatch(r"\d+", cells[1]) or not re.fullmatch(r"\d+(?:\.\d{1,2})?", cells[2]) or cells[0] in seen:
                issues.append(OpenItem("Application", "Malformed or duplicated application class row.", "Confirm the original reported code, employee count and payroll table.", (_source(document, "application"),)))
                return None
            reported.append(ApplicationClass(cells[0], int(cells[1]), Decimal(cells[2]), _reference(document, offset, offset + len(line), f"application class {cells[0]}")))
            seen.add(cells[0])
        offset += len(line)
    if not reported:
        issues.append(OpenItem("Application", "No valid reported class/payroll rows were found.", "Provide the employer's payroll split.", (_source(document, "application"),)))
        return None
    application_cents = {row.class_code: _cents(row.payroll, "Application") for row in reported}
    report_total = sum(application_cents.values())
    register_total = sum(_cents(row.wages, "Register") for row in register)
    difference = register_total - report_total
    pending = _cents(allocation.reconciliation.unresolved_total, "Unresolved register payroll")
    deltas = {code: _money(_cents(by_code.get(code, Decimal("0")), "Verified payroll") - application_cents.get(code, 0)) for code in sorted(set(by_code) | set(application_cents))}
    definitive = not any(line.status == "OPEN" for line in allocation.lines) and not adjustment_open
    if difference or sum(row.employees for row in reported) != len(register):
        issues.append(OpenItem("Application/register comparison", "The application payroll total or employee count conflicts with the payroll register.", "Confirm and correct the application; retain register wages without altering them to force agreement.", tuple(row.source for row in reported)))
    if not definitive or any(value != 0 for value in deltas.values()):
        issues.append(OpenItem("Application/classification comparison", "The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved.", "Confirm the evidence-backed classification changes and resolve pending employee decisions; the application is not classification authority.", tuple(row.source for row in reported)))
    return ApplicationComparison(tuple(reported), _money(report_total), _money(register_total), _money(difference), deltas, _money(pending), definitive)


def process_employer(
    guide_path: str | Path, employer_path: str | Path, interview_path: str | Path, *,
    files: EmployerFiles = EmployerFiles(),
) -> ProcessingResult:
    """Reread authoritative paths; return calculations/evidence without writing files.

    Adapters handle corroborated restaurant, legal-office and contractor duties.
    Unsupported contexts and ambiguous/missing evidence are OPEN, never guessed.
    """
    issues = []
    try:
        inputs = read_inputs(guide_path, employer_path)
    except InputError as exc:
        return ProcessingResult(open_items=(OpenItem("Input sources", str(exc), "Supply readable, valid authoritative source documents."),))
    try:
        interview = read_markdown(interview_path)
        interview_errors = ()
    except InputError as exc:
        interview = None
        interview_errors = (str(exc),)
        issues.append(OpenItem("Interview", str(exc), "Provide the preserved authoritative interview for house rules."))
    documents = {str(doc.path.relative_to(inputs.records_root)): doc for doc in inputs.records}

    def get(filename, expected_type):
        document = documents.get(filename)
        if not isinstance(document, expected_type):
            issues.append(OpenItem(filename, f"Required evidence {inputs.records_root / filename} is missing or has the wrong format.", "Provide the authoritative source at the configured location."))
            return None
        return document

    business = get(files.business, MarkdownSource)
    notes = get(files.notes, MarkdownSource)
    payroll = get(files.payroll, CSVSource)
    application = get(files.application, MarkdownSource)
    legal_office = bool(business and re.search(r"\bis (?:an? )?(?:[a-z0-9-]+ )?law office\b", " ".join(business.text.lower().split())))
    contractor = bool(business and re.search(r"\b(?:replaces roofs|(?:installs|performs) (?:roofing|siding)|roofing and siding contractor)\b", " ".join(business.text.lower().split())))
    homebuilding = bool(business and re.search(r"\bbuilds single-family houses\b", " ".join(business.text.lower().split())))
    courier = bool(business and re.search(r"\bruns same-day document and parcel delivery\b", " ".join(business.text.lower().split())))
    electrical = bool(business and re.search(r"\bdoes residential and light commercial wiring\b", " ".join(business.text.lower().split())))
    receipt_table = None if legal_office or contractor or homebuilding or courier or electrical else get(files.receipts, CSVSource)
    period = _period(business, issues)
    receipts = _receipts(receipt_table, period, issues)
    if payroll is None:
        return ProcessingResult(inputs=inputs, period=period, receipts=receipts, open_items=tuple(issues))
    try:
        register = records_from_csv(payroll)
    except AllocationError as exc:
        issues.append(OpenItem("Payroll register", str(exc), "Correct the authoritative register; no payroll total is invented."))
        return ProcessingResult(inputs=inputs, period=period, receipts=receipts, open_items=tuple(issues))
    evaluator = RuleEvaluator(inputs.guide, interview, source_errors=interview_errors)
    if electrical:
        if not register:
            issues.append(OpenItem("Payroll register", "An empty register cannot substantiate electrical employees or allowance totals.",
                "Supply the complete original payroll register.", (_source(payroll, "empty payroll register"),)))
            return ProcessingResult(inputs=inputs, period=period, open_items=tuple(issues))
        from electrical_processing import evaluate_electrical, combine_travel, employee_totals as electrical_totals
        from contractor_processing import compare_employee_application
        evaluated = evaluate_electrical(inputs, business, notes, payroll, register, period, evaluator,
            get(files.site_signins, CSVSource), interview, interview_errors, files)
        issues.extend(evaluated.open_items)
        result = _finish(inputs, payroll, period, receipts, register, evaluated.decisions, issues, application, interview, interview_errors,
            adjustments=evaluated.adjustments, adapted_adjustment_sources=evaluated.adapted_sources,
            proposals=evaluated.proposals, site_visits=evaluated.site_visits, evidence_open=evaluated.adjustments is None)
        comparisons, comparison_issues = compare_employee_application(result)
        return replace(result, owner_assessment=evaluated.owner, employee_totals=electrical_totals(result),
            travel_reconciliation=combine_travel(result, evaluated.separate_from_base) if evaluated.adjustments is not None else None,
            employee_comparisons=comparisons, unassigned_site_records=evaluated.unassigned_site_records,
            open_items=result.open_items + comparison_issues)
    if courier:
        if not register:
            issues.append(OpenItem("Payroll register", "An empty annual register cannot substantiate the documented courier employees or weekly monetary basis.",
                "Supply the complete authoritative register before confirming payroll totals.", (_source(payroll, "empty payroll register"),)))
            return ProcessingResult(inputs=inputs, period=period, open_items=tuple(issues))
        from courier_processing import evaluate_courier, employee_totals
        evaluated = evaluate_courier(inputs, business, notes, payroll, register, period, evaluator,
            get(files.routes, CSVSource), get(files.weekly_payroll, CSVSource), files)
        issues.extend(evaluated.open_items)
        result = _finish(inputs, payroll, period, receipts, register, evaluated.decisions, issues, application, interview, interview_errors,
            parts=evaluated.parts, proposals=evaluated.proposals,
            evidence_open=not evaluated.weekly_reconciliation.reconciled)
        return replace(result, weekly_results=evaluated.weekly_results, weekly_reconciliation=evaluated.weekly_reconciliation,
            employee_totals=employee_totals(result.allocation))
    if homebuilding:
        if not register:
            issues.append(OpenItem("Payroll register", "The empty payroll register cannot substantiate the documented homebuilding employees.",
                "Supply the complete original payroll register before confirming employee or combined payroll totals.", (_source(payroll, "empty payroll register"),)))
            return ProcessingResult(inputs=inputs, period=period, open_items=tuple(issues))
        from homebuilding_processing import evaluate_homebuilding, combine_payroll
        from contractor_processing import compare_employee_application
        evaluated = evaluate_homebuilding(inputs, business, notes, get(files.site_signins, CSVSource), payroll,
            register, period, evaluator, get(files.subcontractor_payments, CSVSource),
            get(files.certificates, CSVSource), interview, interview_errors, files)
        issues.extend(evaluated.open_items)
        result = _finish(inputs, payroll, period, receipts, register, evaluated.decisions, issues, application, interview, interview_errors,
            proposals=evaluated.proposals, site_visits=evaluated.site_visits,
            adjustments=evaluated.adjustments, adapted_adjustment_sources=evaluated.adapted_sources)
        comparisons, comparison_issues = compare_employee_application(result)
        return replace(result, governing_field=evaluated.governing_field, owner_assessment=evaluated.owner,
            combined_reconciliation=combine_payroll(result) if evaluated.adjustments is not None else None,
            unassigned_site_records=evaluated.unassigned_site_records, employee_comparisons=comparisons,
            open_items=result.open_items + comparison_issues)
    if legal_office:
        # Lazy import keeps the small evidence adapter separate while sharing
        # the established workflow models and finalization calculations.
        from legal_office_processing import evaluate_legal_office
        log = get(files.site_signins, CSVSource)
        office = evaluate_legal_office(inputs, business, notes, log, payroll, register, period, evaluator, files)
        issues.extend(office.open_items)
        return _finish(inputs, payroll, period, receipts, register, office.decisions, issues, application, interview, interview_errors,
                       proposals=office.proposals, site_visits=office.site_visits)
    if contractor:
        from contractor_processing import evaluate_contractor, compare_employee_application
        crew = get(files.crew_timesheets, CSVSource)
        log = get(files.site_signins, CSVSource)
        evaluated = evaluate_contractor(inputs, business, notes, crew, log, payroll, register, period, evaluator, files)
        issues.extend(evaluated.open_items)
        result = _finish(inputs, payroll, period, receipts, register, evaluated.decisions, issues, application, interview, interview_errors,
                         site_visits=evaluated.site_visits)
        comparisons, comparison_issues = compare_employee_application(result)
        return replace(result, roofing_days=evaluated.roofing_days, governing_field=evaluated.governing_field,
                       employee_comparisons=comparisons, unassigned_site_records=evaluated.unassigned_site_records,
                       open_items=result.open_items + comparison_issues)
    business_text = business.text.lower() if business else ""
    notes_text = notes.text.lower() if notes else ""
    context_text = business_text + "\n" + notes_text
    context_refs = tuple(_source(doc, "business description" if doc is business else "auditor field notes") for doc in (business, notes) if doc is not None)
    mapped_names = {files.business, files.notes, files.payroll, files.application, files.receipts}
    unmapped = [doc for name, doc in documents.items() if name not in mapped_names and not _adjustment_evidence(doc)]
    extra_columns = set(payroll.columns) - {"employee_id", "name", "position", "wages_paid"}
    if unmapped or extra_columns:
        issues.append(OpenItem("Unmapped employer evidence", "Additional source files or payroll columns are outside this adapter's schema and may change actual-duty findings.", "Review and map the additional evidence before assigning employee codes.", tuple(_source(doc, "unmapped evidence") for doc in unmapped) + ((_source(payroll, "unmapped payroll columns"),) if extra_columns else ())))
    restaurant = bool(re.search(r"\bis (?:an? )?(?:\d+-seat )?restaurant\b|\bthis restaurant\b", business_text))
    dining_observed = "kitchen" in notes_text and "dining room" in notes_text
    mixed_observed = "catering" in notes_text and "prepare" in notes_text and "serve" in notes_text and "venue" in notes_text and "restaurant shifts" in notes_text
    # This narrow adapter does not interpret individual exceptions or alternative
    # occupations. Any such evidence requires review, rather than a title match.
    exception = bool(re.search(r"\b(?:actual duties|misleading|bookkeep\w*|clerical|office|driver|roof\w*|siding|landscap\w*|nurs\w*|parking)\b", notes_text))
    # Business descriptions may legitimately mention customers' office events or
    # an outside accountant. Explicit employee-duty exceptions still need review.
    exception = exception or bool(re.search(r"\b(?:actual duties|misleading|bookkeep\w*|clerical)\b", business_text))
    negated_duties = bool(re.search(r"\b(?:no|not|never|without|unconfirmed|unknown)\b[^.!?\n]{0,60}\b(?:kitchen|dining room|restaurant shifts|prepare|serve|meal preparation|duties)\b", context_text))
    negated_industry = bool(re.search(r"\b(?:no|not|never)\b[^.!?\n]{0,30}\brestaurant\b", business_text))
    context_conflict = exception or negated_duties or negated_industry or bool(unmapped) or bool(extra_columns)
    if context_conflict:
        issues.append(OpenItem("Duty evidence requires review", "The supplied prose contains negated observations, employee duty exceptions or other occupations outside this adapter's supported restaurant context.", "Review actual duties and resolve exceptions before assigning a code; titles do not override those statements.", context_refs))
    timesheets_present = any("timesheet" in Path(name).stem.lower() for name in documents)
    no_timesheets = bool(re.search(r"\bno (?:employee )?timesheets (?:are available|exist|were kept)\b", context_text))
    positive_timesheets = bool(re.search(r"(?:^|[.!?]\s+)\s*(?:employee )?timesheets (?:are|were) (?:available|kept|provided)\b|\b(?:we|employer) (?:has|have|keeps|kept) (?:employee )?timesheets\b", context_text, re.M))
    sheets = True if timesheets_present or positive_timesheets else False if no_timesheets else None
    has_catering = any(_CATERING_POSITION.match(str(row.values.get("position", ""))) for row in payroll.rows)
    if has_catering and sheets is not False:
        issues.append(OpenItem("Employee timesheets", "No record confirms that employee timesheets are unavailable, or timesheet records are present; the verified mixed-duty rule requires no employee timesheets.", "Confirm timesheet availability and provide records or an authoritative no-timesheets statement.", context_refs))
    if has_catering and (timesheets_present or positive_timesheets) and no_timesheets:
        issues.append(OpenItem("Conflicting timesheet evidence", "Field notes deny available timesheets but a source or another statement indicates timesheets exist.", "Resolve the conflicting evidence before applying the no-timesheets rule.", context_refs))
    decisions = {}
    proposals = {}
    for employee, row in zip(register, payroll.rows):
        evidence = (employee.source, *context_refs)
        position = str(row.values.get("position", ""))
        if period is None or not restaurant or business is None or notes is None or context_conflict:
            decision = _pending("Confirm this employee's actual duties, restaurant industry and exact audit period; this adapter has no rule for other contexts.", evidence)
        elif _CATERING_POSITION.match(position):
            facts = RuleFacts(employee.employee_id, "restaurant", "catering_crew", period.start, period.end,
                              complete=bool(receipts and receipts.coverage_confirmed),
                              evidence_sources=(*evidence, *(receipts.sources if receipts else ())),
                              mixed_catering_restaurant_duties=mixed_observed,
                              employee_timesheets_available=sheets,
                              total_gross_receipts=receipts.total if receipts else None,
                              offsite_catering_receipts=receipts.offsite if receipts else None)
            guide_refs, verified_guide = _guide_refs(evaluator, ("CG-02", "CG-07", "CG-41", "CG-42"))
            decision = evaluator.evaluate("catering_receipts", facts) if verified_guide else _pending("The current guide's catering definitions differ from verified CG-02/CG-07/CG-41/CG-42; obtain auditor review.", facts.evidence_sources, guide_refs)
            if decision.status == "OPEN" and verified_guide and receipts and receipts.percentage is not None and sheets is not True:
                # Hypothetical prerequisites select a proposal only. The actual
                # decision, receipt coverage and allocation remain unchanged.
                candidate = evaluator.evaluate("catering_receipts", replace(facts, complete=True, employee_timesheets_available=False))
                if candidate.status == "CLASSIFIED" and candidate.class_code == "F-710":
                    confirmations = (
                        f"Employer must supply complete off-site catering and total gross receipts for {period.start.isoformat()} through {period.end.isoformat()}, including partial-month boundaries, confirming catering below 40% of total gross receipts.",
                        "Confirm this employee's mixed catering and restaurant duties and that no employee timesheets are available; provide an authoritative no-timesheets statement. If timesheets exist, obtain CG-07 review instead.",
                        "The assigned auditor must review the exact-period evidence, confirm the below-40% rule applies, and approve F-710 before these OPEN wages can enter verified allocations. The current monthly-receipts schema does not verify partial-month coverage automatically.",
                    )
                    proposals[employee.employee_id] = ClassificationProposal(
                        candidate.class_code, candidate.rationale_ref, employee.wages,
                        "Propose the entire wage basis under F-710 only if complete audit-period receipts confirm off-site catering below 40% of total gross receipts, the mixed-duty/no-timesheets practice applies, and the auditor approves. The supplied receipt ratio indicates this candidate but does not resolve the original OPEN evidence gaps. If complete receipts reach 40% or more, or employee timesheets exist, this proposal does not apply.",
                        confirmations, candidate.rule_sources, facts.evidence_sources)
        elif _RESTAURANT_POSITION.fullmatch(position) and dining_observed:
            decision = _direct_restaurant(evaluator, evidence)
        else:
            decision = _pending("Register title and supplied observations do not establish supported actual duties; obtain employee duty evidence or an applicable rule.", evidence)
        decisions[employee.employee_id] = decision
        if decision.status == "OPEN":
            issues.append(OpenItem(f"{employee.name} [{employee.employee_id}]", decision.reason, "; ".join(decision.required_confirmation), decision.evidence_sources + decision.rule_sources, proposals.get(employee.employee_id)))
    return _finish(inputs, payroll, period, receipts, register, decisions, issues, application, interview, interview_errors, proposals=proposals)


def _finish(inputs, payroll, period, receipts, register, decisions, issues, application, interview, interview_errors, *, proposals=None, site_visits=None, adjustments=None, adapted_adjustment_sources=(), parts=None, evidence_open=False):
    """Share the existing exact-cent allocation, comparison and reconciliation."""
    allocation = allocate_payroll(register, decisions) if parts is None else allocate_parts(register, parts, decisions)
    # Rebuild the register from the loaded raw rows, independently of emitted lines.
    independent = reconcile_payroll(records_from_csv(payroll), allocation.lines)
    if not independent.reconciled:
        raise AllocationError("Independent payroll reconciliation failed")
    adjuster = PayrollAdjuster(inputs.guide, interview, source_errors=interview_errors)
    # No monetary adjustment schema is adapted in this first restaurant path.
    # Use the existing component for the empty evidenced set and expose any
    # candidate documents as OPEN, without accepting unbound external claims.
    adjustments = adjustments if adjustments is not None else adjuster.evaluate_batch()
    for line in adjustments.lines:
        if line.status == "OPEN":
            issues.append(OpenItem(line.adjustment_id, line.reason, "; ".join(line.required_confirmation), line.evidence_sources + line.rule_sources))
    unadapted_adjustments = False
    for document in inputs.records:
        if _adjustment_evidence(document) and str(document.path) not in adapted_adjustment_sources:
            unadapted_adjustments = True
            issues.append(OpenItem("Unadapted adjustment evidence", f"{document.path} may contain adjustment evidence that has not been supplied as verified typed cases.", "Provide sourced subcontractor/travel cases before treating adjustment processing as complete.", (_source(document, "adjustment evidence"),)))
    cents = {code: _cents(amount, code) for code, amount in allocation.by_code.items()}
    for code, amount in adjustments.by_code.items():
        cents[code] = cents.get(code, 0) + _cents(amount, code)
    by_code = {code: _money(amount) for code, amount in sorted(cents.items())}
    comparison = _application(application, register, allocation, by_code, evidence_open or unadapted_adjustments or any(line.status == "OPEN" for line in adjustments.lines), issues)
    return ProcessingResult(inputs, period, receipts, register, decisions, allocation, adjustments, by_code, comparison, independent, tuple(issues), proposals or {}, site_visits or {})
