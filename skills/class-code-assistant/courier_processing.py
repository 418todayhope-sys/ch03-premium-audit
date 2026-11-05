"""Evidence-bound weekly courier processing; source uncertainty is never identity."""

from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from datetime import date, timedelta
from decimal import Decimal
import re

from contractor_processing import _GUIDE_WORDING as EXISTING_WORDING
from employer_processing import ClassificationProposal, OpenItem, _pending, _source
from input_reader import CSVRow
from legal_office_processing import _row_references
from payroll_allocation import PayrollPart, _cents, _money
from rule_evaluator import Decision, RuleFacts, SourceReference


@dataclass(frozen=True)
class WeeklyPayrollReconciliation:
    register_total: Decimal
    weekly_total: Decimal | None
    difference: Decimal | None
    employee_weekly_totals: dict[str, Decimal]
    employee_differences: dict[str, Decimal]
    missing_weeks: dict[str, tuple[date, ...]]
    duplicate_weeks: dict[str, tuple[date, ...]]
    orphan_total: Decimal
    source_errors: tuple[str, ...]

    @property
    def reconciled(self):
        return (self.weekly_total is not None and self.difference == 0 and not self.source_errors
            and not any(self.employee_differences.values()) and not any(self.missing_weeks.values())
            and not any(self.duplicate_weeks.values()) and self.orphan_total == 0)


@dataclass(frozen=True)
class WeeklyEmployeeResult:
    employee_id: str
    week_start: date
    week_end: date
    wages: Decimal
    part_id: str
    source: SourceReference
    raw_record: CSVRow
    ride_days: tuple[date, ...]
    route_sources: tuple[SourceReference, ...]
    decision: Decision
    proposal: ClassificationProposal | None = None


@dataclass(frozen=True)
class CourierEvaluation:
    parts: tuple[PayrollPart, ...]
    decisions: dict[str, Decision]
    weekly_results: tuple[WeeklyEmployeeResult, ...]
    weekly_reconciliation: WeeklyPayrollReconciliation
    proposals: dict[str, ClassificationProposal]
    open_items: tuple[OpenItem, ...]


_WORDING = {**EXISTING_WORDING,
    "CG-31": "**CG-31. T-610 Courier and delivery drivers.** Drivers of vans and light trucks delivering parcels and documents, and helpers who ride on the delivery vehicles."}
