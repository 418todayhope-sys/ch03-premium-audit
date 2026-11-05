# Source-bound classification evaluator

`rule_evaluator.py` reuses the unchanged `input_reader.read_markdown`. Load sources
for each run with `RuleEvaluator.from_paths(guide_path, interview_path)`; neither
source path nor employer identity is built into the evaluator. Each instance binds
to the source text loaded for that run. A new factory call rereads both sources.

The implementation is a manually verified interpretation of four house practices,
not a system that invents rules from arbitrary prose. Each rule requires its guide
paragraphs and Nadia's relevant statements and applicability clarifications at the
recorded interview times. Missing, changed or ambiguous anchors leave that rule
OPEN. Fixed rule codes must also remain in their verified guide paragraphs,
and duplicate code or paragraph definitions remain OPEN. Missing source files
also produce OPEN decisions. A changed rule requires
auditor review and a corresponding implementation update.

| Internal rule name | Verified behavior | Applicability | Source references |
|---|---|---|---|
| `contractor_office_visits` | At most four site days: C-110. Five or more: evidenced unique governing field code carrying most payroll. Whole audit period. | Contractors' office employees; actual duties and complete site sign-in evidence. A law office or employer with no established field code does not acquire a contractor classification. | CG-02, CG-04; Nadia 06:03 PM, 06:10 PM, 09:06 PM; selected field code's actual guide paragraph. |
| `roofing_siding` | Fewer than 15 distinct roof days: R-320. At least 15: R-310. Whole audit period. | Field workers at a contractor performing **both roofing and siding in the audit period**. This does not settle a general homebuilder's classification. | CG-02, CG-07, CG-11, CG-12; Nadia 09:04 PM and the limiting clarification at 09:16 PM. |
| `courier_week` | At least two distinct ride days: T-610; zero or one: C-110. Whole Monday–Sunday pay week, without hours-based splitting. | Inside employees of courier employers; complete route and pay-week evidence. Zero days requires a complete log and the inside-duty evidence described by CG-04. | CG-02, CG-04, CG-07, CG-31; Nadia 09:05 PM. |
| `catering_receipts` | Off-site catering receipts at least 40% of total gross receipts: F-720; below 40%: F-710. | Conservatively limited to the interview case: restaurant catering staff also working restaurant shifts without employee timesheets. Both receipt amounts cover the same complete audit period. | CG-02, CG-07, CG-41, CG-42; the 09:02 PM question context and Nadia's 09:02 PM and 09:05 PM answers. |

Internal rule names are implementation identifiers, not fabricated CG identifiers.
Every returned `SourceReference` for a rule includes the supplied source filename,
locator, inclusive line span, exact excerpt and document SHA-256. A classified
decision's `rationale_ref` is the guide's original paragraph identifier for its
code; interview rules are cited separately, never mislabeled as guide paragraphs.

Call `evaluate(rule_name, RuleFacts(...))`. The caller must supply:

- A subject label, evidenced industry and role based on actual duties, and exact
  period start/end as `datetime.date` objects.
- `evidence_sources`: `SourceReference(filename, record_locator)` entries for
  business/duties, activity and any governing-code/receipt facts. These can be made
  from the input reader's document paths and CSV row line numbers.
- `complete=True` only after verifying that those records cover the whole relevant
  period. The evaluator cannot independently certify a caller's factual assertions.
- Calendar dates in `days` for the three activity rules. Duplicate records on one
  day count once; invalid/out-of-period dates remain OPEN. An explicit empty tuple
  with complete evidence represents zero days; `None` represents missing evidence.
- For office staff at five or more site days, `governing_field_code` and
  `governing_code_confirmed=True` only with evidence that it is the unique largest
  field class. The evaluator does not compute field payroll totals or resolve ties.
- `roofing_and_siding=True` only when both employer activities are evidenced in
  the audit period. A job title or employer name does not establish this fact.
- For catering, finite `Decimal` values in `total_gross_receipts` and
  `offsite_catering_receipts`. The total must be positive and off-site receipts
  must be within the total. The exact threshold comparison does not depend on
  Decimal context precision and does not calculate payroll allocations.
- Also confirm `mixed_catering_restaurant_duties=True` and
  `employee_timesheets_available=False`. This is a conservative implementation
  boundary taken from the question Nadia answered, not a claim that her answer
  explicitly prohibits all other catering treatments. CG-07 allows division with
  time records; applicability when such records exist remains OPEN for the auditor
  rather than overriding that paragraph with an unverified broad interpretation.

The return value is a `Decision` with status `CLASSIFIED` or `OPEN`, `class_code`,
`rationale_ref`, reason, rule sources, evidence sources, applicability boundaries
and whole-period/whole-week scope. CLASSIFIED is a supported code decision for
the supplied facts, not final audit sign-off. OPEN carries no code and no rationale
paragraph plus a subject-specific confirmation required from the auditor or
employer. Unknown rules remain OPEN, citing Nadia's 09:11 PM review instruction
when present. No candidate code is invented for an uncovered case.

This step does not automatically extract employer facts, resolve evidence conflicts,
apply owner/subcontractor/allowance rules, calculate payroll allocations or generate
final deliverables. Conflicting evidence must not be marked complete or a governing
code confirmed; uncertain facts stay OPEN for human review. No fixed employer list
or employee answers are present.

Run all synthetic reader and evaluator tests from the repository root:

```bash
python3 -B -m unittest discover -s skills/class-code-assistant/tests -v
```
