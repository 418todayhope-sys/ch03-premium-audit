# Audit report generator

From the repository root, after generating verified CSVs/review state and the
unanswered question document:

```bash
python3 -B skills/class-code-assistant/audit_report.py \
  --review-state deliverables/classification-review.json \
  --codes-dir deliverables/codes \
  --questions deliverables/audit-questions.md \
  --output deliverables/audit-report.md
```

All four paths are configurable. Python 3.10+ and its standard library suffice.
The review state selects one employer or all discovered employers and records the
auditor-supplied guide, interview and employer locations. To use different source
locations, first invoke `generate_codes.py` with those paths, then generate the
corresponding questions. No cached development snapshot substitutes for a newly
supplied location. Use the same relative `--file FIELD=RELATIVE_PATH` overrides
as the CSV/question generation stages when required.

`audit_report.py` rereads the sources through `preview.py` and
`employer_processing.py`, requires exact agreement with the review state,
validates each supplied CSV's bytes, rows, guide references and totals, and
rebuilds the expected question document in memory using `audit_questions.py`.
It requires that supplied document to match exactly; it never creates, rewrites
or approves the question document. Edited answers require a separate approval
workflow; this generator handles the currently implemented unanswered document.

The report includes an employer conclusion, reported/verified class comparisons,
employee wages, supported individual coding changes, every payment/allowance,
weekly payroll detail, OPEN findings, unapproved alternatives, exact source
locators, original guide paragraphs, interview timestamps and file hashes. The
question links preserve the full dated record index and specific confirmation
prompts. Employee application assignments inferred by the engine are explicitly
marked; no individual reported code is invented when only aggregate reporting
exists. Recorded first-call choices are source-bound, not a new ranking policy.

ACCEPTED means the evidenced monetary/classification split matches; CORRECTED
means verified differences require correction; PARTIALLY UNRESOLVED means the
full split cannot yet be settled. All require employer fact confirmation and
auditor review. Conflicting total reported headcounts prevent acceptance even where
the dollar split matches. Verified zero/fully excluded payments display no payroll
allocation, rather than an OPEN code. Negative differences caused by omitted OPEN wages are provisional,
not verified wage reductions. VERIFIED calculations, OPEN wage basis, unresolved
payment basis and UNAPPROVED PROPOSED treatments remain separate.

Independent integer-cent controls resum the Decimal-backed engine contributions:

- Original wages plus verified additions equal verified classified payroll plus
  OPEN employee wages.
- Evaluated payment basis equals verified additions plus nonpayroll/excluded
  payments plus unresolved payment basis.
- Original wages plus evaluated payments equal verified payroll plus OPEN wages
  plus excluded payments plus unresolved payment basis.

Known payroll includes OPEN employee wages and is not all verified/classified.
Do not add payment basis or proposed payroll again. An absent adjustment evaluation
is NOT EVALUATED, not a verified zero. Owner exclusions never create a deduction
for wages absent from the register. Proposed sub-cent amounts retain their exact
precision until a human resolves rounding; verified values remain cents.

The employer payroll/records contact supplies identity, duty, period, payment and
coverage evidence. The auditor resolves policy applicability and approves any
proposed treatment. This report records no approvals and contacts nobody.

Missing/malformed/stale evidence, mismatched CSVs/state/questions, failed controls,
unknown source references and unsafe output locations stop publication with a
clear error (exit 1). Invalid CLI arguments exit 2; supported generation exits 0,
including unresolved cases. Outputs cannot replace evidence or dependencies.
Differing existing reports are preserved; use a new output location for changed
runs. Identical reruns reuse the same bytes without touching the output mtime.
Publication is atomic for the report file, with input hashes rechecked first.

Limits: existing evidence schemas only; no source locking, authenticated evidence,
atomic multi-file snapshot, approval ledger, certificate issuer lookup, rates or
premium calculation. New source evidence requires regenerated CSV/state/questions
before a report can reflect it. Preserve the original evidence and Entire capture;
generation authorizes no commits, synchronization, deployment or transmission.
