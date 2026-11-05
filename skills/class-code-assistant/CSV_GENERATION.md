# Verified classification CSVs

`generate_codes.py` uses the unchanged `preview.run_preview` interface, which
rereads the supplied guide, interview and selected employer records and calls the
existing processing engine. Python 3.10+ and the standard library are sufficient.
No employer list, source location, classification answer or paragraph map is built
into the generator.

From the repository root, supply current authoritative paths and separate output
locations. Generate one employer:

```bash
python3 -B skills/class-code-assistant/generate_codes.py \
  --guide "$AUDIT_GUIDE_PATH" \
  --interview "$AUDIT_INTERVIEW_PATH" \
  --employer "$AUDIT_EMPLOYER_DIR" \
  --output-dir deliverables/codes \
  --review-state deliverables/classification-review.json
```

Or generate all immediate nonhidden employer folders:

```bash
python3 -B skills/class-code-assistant/generate_codes.py \
  --guide "$AUDIT_GUIDE_PATH" \
  --interview "$AUDIT_INTERVIEW_PATH" \
  --all-employers "$AUDIT_EMPLOYERS_ROOT" \
  --output-dir deliverables/codes \
  --review-state deliverables/classification-review.json
```

Both output paths are configurable and required. `--file FIELD=RELATIVE_PATH`
supports the same `EmployerFiles` overrides as the preview runner; all-mode
overrides apply to every selected employer. Run `generate_codes.py --help` for
options. Use separate output/review-state locations for separate runs or selections.

## CSV contract

Each filename is a lowercase ASCII slug of its employer directory name: spaces
and punctuation become hyphens. Thus the assignment's existing directory names
produce its six exact required CSV filenames. New employer directories work the
same way; empty slugs or colliding names are errors, without overwriting another
employer's CSV. Folder identity remains in review state independently of its slug.

Columns are exactly `class_code,payroll_allocated,rationale_ref`. Rows are sorted
by code, contain nonzero verified totals, and use US-dollar amounts with exactly
two decimal places, no thousands separators and no float conversion. Exact
integer-cent aggregation reuses the allocator's Decimal helpers and cannot round
under a caller's low-precision Decimal context. UTF-8 output uses LF newlines.

Each row combines ALLOCATED employee wages and VERIFIED payroll adjustments from
the engine, counted once. It excludes OPEN employee wages, unresolved adjustment
basis, verified nonpayroll exclusions and every unapproved proposal. The exact
`rationale_ref` comes from the supplied guide's unique definition of that code and
must agree with each contributing decision and its current source citation. A
general policy paragraph cannot replace a code-description paragraph. Unsupported,
missing, duplicate, stale or conflicting references block that employer's CSV and
are recorded as errors rather than fabricated values.

An entirely OPEN employer may produce a header-only CSV with REVIEW status and
its full unresolved payroll retained separately. A CSV's absence of a class or
employee is therefore not evidence that the employer has no payroll exposure.

## Checks and durable review state

Before publication the generator checks every available reconciliation and
independently sums employee parts to their register wages, verified wages and OPEN
amounts. It checks adjustment payment bases against payroll additions, nonpayroll
and unresolved amounts, and compares the combined verified class totals against
the processing engine. Each CSV is parsed again to validate its exact schema,
formatting, amounts and references. Published bytes are read back and checked.

Source manifests and citation hashes/line spans are checked against the current
files, with a final content-hash recheck before publication. This detects source
changes between processing and export; it does not authenticate the records or
lock sources. Keep the source set stable during a run. A source change detected
by the final hash recheck aborts the entire batch before publication and creates
no new review-state file; stabilize the sources and rerun. Prior outputs do not
become results of that failed invocation.

The required JSON review-state file preserves the complete unchanged engine
preview under `processing`: employee IDs/pay parts, OPEN wages, unresolved payment
basis, conditional proposals, human questions, source references/SHA-256,
application differences and all available reconciliation controls. Its `outputs`
list records each CSV's path, rows, verified total and SHA-256. A missing
adjustment evaluation stays NOT_EVALUATED, rather than becoming a verified zero.
Citation identifiers are local to each employer. Review state is a machine-readable
record for later reports, not `audit-report.md` or `audit-questions.md`.

`generate_csvs(guide, interview, *, employer=None, all_employers=None, output_dir,
review_state, files=EmployerFiles())` returns this persisted dictionary.
`build_rows(entry, guide_document)` validates engine controls, contributions and
guide references; `validate_csv(text, entry, guide_document)` validates rendered
CSV content. Those lower-level functions do not reread every employer source;
use `generate_csvs` for a source-validated run.

## Errors and review boundaries

Exit `0` means generation completed with OK or REVIEW, not audit approval. Exit
`1` means a source, processing, reconciliation, reference or output error; `2`
means invalid CLI arguments. Per-employer processing/validation errors suppress
that CSV while preserving other valid employers and the complete review state.
Shared missing-source errors yield no CSVs and a review-state error record.

Output destinations must be outside selected source directories and must not
replace the guide or interview. Differing existing outputs and symbolic-link
outputs are refused; byte-identical reruns reuse existing files. Differing files
require new output locations. Output conflicts are checked before publishing the
batch. Files are published atomically one at a time, not as a transaction across
all files. An I/O failure may leave a partial batch: require a successful command,
the review-state output list and matching CSV hashes before using the set. A
previous CSV outside the current successful output list is not a current result.

Verified-only CSVs may be incomplete while OPEN cases exist. Human confirmation
is still required for proposed treatments, ambiguous identity/duties, policy gaps
and application corrections. This generator does not resolve those questions,
approve a quote, produce audit Markdown, alter evidence or transmit anything.

Run the complete suite from the repository root:

```bash
python3 -B -m unittest discover -s skills/class-code-assistant/tests -v
```
