"""Source-bound payroll additions with separate, unapproved OPEN proposals."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path
import re
from typing import Iterable

from input_reader import CSVRow, InputError, read_markdown
from payroll_allocation import AllocationError, PayrollPart, _cents, _decision_issue, _identifier, _money, _source_key
from rule_evaluator import Decision, RuleEvaluator, SourceReference, _reference


class AdjustmentError(AllocationError):
    """Invalid currency or duplicate monetary evidence in an adjustments batch."""


@dataclass(frozen=True)
class AuditPeriod:
    start: date
    end: date


@dataclass(frozen=True)
class SubcontractorPayment:
    payment_id: str
    subcontractor: str
    payment_date: date
    work: str
    amount: Decimal
    source: SourceReference
    decision: Decision | None = None
    raw_record: CSVRow | None = None


@dataclass(frozen=True)
class Certificate:
    certificate_no: str
    subcontractor: str
    coverage_from: date | None
    coverage_to: date | None
    source: SourceReference
    raw_record: CSVRow | None = None


@dataclass(frozen=True)
class SubcontractorCase:
    period: AuditPeriod
    payment: SubcontractorPayment
    certificates: tuple[Certificate, ...] | None = None
    search_complete: bool = False
    search_source: SourceReference | None = None


@dataclass(frozen=True)
class DailyAllowance:
    day: date
    amount: Decimal
    source: SourceReference
    raw_record: CSVRow | None = None


@dataclass(frozen=True)
class TravelAllowance:
    allowance_id: str
    employee_id: str
    name: str
    amount: Decimal
    travel_days: int | None
    source: SourceReference
    days_source: SourceReference | None = None
    days_complete: bool = False
    separate_from_base: bool | None = None
    decision: Decision | None = None
    raw_record: CSVRow | None = None
    daily_payments: tuple[DailyAllowance, ...] | None = None
    uniform_daily_amount: Decimal | None = None
    rate_source: SourceReference | None = None


@dataclass(frozen=True)
class TravelCase:
    period: AuditPeriod
    allowance: TravelAllowance


@dataclass(frozen=True)
class ProposedTreatment:
    payroll_added: Decimal | None
    nonpayroll: Decimal | None
    reason: str


@dataclass(frozen=True)
class AdjustmentLine:
    kind: str
    adjustment_id: str
    period: AuditPeriod
    input_record: SubcontractorPayment | TravelAllowance
    status: str
    payroll_added: Decimal
    nonpayroll: Decimal
    unresolved_basis: Decimal
    class_code: str | None
    rationale_ref: str | None
    proposal: ProposedTreatment | None
    reason: str
    required_confirmation: tuple[str, ...]
    rule_sources: tuple[SourceReference, ...]
    evidence_sources: tuple[SourceReference, ...]
    certificates: tuple[Certificate, ...] = ()


@dataclass(frozen=True)
class AdjustmentReconciliation:
    basis_total: Decimal
    payroll_added: Decimal
    nonpayroll: Decimal
    unresolved_basis: Decimal
    difference: Decimal
    record_differences: dict[tuple[str, str], Decimal]
    missing_records: tuple[tuple[str, str], ...] = ()

    @property
    def reconciled(self) -> bool:
        return not self.missing_records and self.difference == 0 and all(value == 0 for value in self.record_differences.values())


@dataclass(frozen=True)
class AdjustmentResult:
    lines: tuple[AdjustmentLine, ...]
    by_code: dict[str, Decimal]
    reconciliation: AdjustmentReconciliation


_SUBCONTRACTOR_ANCHORS = (
    ("06:12 PM", "A certificate of insurance covering the whole audit period. If a subcontractor can't show one, payments to them are added to the payroll at 60 percent."),
    ("06:12 PM", "A certificate that lapses partway through counts as no certificate at all, so we add the subcontractor's payments to payroll at 60 percent."),
    ("09:08 PM", "I have not had a certificate come back in a name that differs from the name on the payments, so I have no practice for deciding if it is the same subcontractor."),
    ("09:09 PM", "Yes, if the documentation is missing, it counts as no certificate and the payments are added to the payroll at 60 percent."),
)
_TRAVEL_ANCHORS = (
    ("06:05 PM", "A daily allowance paid to crews working out-of-town is left out of payroll up to forty-seven dollars per worker per day. Anything paid above that amount counts as payroll."),
    ("09:09 PM", "I have no clear practice for someone receiving a daily allowance with no out-of-town days. Propose how you would handle it and why, and mark it as an open item."),
)
_GUIDE_WORDING = {
    "CG-03": "**CG-03. Payroll.** Payroll is the gross remuneration paid to employees for the period: wages, salaries, commissions and bonuses. Expense reimbursements that the employer can document, such as travel and lodging costs, are not payroll.",
    "CG-06": "**CG-06. Subcontractors.** Payments to a subcontractor who does not carry workers' compensation insurance for its own workers may be treated as payroll of the employer, under the code for the work the subcontractor performed.",
}
_GUIDE = re.compile(r"(?m)^\*\*(CG-[0-9]+)\.")
_MESSAGE = re.compile(r"(?m)^\*\*([^*]+)\*\* · (?:Voice|Text) · ([0-9:]+ [AP]M)[ \t]*$")


def _amount(value: Decimal, subject: str) -> int:
    try:
        return _cents(value, subject)
    except AllocationError as exc:
        raise AdjustmentError(str(exc)) from exc


def _has_source(source: SourceReference | None) -> bool:
    try:
        _source_key(source)
    except AllocationError:
        return False
    return True


def _id(value: str, subject: str) -> str:
    try:
        return _identifier(value, subject)
    except AllocationError as exc:
        raise AdjustmentError(str(exc)) from exc


def _valid_period(period: AuditPeriod) -> bool:
    return isinstance(period, AuditPeriod) and type(period.start) is date and type(period.end) is date and period.start <= period.end


def _scaled(units: int, places: int) -> Decimal:
    whole, fraction = divmod(abs(units), 10 ** places)
    return Decimal(f"{'-' if units < 0 else ''}{whole}.{fraction:0{places}d}")


def _continuous_coverage(certificates: tuple[Certificate, ...], period: AuditPeriod) -> bool:
    covered = None
    for certificate in sorted(certificates, key=lambda item: item.coverage_from):
        if covered is None:
            if certificate.coverage_from <= period.start <= certificate.coverage_to:
                covered = certificate.coverage_to
        elif (certificate.coverage_from - covered).days <= 1:
            covered = max(covered, certificate.coverage_to)
        if covered is not None and covered >= period.end:
            return True
    return False


class PayrollAdjuster:
    """Manually verified policies bound to configured documents for one run."""

    @classmethod
    def from_paths(cls, guide_path: str | Path, interview_path: str | Path) -> PayrollAdjuster:
        documents = []
        errors = []
        for path in (guide_path, interview_path):
            try:
                documents.append(read_markdown(path))
            except InputError as exc:
                documents.append(None)
                errors.append(str(exc))
        return cls(*documents, source_errors=tuple(errors))

    def __init__(self, guide, interview, *, source_errors=()):
        self.catalog = RuleEvaluator(guide, interview, source_errors=source_errors)
        paragraphs = {}
        if guide is not None:
            matches = list(_GUIDE.finditer(guide.text))
            for index, match in enumerate(matches):
                end = matches[index + 1].start() if index + 1 < len(matches) else len(guide.text)
                paragraphs.setdefault(match.group(1), []).append(_reference(guide, match.start(), end, match.group(1)))
        messages = []
        if interview is not None:
            matches = list(_MESSAGE.finditer(interview.text))
            for index, match in enumerate(matches):
                end = matches[index + 1].start() if index + 1 < len(matches) else len(interview.text)
                if match.group(1) == "Nadia Brennan":
                    messages.append((match.group(2), interview.text[match.end():end], _reference(interview, match.start(), end, f"Nadia Brennan · {match.group(2)}")))
        self.rule_sources = {}
        self.source_errors = {}
        for kind, paragraph, anchors in (("subcontractor", "CG-06", _SUBCONTRACTOR_ANCHORS), ("travel", "CG-03", _TRAVEL_ANCHORS)):
            refs = []
            errors = list(source_errors)
            found = paragraphs.get(paragraph, [])
            if len(found) != 1:
                errors.append(f"guide paragraph {paragraph} is missing or ambiguous")
            else:
                refs.extend(found)
                if " ".join(found[0].excerpt.split()) != _GUIDE_WORDING[paragraph]:
                    errors.append(f"guide paragraph {paragraph} differs from the verified written policy; auditor review is required")
            for time, wording in anchors:
                found = [ref for stamp, body, ref in messages if stamp == time and wording in body]
                if len(found) != 1:
                    errors.append(f"Nadia's {time} source statement is missing, changed or ambiguous: {wording}")
                else:
                    refs.extend(found)
            self.rule_sources[kind] = tuple(refs)
            self.source_errors[kind] = tuple(errors)

    def _line(self, kind, case, reason, *, included=None, proposal=None):
        record = case.payment if kind == "subcontractor" else case.allowance
        record_id = record.payment_id if kind == "subcontractor" else record.allowance_id
        subject = record.subcontractor if kind == "subcontractor" else f"{record.name} [{record.employee_id}]"
        basis = _amount(record.amount, subject)
        certificates = (case.certificates or ()) if kind == "subcontractor" else ()
        evidence = [record.source]
        evidence.extend(certificate.source for certificate in certificates)
        evidence.append(case.search_source if kind == "subcontractor" else record.days_source)
        if kind == "travel":
            evidence.append(record.rate_source)
            evidence.extend(day.source for day in (record.daily_payments or ()))
        if record.decision is not None:
            evidence.extend(record.decision.evidence_sources)
        refs = self.rule_sources[kind]
        if included is not None and included > 0:
            refs += record.decision.rule_sources
        is_open = included is None
        return AdjustmentLine(
            kind, record_id, case.period, record, "OPEN" if is_open else "VERIFIED",
            _money(0 if is_open else included), _money(0 if is_open else basis - included),
            _money(basis if is_open else 0),
            record.decision.class_code if included is not None and included > 0 else None,
            record.decision.rationale_ref if included is not None and included > 0 else None,
            proposal if is_open else None, reason,
            (f"Auditor or employer must confirm {subject}, record {record_id}: {reason}",) if is_open else (),
            refs, tuple(ref for ref in evidence if _has_source(ref)), certificates,
        )

    def _common_issue(self, kind, case, record):
        _id(record.payment_id if kind == "subcontractor" else record.allowance_id, "Adjustment record")
        if kind == "travel":
            _id(record.employee_id, "Worker")
        cents = _amount(record.amount, "Adjustment input")
        if self.source_errors[kind]:
            return "Authoritative adjustment rule is not verified: " + "; ".join(self.source_errors[kind])
        if not _valid_period(case.period):
            return "Confirm the exact audit-period start and end dates."
        if not _has_source(record.source):
            return "Provide the original amount record's source filename and locator."
        if cents < 0:
            return "Negative payment/allowance corrections have no verified adjustment treatment; obtain auditor confirmation."
        return None

    def _classification_issue(self, record, included):
        subject = record.subcontractor if isinstance(record, SubcontractorPayment) else record.employee_id
        part = PayrollPart("adjustment", subject, _money(included), record.source)
        issue = _decision_issue(record.decision, part)
        if issue:
            return issue
        decision = record.decision
        definitions = self.catalog.code_sources.get(decision.class_code, [])
        if len(definitions) != 1 or definitions[0].locator != decision.rationale_ref or decision.rationale_ref in self.catalog.ambiguous_paragraphs or decision.class_code in self.catalog.code_errors:
            return "The documented work/employee classification is not uniquely supported by the configured guide."
        current = definitions[0]
        if not any(ref.source == current.source and ref.locator == current.locator and ref.sha256 == current.sha256 and " ".join(ref.excerpt.split()) == " ".join(current.excerpt.split()) for ref in decision.rule_sources):
            return "The classification decision does not cite the current guide definition and SHA-256; reread and verify its work code."
        return None

    def subcontractor(self, case: SubcontractorCase) -> AdjustmentLine:
        record = case.payment
        issue = self._common_issue("subcontractor", case, record)
        if issue:
            return self._line("subcontractor", case, issue)
        if type(record.payment_date) is not date or not case.period.start <= record.payment_date <= case.period.end:
            return self._line("subcontractor", case, "Confirm the payment date belongs to this audit period.")
        if not isinstance(record.subcontractor, str) or not record.subcontractor.strip():
            return self._line("subcontractor", case, "Confirm the payee's documented legal name.")
        if case.certificates is None:
            return self._line("subcontractor", case, "Certificate evidence is unavailable; confirm whether documents are genuinely missing.")
        if any(certificate.subcontractor != record.subcontractor for certificate in case.certificates):
            return self._line("subcontractor", case, "Certificate/payee names do not match exactly; confirm identity without assuming a name alias.")
        for certificate in case.certificates:
            if not _has_source(certificate.source) or type(certificate.coverage_from) is not date or type(certificate.coverage_to) is not date or certificate.coverage_from > certificate.coverage_to:
                return self._line("subcontractor", case, "Confirm certificate source and valid coverage-from/coverage-to dates.")
        if any(certificate.coverage_from <= case.period.start and certificate.coverage_to >= case.period.end for certificate in case.certificates):
            return self._line("subcontractor", case, "An exactly named certificate covers the entire audit period, including both endpoints.", included=0)
        if case.search_complete is not True or not _has_source(case.search_source):
            return self._line("subcontractor", case, "Document a complete certificate search before treating unavailable full-period proof as missing coverage.")
        if _continuous_coverage(case.certificates, case.period):
            return self._line("subcontractor", case, "Multiple partial certificates may show continuous coverage, but no confirmed rule permits stitching them into one full-period certificate; obtain auditor treatment.")
        basis = _amount(record.amount, record.subcontractor)
        included, remainder = divmod(basis * 3, 5)
        proposal = ProposedTreatment(_scaled(basis * 6, 3), _scaled(basis * 4, 3), "Proposed 60-percent payroll treatment; identity, classification and rounding must be confirmed before use.")
        if remainder:
            return self._line("subcontractor", case, "The exact 60-percent result contains fractional cents; confirm a rounding policy before treating it as payroll.", proposal=proposal)
        if included and (not isinstance(record.work, str) or not record.work.strip()):
            return self._line("subcontractor", case, "Confirm the documented work and applicable work code.", proposal=proposal)
        if included:
            issue = self._classification_issue(record, included)
            if issue:
                return self._line("subcontractor", case, issue, proposal=proposal)
        return self._line("subcontractor", case, "Missing or incomplete/expired full-period certificate: include 60 percent of payments under the documented work code; do not prorate coverage.", included=included)

    def travel(self, case: TravelCase) -> AdjustmentLine:
        record = case.allowance
        issue = self._common_issue("travel", case, record)
        if issue:
            return self._line("travel", case, issue)
        basis = _amount(record.amount, record.employee_id)
        if basis == 0:
            return self._line("travel", case, "No allowance was paid; no payroll addition or exclusion is required.", included=0)
        if record.separate_from_base is not True:
            return self._line("travel", case, "Confirm the allowance is additional to base wages; an amount already in base payroll cannot be added again.")
        if record.days_complete is not True or not _has_source(record.days_source) or type(record.travel_days) is not int or record.travel_days < 0:
            return self._line("travel", case, "Confirm a complete, documented nonnegative integer count of out-of-town days for this worker and audit period; missing evidence is not zero days.")
        if record.travel_days > (case.period.end - case.period.start).days + 1:
            return self._line("travel", case, "The documented day count exceeds the calendar days in this audit period; confirm the worker's day evidence and period.")
        if record.travel_days == 0:
            proposal = ProposedTreatment(_money(basis), _money(0), "Propose including the full allowance as payroll because no exclusion days are documented, pending auditor/employer confirmation; this is not a verified house rule.")
            return self._line("travel", case, "Nadia has no practice for a paid allowance with zero documented out-of-town days; confirm treatment and any missing travel evidence.", proposal=proposal)
        if record.daily_payments is not None and record.uniform_daily_amount is not None:
            return self._line("travel", case, "Provide one reconciled daily-payment basis or uniform-rate basis, rather than two potentially conflicting payment bases.")
        if record.daily_payments is not None:
            if len(record.daily_payments) != record.travel_days:
                return self._line("travel", case, "Provide one documented allowance amount for each out-of-town day, including days paid zero.")
            dates = set()
            daily_sources = set()
            paid_total = excluded = 0
            for day in record.daily_payments:
                if type(day.day) is not date or not case.period.start <= day.day <= case.period.end or day.day in dates or not _has_source(day.source):
                    return self._line("travel", case, "Confirm distinct in-period travel dates and original daily payment sources; do not apply a day's cap twice.")
                source_key = _source_key(day.source)
                if source_key in daily_sources:
                    return self._line("travel", case, "A daily payment source row is repeated; confirm the original daily evidence.")
                paid = _amount(day.amount, "Daily allowance")
                if paid < 0:
                    return self._line("travel", case, "Negative daily allowance corrections need auditor treatment.")
                dates.add(day.day)
                daily_sources.add(source_key)
                paid_total += paid
                excluded += min(paid, 4700)
            if paid_total != basis:
                return self._line("travel", case, "Daily payments do not reconcile to the original allowance total; confirm complete daily payment evidence.")
        elif record.uniform_daily_amount is not None:
            daily_amount = _amount(record.uniform_daily_amount, "Uniform daily allowance")
            if daily_amount < 0 or not _has_source(record.rate_source) or daily_amount * record.travel_days != basis:
                return self._line("travel", case, "Confirm a documented nonnegative uniform daily rate whose days-times-rate reconciles to the allowance total.")
            excluded = min(daily_amount, 4700) * record.travel_days
        else:
            return self._line("travel", case, "A period allowance total and day count do not establish daily payments; provide daily amounts or a documented uniform daily rate before applying the per-day cap.")
        included = basis - excluded
        if included:
            issue = self._classification_issue(record, included)
            if issue:
                return self._line("travel", case, issue, proposal=ProposedTreatment(_money(included), _money(excluded), "Proposed allowance calculation pending verified employee classification."))
        return self._line("travel", case, f"Exclude up to $47 for each of {record.travel_days} documented out-of-town days; add only the excess to payroll.", included=included)

    def evaluate_batch(
        self, subcontractors: Iterable[SubcontractorCase] = (), travel: Iterable[TravelCase] = (),
    ) -> AdjustmentResult:
        subcontractors, travel = tuple(subcontractors), tuple(travel)
        lines = tuple(self.subcontractor(case) for case in subcontractors) + tuple(self.travel(case) for case in travel)
        return summarize_adjustments(lines, expected_cases=(*subcontractors, *travel))


def _controls(entries):
    controls = {}
    seen_sources = set()
    workers = []
    for kind, period, record in entries:
        if kind == "subcontractor" and isinstance(record, SubcontractorPayment):
            record_id = record.payment_id
        elif kind == "travel" and isinstance(record, TravelAllowance):
            record_id = record.allowance_id
            _id(record.employee_id, "Worker")
        else:
            raise AdjustmentError("Adjustment kind does not match its original input record")
        key = kind, _id(record_id, "Adjustment record")
        try:
            source_key = _source_key(record.source)
        except AllocationError as exc:
            raise AdjustmentError(str(exc)) from exc
        if key in controls:
            raise AdjustmentError(f"{key}: duplicate adjustment ID or original monetary source row")
        if kind == "travel":
            for employee, prior_period in workers:
                same_worker = employee == record.employee_id
                overlap = _valid_period(period) and _valid_period(prior_period) and period.start <= prior_period.end and prior_period.start <= period.end
                if same_worker and (overlap or period == prior_period):
                    raise AdjustmentError(f"{employee}: duplicate/overlapping worker-period allowance total; the daily cap cannot be applied twice")
            workers.append((record.employee_id, period))
        monetary_sources = {source_key}
        if kind == "travel":
            monetary_sources.update(_source_key(day.source) for day in (record.daily_payments or ()) if _has_source(day.source))
        if monetary_sources.intersection(seen_sources):
            raise AdjustmentError(f"{key}: duplicate original monetary source row across adjustment cases")
        seen_sources.update(monetary_sources)
        _amount(record.amount, str(key))
        controls[key] = period, record
    return controls


def reconcile_adjustments(
    lines: Iterable[AdjustmentLine], *,
    expected_cases: Iterable[SubcontractorCase | TravelCase] | None = None,
) -> AdjustmentReconciliation:
    """Reconcile against independent input cases when supplied; ignore proposals."""
    lines = tuple(lines)
    if expected_cases is None:
        entries = ((line.kind, line.period, line.input_record) for line in lines)
    else:
        entries = []
        for case in expected_cases:
            if isinstance(case, SubcontractorCase):
                entries.append(("subcontractor", case.period, case.payment))
            elif isinstance(case, TravelCase):
                entries.append(("travel", case.period, case.allowance))
            else:
                raise AdjustmentError("Expected a subcontractor or travel input case for reconciliation")
    controls = _controls(entries)
    basis_total = sum(_amount(record.amount, str(key)) for key, (_, record) in controls.items())
    payroll = nonpayroll = unresolved = 0
    differences = {}
    for line in lines:
        key = line.kind, line.adjustment_id
        if key in differences:
            raise AdjustmentError(f"{key}: duplicate adjustment output")
        if key not in controls or controls[key] != (line.period, line.input_record):
            raise AdjustmentError(f"{key}: output does not match an original input case")
        basis = _amount(controls[key][1].amount, str(key))
        added = _amount(line.payroll_added, str(key))
        excluded = _amount(line.nonpayroll, str(key))
        pending = _amount(line.unresolved_basis, str(key))
        if line.status == "OPEN":
            if added or excluded or line.class_code is not None or line.rationale_ref is not None or not line.required_confirmation:
                raise AdjustmentError(f"{key}: OPEN records cannot contribute verified amounts or codes")
        elif line.status == "VERIFIED":
            if pending or line.proposal is not None or line.required_confirmation or added < 0 or excluded < 0:
                raise AdjustmentError(f"{key}: inconsistent verified adjustment fields")
            if added > 0:
                part = PayrollPart(line.adjustment_id, "adjustment", _money(added), line.input_record.source)
                issue = _decision_issue(line.input_record.decision, part)
                if issue or line.class_code != line.input_record.decision.class_code or line.rationale_ref != line.input_record.decision.rationale_ref:
                    raise AdjustmentError(f"{key}: unverified classification on a claimed payroll addition")
            elif line.class_code is not None or line.rationale_ref is not None:
                raise AdjustmentError(f"{key}: zero payroll addition cannot carry a classification")
        else:
            raise AdjustmentError(f"{key}: unknown adjustment status")
        differences[key] = _money(basis - added - excluded - pending)
        payroll += added
        nonpayroll += excluded
        unresolved += pending
    missing = tuple(key for key in controls if key not in differences)
    differences.update((key, _money(_amount(controls[key][1].amount, str(key)))) for key in missing)
    return AdjustmentReconciliation(_money(basis_total), _money(payroll), _money(nonpayroll), _money(unresolved), _money(basis_total - payroll - nonpayroll - unresolved), differences, missing)


def summarize_adjustments(
    lines: Iterable[AdjustmentLine], *,
    expected_cases: Iterable[SubcontractorCase | TravelCase] | None = None,
) -> AdjustmentResult:
    lines = tuple(lines)
    check = reconcile_adjustments(lines, expected_cases=expected_cases)
    if not check.reconciled:
        raise AdjustmentError("Adjustment amounts do not reconcile to their original monetary records")
    by_code = {}
    for line in lines:
        if line.status == "VERIFIED" and line.class_code is not None:
            by_code[line.class_code] = by_code.get(line.class_code, 0) + _amount(line.payroll_added, line.adjustment_id)
    return AdjustmentResult(lines, {code: _money(cents) for code, cents in sorted(by_code.items()) if cents}, check)