_NUMBERS = {name: number for number, name in enumerate(
    ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"))}


def _guide_refs(evaluator, identifiers):
    refs = tuple(ref for ref in evaluator.rule_sources["courier_week"] if ref.locator in identifiers)
    valid = all(sum(ref.locator == key for ref in refs) == 1 for key in identifiers)
    valid = valid and all(" ".join(ref.excerpt.split()) in (_WORDING[ref.locator], _WORDING[ref.locator] + " ## Class codes") for ref in refs)
    return refs, valid


def _day(value):
    try:
        result = date.fromisoformat(value)
        return result if result.isoformat() == value else None
    except (TypeError, ValueError):
        return None


def _week(day):
    return day - timedelta(days=day.weekday())


def _weeks(period):
    if period is None or period.start.weekday() != 0 or period.end.weekday() != 6:
        return ()
    return tuple(period.start + timedelta(days=offset) for offset in range(0, (period.end - period.start).days + 1, 7))


def _number(value):
    return int(value) if value.isdigit() else _NUMBERS.get(value)


def _payroll(weekly, register, expected, issues):
    employees = {employee.employee_id: employee for employee in register}
    sums = dict.fromkeys(employees, 0)
    seen = Counter()
    errors = defaultdict(list)
    source_errors = []
    rows = []
    orphan = 0
    valid = weekly is not None and set(weekly.columns) == {"week_start", "week_end", "employee_id", "gross_pay"}
    if not valid or not weekly.rows or not expected:
        source_errors.append("Complete nonempty weekly payroll and an audit period of whole Monday-to-Sunday weeks are required.")
        for key in employees:
            errors[key].append(source_errors[-1])
    total = None
    if valid:
        total = 0
        for row, ref in _row_references(weekly):
            values = row.values
            key, amount = values["employee_id"], _cents(values["gross_pay"], f"{weekly.path}:{row.line_number}")
            total += amount
            if key not in employees:
                orphan += amount
                reason = f"Weekly monetary row has an unattributed employee ID {key!r}; no identity is inferred."
                source_errors.append(reason)
                issues.append(OpenItem("Unattributed weekly payroll", reason, "Confirm the original payee identity and reconcile this amount to an authoritative register.", (ref,)))
                continue
            sums[key] += amount
            start, end = _day(values["week_start"]), _day(values["week_end"])
            if start not in expected or end is None or end != start + timedelta(days=6):
                errors[key].append(f"{ref.locator}: invalid, outside-audit or non-Monday-to-Sunday pay-week dates.")
                continue
            seen[key, start] += 1
            rows.append((key, start, end, values["gross_pay"], row, ref))
    missing = {key: tuple(start for start in expected if not seen[key, start]) for key in employees}
    duplicates = {key: tuple(start for start in expected if seen[key, start] > 1) for key in employees}
    differences = {key: _cents(employee.wages, key) - sums[key] for key, employee in employees.items()}
    for key in employees:
        if missing[key]:
            errors[key].append("Missing weekly payroll rows; missing zero-dollar weeks cannot be inferred.")
        if duplicates[key]:
            errors[key].append("Duplicate employee/pay-week rows require original-source correction.")
        if differences[key]:
            errors[key].append("Weekly gross pay does not reconcile to this employee's annual register amount.")
        if errors[key]:
            source_errors.extend(f"{key}: {reason}" for reason in errors[key])
            evidence = (employees[key].source, *((_source(weekly, "examined weekly payroll"),) if weekly else ()))
            issues.append(OpenItem(f"Weekly payroll {key}", " ".join(errors[key]),
                "Supply corrected complete weekly evidence; the register wage remains OPEN without invented residual pay.", evidence))
    register_total = sum(_cents(employee.wages, employee.employee_id) for employee in register)
    reconciliation = WeeklyPayrollReconciliation(_money(register_total), _money(total) if total is not None else None,
        _money(register_total - total) if total is not None else None,
        {key: _money(value) for key, value in sums.items()}, {key: _money(value) for key, value in differences.items()},
        missing, duplicates, _money(orphan), tuple(source_errors))
    return rows, errors, reconciliation


def _routes(log, register, expected, period, business_text, note_text, issues):
    employees = {employee.employee_id: employee for employee in register}
    rides = defaultdict(set)
    driving = defaultdict(set)
    unknown = defaultdict(set)
    references = defaultdict(list)
    week_errors = defaultdict(list)
    global_errors = []
    schedule = re.search(r"\b([a-z]+|[0-9]+) van routes ([a-z]+|[0-9]+) days a week\b", business_text)
    route_count, days_count = (_number(value) for value in schedule.groups()) if schedule else (None, None)
    if not route_count or not days_count or days_count > 7:
        global_errors.append("The documented route-count/days-per-week schedule is missing or unsupported.")
    exhaustive = re.search(r"(?:^|[.!?]\s+)(?:the )?route log lists every route day with its driver and anyone riding along\.", note_text)
    if not exhaustive:
        global_errors.append("An affirmative complete route-log observation is required; missing entries are not zero rides.")
    if re.search(r"\b(?:route|records?|pages|logs?)\b[^.!?]{0,100}\b(?:missing|incomplete|unavailable|lost|not complete)\b|\b(?:missing|incomplete|unavailable|lost)\b[^.!?]{0,100}\b(?:route|records?|pages|logs?)\b", note_text):
        global_errors.append("Explicitly incomplete route records prevent complete activity-day bounds.")
    valid = log is not None and set(log.columns) == {"date", "route_id", "driver_id", "ride_along_id", "stops"}
    if not valid or not log.rows:
        global_errors.append("Route records are missing, empty or have an unsupported schema.")
    matrix = defaultdict(lambda: defaultdict(set))
    seen = {}
    route_ids = set()
    if valid:
        for row, ref in _row_references(log):
            values = row.values
            day = _day(values["date"])
            if day is None or period is None or not period.start <= day <= period.end:
                global_errors.append("An invalid or outside-audit route date cannot be assigned to a payroll week.")
                issues.append(OpenItem("Route dates", global_errors[-1], "Confirm the route's original date and audit period.", (ref,)))
                continue
            start = _week(day)
            references[start].append(ref)
            route = values["route_id"]
            if not route.strip() or route != route.strip() or not re.fullmatch(r"[0-9]+", values["stops"]):
                week_errors[start].append("A route has invalid route/stops details; confirm the original entry.")
            route_ids.add(route)
            matrix[start][route].add(day.weekday())
            key = day, route
            if key in seen:
                reason = "Duplicate or conflicting date/route records require confirmation; count dates once and retain all rows."
                week_errors[start].append(reason)
                issues.append(OpenItem("Duplicate/conflicting routes", reason, "Confirm the authoritative route record, driver and rider.", (seen[key], ref)))
            seen[key] = ref
            driver, rider = values["driver_id"], values["ride_along_id"]
            if driver not in employees:
                week_errors[start].append("An unattributed driver identity requires confirmation; no employee alias is assumed.")
                issues.append(OpenItem("Unattributed route driver", week_errors[start][-1], "Confirm the original driver's payroll identity.", (ref,)))
            else:
                driving[driver, start].add(day)
            if rider:
                if rider not in employees:
                    unknown[start].add(day)
                    issues.append(OpenItem("Unattributed route rider", "A rider ID has no matching register employee; no identity is assigned.",
                        "Confirm whether the rider is a nonpayroll visitor or supply the correct employee ID.", (ref,)))
                else:
                    rides[rider, start].add(day)
                    if rider == driver:
                        week_errors[start].append("One route lists the same employee as driver and ride-along; confirm the actual role.")
    if route_count and len(route_ids) != route_count:
        global_errors.append("Observed distinct route IDs do not match the documented route count.")
    # A repeating route/day matrix is evidence of supplied-log completeness,
    # not permission to invent missing route identities or ride dates.
    patterns = Counter(tuple(sorted(days)) for routes in matrix.values() for days in routes.values() if len(days) == days_count)
    leaders = [pattern for pattern, count in patterns.items() if count == max(patterns.values())] if patterns else []
    pattern = leaders[0] if len(leaders) == 1 else None
    for start in expected:
        week_matrix = matrix[start]
        if not pattern or set(week_matrix) != route_ids or any(tuple(sorted(days)) != pattern for days in week_matrix.values()):
            week_errors[start].append("Incomplete or conflicting route/day coverage for this pay week; confirm all scheduled route records and any exceptions.")
    return rides, driving, unknown, references, global_errors, week_errors


def _driver(evaluator, evidence):
    refs, valid = _guide_refs(evaluator, ("CG-02", "CG-31"))
    if not valid or "T-610" in evaluator.code_errors:
        return replace(_pending("The current driver guide definition requires review.", evidence, refs), scope="whole_pay_week")
    return Decision("courier_documented_driver", "CLASSIFIED", "T-610", "CG-31",
        "Delivery business, documented driver duties and actual route-driving records support courier driver payroll.", (), refs,
        evidence, ("courier delivery business", "documented regular driver and actual route evidence"), "whole_pay_week")


def evaluate_courier(inputs, business, notes, payroll, register, period, evaluator, routes, weekly, files):
    issues = []
    expected = _weeks(period)
    context = tuple(_source(document, "business description" if document is business else "auditor field notes") for document in (business, notes) if document)
    business_text = " ".join(business.text.lower().split())
    note_text = " ".join(" ".join(line for line in notes.text.lower().splitlines() if not line.lstrip().startswith("#")).split()) if notes else ""
    context_errors = []
    if not notes or not re.search(r"(?:^|[.!?]\s+)dispatch office with\b", note_text) or "radio" not in note_text or not re.search(r"(?:^|[.!?]\s+)pay weeks run monday to sunday\.", note_text):
        context_errors.append("Corroborating dispatch-office/delivery observations and Monday-to-Sunday pay weeks are required.")
    mapped = {files.business, files.notes, files.payroll, files.application, files.routes, files.weekly_payroll}
    extra = [document for document in inputs.records if str(document.path.relative_to(inputs.records_root)) not in mapped]
    if extra or set(payroll.columns) != {"employee_id", "name", "position", "wages_paid"}:
        context_errors.append("Unmapped source files or payroll columns require actual-duty review.")
        context += tuple(_source(document, "unmapped evidence") for document in extra)
    prose = business_text + " " + note_text
    if re.search(r"\b(?:actual duties|misleading|contrary|instead|physical|roof\w*|siding|wiring|landscap\w*|nurs\w*|exclusively)\b", prose):
        context_errors.append("Exceptional or conflicting duties are outside this adapter's supported courier observations; obtain human review.")
    if re.search(r"\b(?:no|no longer|not|never|without)\b[^.!?]{0,65}\b(?:delivery|dispatch office|radio|pay weeks|dispatch|bookkeeping|driv\w*)\b", prose):
        context_errors.append("Negated business or office observations do not establish courier/inside duty applicability.")
    # Accept only the already-supported named dispatcher observations. An
    # additional named duty statement needs review, even if it omits a keyword
    # such as 'physical'. Titles and route rows cannot override that prose.
    for employee in register:
        name = re.escape(employee.name.casefold())
        observed = re.compile(r"(?:while i was there, )?the (?:other )?dispatcher,? " + name +
            r",? (?:was on the radio|left with the [a-z0-9_-]+ van and came back at noon)\.")
        remaining = observed.sub(" ", prose)
        if employee.name and employee.name.casefold() in remaining:
            context_errors.append("An individual employee statement is outside the supported dispatch observations; review the named duties before using register roles.")
            break
    if re.search(r"\b(?:bookkeeper|dispatcher|drivers?)\b[^.!?]{0,100}\b(?:warehouse|unload\w*|manual work|field work|works? outside)\b", prose):
        context_errors.append("Warehouse, manual or outside-work observations require duty review; no clerical or driver code is inferred from a title.")
    pay_rows, pay_errors, reconciliation = _payroll(weekly, register, expected, issues)
    rides, driving, unknown, route_refs, route_errors, week_errors = _routes(routes, register, expected, period, business_text, note_text, issues)
    guide_refs, guide_valid = _guide_refs(evaluator, ("CG-02", "CG-04", "CG-07", "CG-31"))
    employees = {employee.employee_id: employee for employee in register}
    decisions = {}
    parts = []
    results = []
    proposals = {}
    for key, start, end, wages, raw, ref in pay_rows:
        employee = employees[key]
        part_id = f"{key}@{start.isoformat()}#{raw.line_number}"
        role = str(employee.raw_record.values.get("position", "")).casefold()
        evidence = tuple(dict.fromkeys((employee.source, ref, *context,
            *((_source(routes, "examined audit-period route log"),) if routes else ()), *route_refs[start])))
        errors = context_errors + route_errors + week_errors[start] + pay_errors[key]
        if _cents(wages, key) < 0:
            errors = errors + ["Negative weekly pay requires confirmation of the correction's original work period."]
        facts = RuleFacts(key, "courier", "inside", start, end, complete=not errors,
            evidence_sources=evidence, days=tuple(sorted(rides[key, start])))
        proposal = None
        if role == "driver":
            decision = _driver(evaluator, evidence)
            if errors or not driving[key, start]:
                decision = replace(_pending(" ".join(errors) if errors else "No route-driving evidence substantiates this driver's weekly duties.", evidence, decision.rule_sources), scope="whole_pay_week")
        elif role in {"dispatcher", "bookkeeper"}:
            if driving[key, start]:
                errors = errors + ["A documented inside employee appears as a route driver; the ride-along rule does not resolve mixed driving duties."]
                facts = replace(facts, complete=False)
            lower = evaluator.evaluate("courier_week", facts)
            upper = evaluator.evaluate("courier_week", replace(facts, days=tuple(sorted(rides[key, start] | unknown[start]))))
            if errors or not guide_valid:
                decision = replace(_pending(" ".join(errors) if errors else "Current complete courier/clerical definitions require review.", evidence, guide_refs), scope="whole_pay_week")
            elif lower.status == upper.status == "CLASSIFIED" and lower.class_code == upper.class_code:
                decision = replace(lower, reason=f"Between {len(rides[key, start])} confirmed and {len(rides[key, start] | unknown[start])} possible distinct ride days; both bounds yield {lower.class_code}. " + lower.reason)
            else:
                decision = replace(_pending("Ride-day bounds or authoritative weekly rules do not establish one verified code. " + lower.reason + " " + upper.reason,
                    evidence, tuple(dict.fromkeys((*lower.rule_sources, *upper.rule_sources)))), scope="whole_pay_week")
            if decision.status == "OPEN" and not context_errors and guide_valid:
                hypothetical = evaluator.evaluate("courier_week", replace(facts, complete=True))
                if hypothetical.status == "CLASSIFIED":
                    proposal = ClassificationProposal(hypothetical.class_code, hypothetical.rationale_ref, wages,
                        "Conditional treatment using the observed ride dates only; confirm complete activity, identities, duties and weekly pay before use.",
                        decision.required_confirmation, hypothetical.rule_sources, evidence)
        else:
            decision = replace(_pending("The documented role does not establish supported courier-driver or inside duties; confirm actual work.", evidence, guide_refs), scope="whole_pay_week")
        if decision.status == "OPEN":
            if proposal is None:
                proposal = ClassificationProposal(None, None, wages, "No supported code is proposed until the missing or conflicting work/pay evidence is confirmed.",
                    decision.required_confirmation, decision.rule_sources, evidence)
            proposals[part_id] = proposal
            issues.append(OpenItem(f"{key} week {start}", decision.reason, "; ".join(decision.required_confirmation), evidence + decision.rule_sources, proposal))
        results.append(WeeklyEmployeeResult(key, start, end, wages, part_id, ref, raw,
            tuple(sorted(rides[key, start])), tuple(route_refs[start]), decision, proposal))
        if not pay_errors[key]:
            parts.append(PayrollPart(part_id, key, wages, ref, "whole_pay_week"))
            decisions[part_id] = decision
    for employee in register:
        if pay_errors[employee.employee_id]:
            key = f"annual:{employee.employee_id}"
            evidence = (employee.source, *context, *((_source(weekly, "unreconciled weekly payroll"),) if weekly else ()))
            decision = _pending(" ".join(pay_errors[employee.employee_id]), evidence, guide_refs)
            parts.append(PayrollPart(key, employee.employee_id, employee.wages, employee.source))
            decisions[key] = decision
            proposals[key] = ClassificationProposal(None, None, employee.wages,
                "Retain full register wages OPEN; review observed weekly results without inventing omitted pay or allocating an unreconciled partition.",
                decision.required_confirmation, guide_refs, evidence)
    return CourierEvaluation(tuple(parts), decisions, tuple(results), reconciliation, proposals, tuple(issues))


def employee_totals(allocation):
    cents = defaultdict(lambda: defaultdict(int))
    for line in allocation.lines:
        cents[line.employee.employee_id][line.class_code or "OPEN"] += _cents(line.wages, line.employee.employee_id)
    return {key: {code: _money(amount) for code, amount in sorted(codes.items())} for key, codes in cents.items()}
