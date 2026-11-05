# Base payroll allocation

`payroll_allocation.py` builds on the existing `CSVSource`, `CSVRow`, `Decision`
and `SourceReference` types. It does not modify the reader or evaluator. All
functions return in-memory objects and write no deliverables or source files.

## Whole-register wages

1. Read a payroll register with `input_reader.read_csv(path)`.
2. Convert its rows with `records_from_csv(table)`. Defaults are employee ID
   column `employee_id`, wage column `wages_paid`, and optional name column `name`;
   callers can configure these columns. Custom wage columns must be read as money
   by the existing reader. Only the selected base wage field is used.
3. Pass those `PayrollRecord` objects and a mapping of employee IDs to verified
   evaluator `Decision` objects to `allocate_payroll(register, decisions)`.

The adapter retains the original `CSVRow`, source filename, physical line span,
exact CSV excerpt and loaded-document SHA-256. Each allocation line retains that
employee record and the complete original decision, including its actual guide
paragraph, interview references, applicability and supporting evidence.

## Evidenced pay-period parts

For an employee whose classification changes by pay week, use
`allocate_parts(register, parts, decisions)`. A `PayrollPart` contains `part_id`,
`employee_id`, `wages`, `source` and `scope`. Each part must represent a disjoint,
evidenced wage record. Decision keys are part IDs. Weekly decisions require parts
with `scope="whole_pay_week"`; the default is `whole_audit_period`. A weekly
decision cannot allocate an entire annual register amount through the convenience
API. The function does not compute weekly wages, time proportions or splits.

Every employee's supplied parts must sum exactly to that employee's register wage.
Underpayment/overpayment partitions fail with `AllocationError`, even if errors
offset across employees. An employee with no parts remains wholly OPEN. Part IDs
and source-record identities must be unique; reusing a source row under a new
part ID is rejected. Do not supply both an annual wage and its weekly breakdown
as separate additive parts. One register row per employee is required; assemble
transactions into an evidenced register before calling this API.

The caller binds each verified decision to the correct employee and period. The
existing evaluator `Decision` carries scope but has no employee ID or period dates,
so the allocator cannot independently infer or certify that binding. It verifies
decision status, code/paragraph and references, absence of pending confirmation,
agreement of the code with its cited guide-definition heading, and agreement
between decision and part scope. It does not rerun classification
rules or infer a code from a job title, employee identity or employer name.

## OPEN wages and reconciliation

Missing decisions, evaluator OPEN decisions, incomplete verification metadata,
pending confirmations and scope mismatches remain OPEN. Their wage amounts never
enter class-code totals. Each OPEN line has no class code or rationale paragraph,
retains the original decision if present, and carries the existing confirmation
request or a subject-specific request for the auditor/employer.

`AllocationResult` exposes `by_code`, employee/part `lines`, and a `reconciliation`.
The latter contains `register_total`, `allocated_total`, `unresolved_total`,
`difference` (register minus allocated minus unresolved), `employee_differences`
and `part_differences` (source part minus emitted wage), plus a `reconciled` flag.
`reconcile_payroll(register, lines)` can independently check an emitted set of
lines; employer, employee and source-part differences must all be zero. This
catches shifts between two class codes even when the employee total still matches.
Duplicate IDs, duplicate source records, unknown employees/decision keys,
invalid money and unreconciled parts raise clear errors rather than silently
deduplicating, discarding wages or manufacturing balancing amounts.

## Cents and exclusions

Amounts are finite Python `Decimal` inputs and two-place `Decimal` outputs.
Aggregation uses exact integer cents internally so a caller's Decimal precision
cannot round large totals. No floating-point arithmetic is used. Exact-cent
values such as `1.2300` normalize to `1.23`. Fractional cents, including `1.235`,
are rejected: this base-wage stage requires no rounding, and no rounding policy
has been supplied. Zero wage lines and signed wage corrections remain auditable;
zero class totals are omitted from the aggregate map only.

Subcontractor payments and travel allowances are not added, excluded, adjusted or
otherwise interpreted here. The selected base wages are the entire reconciliation
control for this component. For example, the reader may retain a travel-allowance
column as evidence, but it does not change `wages_paid` or the base-wage total.

Run all synthetic tests from the repository root:

```bash
python3 -B -m unittest discover -s skills/class-code-assistant/tests -v
```
