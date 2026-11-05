"""Reconcile base employee wages with verified decisions; retain OPEN amounts."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
import hashlib
import io
import re
from typing import Iterable, Mapping

from input_reader import CSVRow, CSVSource
from rule_evaluator import Decision, SourceReference


class AllocationError(ValueError):
    """Invalid money, duplicate payroll evidence, or unreconciled wage parts."""


@dataclass(frozen=True)
class PayrollRecord:
    employee_id: str
    name: str
    wages: Decimal
    source: SourceReference
    raw_record: CSVRow | None = None


@dataclass(frozen=True)
class PayrollPart:
    part_id: str
    employee_id: str
    wages: Decimal
    source: SourceReference
    scope: str = "whole_audit_period"


@dataclass(frozen=True)
class WageAllocation:
    employee: PayrollRecord
    part: PayrollPart
    wages: Decimal
    status: str
    class_code: str | None
    rationale_ref: str | None
    decision: Decision | None
    reason: str
    required_confirmation: tuple[str, ...]


@dataclass(frozen=True)
class Reconciliation:
    register_total: Decimal
    allocated_total: Decimal
    unresolved_total: Decimal
    difference: Decimal
    employee_differences: dict[str, Decimal]
    part_differences: dict[str, Decimal]

    @property
    def reconciled(self) -> bool:
        return self.difference == 0 and all(value == 0 for value in (*self.employee_differences.values(), *self.part_differences.values()))


@dataclass(frozen=True)
class AllocationResult:
    by_code: dict[str, Decimal]
    lines: tuple[WageAllocation, ...]
    reconciliation: Reconciliation


def _cents(value: Decimal, context: str) -> int:
    if not isinstance(value, Decimal) or not value.is_finite():
        raise AllocationError(f"{context}: wages must be a finite Decimal, got {value!r}")
    numerator, denominator = value.as_integer_ratio()
    cents, remainder = divmod(numerator * 100, denominator)
    if remainder:
        raise AllocationError(f"{context}: sub-cent wages {value!r}; no rounding policy is assumed")
    return cents


def _money(cents: int) -> Decimal:
    whole, fraction = divmod(abs(cents), 100)
    return Decimal(f"{'-' if cents < 0 else ''}{whole}.{fraction:02d}")


def _identifier(value: str, context: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise AllocationError(f"{context}: identifier must be a nonblank string without surrounding whitespace")
    return value


def _source_key(source: SourceReference) -> tuple:
    if not isinstance(source, SourceReference) or not isinstance(source.source, str) or not source.source.strip() or not isinstance(source.locator, str) or not source.locator.strip():
        raise AllocationError("Payroll evidence requires a source filename and record locator")
    return source.source, ("line", source.line_start) if source.line_start else ("locator", source.locator)


def _register(records: Iterable[PayrollRecord]) -> dict[str, PayrollRecord]:
    employees = {}
    sources = set()
    for record in records:
        employee = _identifier(record.employee_id, "Register employee")
        if employee in employees:
            raise AllocationError(f"{employee}: duplicate employee in payroll register")
        key = _source_key(record.source)
        if key in sources:
            raise AllocationError(f"{employee}: duplicate payroll register source record {key}")
        _cents(record.wages, f"{employee} at {record.source.source} {record.source.locator}")
        employees[employee] = record
        sources.add(key)
    return employees


def records_from_csv(
    table: CSVSource, *, employee_column: str = "employee_id",
    wages_column: str = "wages_paid", name_column: str = "name",
) -> tuple[PayrollRecord, ...]:
    """Adapt reader rows, selecting only base wages and retaining original evidence."""
    missing = {employee_column, wages_column}.difference(table.columns)
    if missing:
        raise AllocationError(f"{table.path}: missing required payroll columns: {', '.join(sorted(missing))}")
    text_lines = list(io.StringIO(table.text, newline=""))
    digest = hashlib.sha256(table.text.encode("utf-8")).hexdigest()
    records = []
    for index, row in enumerate(table.rows):
        employee = _identifier(row.values.get(employee_column), f"{table.path}:{row.line_number}")
        wages = row.values.get(wages_column)
        _cents(wages, f"{employee} at {table.path}:{row.line_number} column {wages_column}")
        end = table.rows[index + 1].line_number - 1 if index + 1 < len(table.rows) else len(text_lines)
        source = SourceReference(str(table.path), f"CSV line {row.line_number}", row.line_number, end, "".join(text_lines[row.line_number - 1:end]).rstrip("\r\n"), digest)
        records.append(PayrollRecord(employee, row.values.get(name_column, employee), wages, source, row))
    _register(records)
    return tuple(records)


def _decision_issue(decision: Decision | None, part: PayrollPart) -> str | None:
    if decision is None:
        return "Classification decision is missing."
    if not isinstance(decision, Decision):
        raise AllocationError(f"{part.employee_id}, part {part.part_id}: expected an evaluator Decision")
    if decision.status == "OPEN":
        return decision.reason or "Classification remains OPEN."
    if decision.status != "CLASSIFIED":
        return f"Classification status {decision.status!r} is not verified."
    if part.scope not in {"whole_audit_period", "whole_pay_week"} or decision.scope != part.scope:
        return f"Decision scope {decision.scope!r} does not verify payroll part scope {part.scope!r}."
    if not all(isinstance(value, str) and value.strip() for value in (decision.class_code, decision.rationale_ref, decision.rule, decision.reason)) or not decision.applicability:
        return "Classification decision lacks a code, rule, guide paragraph, reason or applicability evidence."
    if decision.required_confirmation:
        return "Classification still requires human confirmation."
    if not decision.rule_sources or not decision.evidence_sources:
        return "Classification decision lacks rule or supporting evidence references."
    for source in (*decision.rule_sources, *decision.evidence_sources):
        try:
            _source_key(source)
        except AllocationError:
            return "Classification decision contains incomplete source references."
    heading = re.compile(r"^\*\*" + re.escape(decision.rationale_ref) + r"\.\s+" + re.escape(decision.class_code) + r"\b")
    if not any(source.locator == decision.rationale_ref and isinstance(source.excerpt, str) and heading.match(source.excerpt) for source in decision.rule_sources):
        return "Classification code and guide paragraph are not supported by the decision's cited definition."
    return None


def reconcile_payroll(
    register: Iterable[PayrollRecord], lines: Iterable[WageAllocation],
) -> Reconciliation:
    """Independently reconcile emitted amounts globally and for every employee."""
    employees = _register(register)
    accounted = dict.fromkeys(employees, 0)
    allocated = unresolved = 0
    seen_parts = set()
    seen_sources = set()
    part_differences = {}
    for line in lines:
        employee = line.employee.employee_id
        if employee not in employees or line.part.employee_id != employee:
            raise AllocationError(f"{employee}: allocation does not match a register employee")
        if line.employee != employees[employee]:
            raise AllocationError(f"{employee}: allocation register source or wage record differs")
        key = _source_key(line.part.source)
        if line.part.part_id in seen_parts or key in seen_sources:
            raise AllocationError(f"{employee}: duplicate allocation part or source record")
        seen_parts.add(line.part.part_id)
        seen_sources.add(key)
        cents = _cents(line.wages, f"{employee}, allocation {line.part.part_id}")
        part_differences[line.part.part_id] = _money(_cents(line.part.wages, f"{employee}, source part {line.part.part_id}") - cents)
        if line.status == "ALLOCATED" and line.class_code and line.rationale_ref:
            allocated += cents
        elif line.status == "OPEN" and line.class_code is None and line.rationale_ref is None:
            unresolved += cents
        else:
            raise AllocationError(f"{employee}: inconsistent allocation status or classification fields")
        accounted[employee] += cents
    register_cents = {employee: _cents(record.wages, employee) for employee, record in employees.items()}
    total = sum(register_cents.values())
    return Reconciliation(
        _money(total), _money(allocated), _money(unresolved),
        _money(total - allocated - unresolved),
        {employee: _money(cents - accounted[employee]) for employee, cents in register_cents.items()},
        part_differences,
    )


def allocate_payroll(
    register: Iterable[PayrollRecord], decisions: Mapping[str, Decision],
) -> AllocationResult:
    """Allocate whole-register wages with decisions keyed by employee ID."""
    records = tuple(register)
    parts = tuple(PayrollPart(record.employee_id, record.employee_id, record.wages, record.source) for record in records)
    return allocate_parts(records, parts, decisions)


def allocate_parts(
    register: Iterable[PayrollRecord], parts: Iterable[PayrollPart],
    decisions: Mapping[str, Decision],
) -> AllocationResult:
    """Allocate evidenced, disjoint wage parts; decisions are keyed by part ID.

    Supplied parts must match each employee's register wages exactly. This function
    does not derive percentages, calculate pay-period wages, or classify employees.
    """
    employees = _register(register)
    grouped: dict[str, list[PayrollPart]] = {employee: [] for employee in employees}
    part_ids = set()
    sources = set()
    for part in parts:
        _identifier(part.part_id, f"{part.employee_id} payroll part")
        if part.employee_id not in employees:
            raise AllocationError(f"{part.employee_id}: payroll part has no register employee")
        key = _source_key(part.source)
        if part.part_id in part_ids or key in sources:
            raise AllocationError(f"{part.employee_id}: duplicate payroll part ID or source record")
        _cents(part.wages, f"{part.employee_id}, part {part.part_id}")
        part_ids.add(part.part_id)
        sources.add(key)
        grouped[part.employee_id].append(part)
    unknown = set(decisions).difference(part_ids)
    if unknown:
        raise AllocationError(f"Decision keys have no payroll part: {sorted(unknown)!r}")

    lines = []
    code_cents: dict[str, int] = {}
    for employee, record in employees.items():
        employee_parts = grouped[employee]
        missing_parts = not employee_parts
        if missing_parts:
            part_id = f"missing:{employee}"
            while part_id in part_ids:
                part_id = "_" + part_id
            part_ids.add(part_id)
            employee_parts = [PayrollPart(part_id, employee, record.wages, record.source)]
        elif sum(_cents(part.wages, employee) for part in employee_parts) != _cents(record.wages, employee):
            raise AllocationError(f"{employee}: payroll part wages do not reconcile to the register; no allocation result produced")
        for part in employee_parts:
            decision = decisions.get(part.part_id) if not missing_parts else None
            issue = "Payroll parts and classification decision are missing." if missing_parts else _decision_issue(decision, part)
            wages = _money(_cents(part.wages, employee))
            if issue is not None:
                confirmation = decision.required_confirmation if decision and decision.required_confirmation else (f"Auditor or employer must confirm {record.name} [{employee}], part {part.part_id}: {issue}",)
                lines.append(WageAllocation(record, part, wages, "OPEN", None, None, decision, issue, confirmation))
            else:
                code_cents[decision.class_code] = code_cents.get(decision.class_code, 0) + _cents(wages, employee)
                lines.append(WageAllocation(record, part, wages, "ALLOCATED", decision.class_code, decision.rationale_ref, decision, decision.reason, ()))
    lines = tuple(lines)
    reconciliation = reconcile_payroll(employees.values(), lines)
    if not reconciliation.reconciled:
        raise AllocationError("Allocated and unresolved wages do not reconcile to the payroll register")
    return AllocationResult({code: _money(cents) for code, cents in sorted(code_cents.items()) if cents}, lines, reconciliation)
