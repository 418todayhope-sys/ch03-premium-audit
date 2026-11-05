# Employer audit confirmation questions

`audit_questions.py` generates the assignment's question document using existing
classification/payroll results, classification CSVs and the separate review state.
It requires Python 3.10+ and the standard library. It changes no classifications,
allocations, OPEN decisions, CSVs, source evidence or review-state JSON.

From the repository root:

```bash
python3 -B skills/class-code-assistant/audit_questions.py \
  --review-state deliverables/classification-review.json \
  --codes-dir deliverables/codes \
  --output deliverables/audit-questions.md
```

All three paths are configurable. This works for either a single-employer or
all-employer state produced by `generate_codes.py`; no employer names or answers
are built into the generator. If CSV generation used filename overrides, repeat
the same `--file FIELD=RELATIVE_PATH` arguments here. An absent or unsupported
source never falls back to a development snapshot.

## Input validation

The review state records the auditor-supplied guide, interview, employer selection
and source manifests. Every invocation rereads those locations, calls the existing
preview/processing APIs and requires current results to match the saved state.
Each selected employer needs one distinct CSV with the expected SHA-256, exact
schema, current guide references and engine-derived totals. Missing, changed,
unexpected or tampered inputs stop publication and require corrected inputs or
fresh CSV/review-state generation. Supplied copies of the CSV/state files may be
in other directories; the document identifies their actual supplied locations.

The generator checks source hashes/line spans and rechecks input bytes immediately
before publishing. Sources are not locked. A concurrent edit can abort the run;
stabilize the source set and rerun. This validation cannot authenticate employer
statements, prove an inventory complete or establish missing employee identities.

## Question construction and coverage

Questions are grouped by employee, subcontractor/payment subject, allowance
recipient, application, business context and policy applicability. Every original
employee and payroll part remains identifiable. Courier questions include all
pay-week dates, wage parts, resulting codes and inside ride dates. Subcontractor
questions retain individual invoice IDs, payment dates, names, certificate periods
and verified/OPEN/proposed amounts. Owner questions preserve election evidence.
An unknown audit period is explicitly requested rather than invented.

Existing OPEN findings are attached to the relevant employee/payment/application
question; repeated findings retain distinct coverage identifiers without duplicating
the question. Mixed headings explicitly distinguish verified calculations from
attached OPEN findings. Conditional treatments remain UNAPPROVED and outside CSV
totals. Employers confirm duties, money, dates, identity and record completeness;
auditors approve policy applicability and proposed treatment. A balanced control
or verified calculation is not confirmation or sign-off.

The renderer retains unattributed sign-in dates, blank IDs, visitor names and site
locations in the affected questions. It requests identification without assigning
those records to an employee. Conditional office-visit alternatives remain subject
to identity and rule-applicability confirmation.

Every employer section includes a collapsible evidence index. It maps every
review-state source citation and relied-upon physical CSV data row to question IDs,
with original locators, employee/payment/date fields, source locations and SHA-256.
It covers monthly receipt rows even where the engine cites only the whole summary,
and preserves detailed route/timesheet records without one repeated question per
row. Exact input data remain authoritative; diagnostic percentages are rounded to
two places for display only. The full index makes large record sets produce a
large Markdown file; renderers without HTML disclosure support may show it expanded.

Coverage requirements include employees, payroll parts, adjustments, every saved
finding/proposal, nonzero CSV classes, reconciliation controls, owner/receipt/
governing-code assessments, cited documents and physical records. Unmatched cited
records receive explicit OPEN record-review questions. Coverage measures an
unanswered confirmation request, not verified identity, authentic evidence or
resolution of an OPEN case. Manual review of meaning remains necessary.

## Recorded priorities

First-call choices are read from the current interview's explicit acknowledgement
by Nadia and matched to complete employer business names, allowing case/spacing
differences. Prefix/suffix matching and inferred aliases are excluded. Multiple
acknowledgements or ambiguous selected identities require human confirmation.
The expected acknowledgement wording is intentionally narrow; absent/unmatched
choices are reported for the auditor rather than replaced with a calculated rank.
Company names containing ambiguous list punctuation may need human clarification.
An incompletely matched list is withheld as a whole: splitting a compound company
name must not create a priority for a shorter, differently named employer. A
single-employer run may therefore need auditor confirmation of the broader call
list's scope.

Reasons use the existing structured certificate findings, verified additions,
unresolved payments, employee-level classification changes and submitted split.
The document identifies the acknowledged group without claiming an order between
its members or making it a universal priority policy for future employers.

## APIs and output behavior

`build_question_plan(state, native_results, guide, interview, *, files=...)` builds
structured questions and record coverage from already loaded inputs.
`coverage_gaps(plan)` recomputes uncovered requirements from retained questions.
`render_questions(plan)` refuses a plan with uncovered evidence.
`generate_questions(review_state, *, codes_dir, output, files=EmployerFiles())`
performs fresh-source/engine/CSV validation, writes the Markdown and returns its
SHA-256, per-employer question/source/record counts, uncovered requirements and
source-bound priority metadata. Use this full entry point for a validated run.

Only the question document is written. Output must be separate from current
sources, CSVs and review state; symlink files and differing existing operator work
are refused. Identical repeated runs reuse the existing document. New inputs or
changed generation logic require a new output location if the old document differs.
Publication uses the existing atomic single-file output helper and verifies bytes.

Exit `0` means the question document was generated with complete request coverage;
it does not settle OPEN findings or constitute human approval. Exit `1` reports
validation/publication errors; `2` reports invalid CLI arguments. No questions are
sent to employers or interview participants. Audit reports use the separate
[audit_report.py](audit_report.py) command described in [AUDIT_REPORT.md](AUDIT_REPORT.md).

Run the complete test suite from the repository root:

```bash
python3 -B -m unittest discover -s skills/class-code-assistant/tests -v
```
