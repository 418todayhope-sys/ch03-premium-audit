# Class Code Assistant

Requires Python 3.10+ and its standard library.

## Audit report

Generate the report from current validated sources, CSVs, review state and the
unanswered question document:

```bash
python3 -B skills/class-code-assistant/audit_report.py \
  --review-state deliverables/classification-review.json \
  --codes-dir deliverables/codes \
  --questions deliverables/audit-questions.md \
  --output deliverables/audit-report.md
```

All paths are configurable. The report separates verified allocations, OPEN
payroll/payment basis and unapproved proposals, compares employer submissions,
and preserves employee/payment identities, citations and question links. See
[AUDIT_REPORT.md](AUDIT_REPORT.md) for validation, reconciliation, human-review
boundaries and limitations. Generation records no approvals.

## Audit confirmation questions

Generate the question document from validated CSVs/review state and fresh employer
processing, using configurable paths:

```bash
python3 -B skills/class-code-assistant/audit_questions.py \
  --review-state deliverables/classification-review.json \
  --codes-dir deliverables/codes \
  --output deliverables/audit-questions.md
```

Questions preserve named employees/payments, pay weeks, source-record coverage,
recorded priority calls and separate verified/OPEN/proposed treatments. All remain
unanswered; generation is not audit approval. See
[AUDIT_QUESTIONS.md](AUDIT_QUESTIONS.md) for inputs, coverage, error handling,
repeatability and limitations.

## Verified classification CSVs

Use `generate_codes.py` when CSV generation is requested. From the repository
root, supply current sources and separate output locations:

```bash
python3 -B skills/class-code-assistant/generate_codes.py \
  --guide "$AUDIT_GUIDE_PATH" \
  --interview "$AUDIT_INTERVIEW_PATH" \
  --all-employers "$AUDIT_EMPLOYERS_ROOT" \
  --output-dir deliverables/codes \
  --review-state deliverables/classification-review.json
```

Use `--employer "$AUDIT_EMPLOYER_DIR"` instead of `--all-employers` for one
employer. CSVs contain verified payroll only; OPEN wages, unresolved adjustment
basis and unapproved proposals remain in the required JSON review-state file
with evidence and reconciliation controls. See
[CSV_GENERATION.md](CSV_GENERATION.md) for the exact output contract,
validation, filename rules, rerun behavior and limitations.

## Unified execution preview

From the repository root, preview one employer using auditor-supplied locations:

```bash
python3 -B skills/class-code-assistant/preview.py \
  --guide /path/to/classification-guide.md \
  --interview /path/to/verified-interview.md \
  --employer /path/to/one-employer
```

Or preview every immediate nonhidden employer folder in a container:

```bash
python3 -B skills/class-code-assistant/preview.py \
  --guide /path/to/classification-guide.md \
  --interview /path/to/verified-interview.md \
  --all-employers /path/to/employer-folders
```

The command calls the existing `process_employer` workflow independently for each
selected directory. All six business paths are reused unchanged. Every invocation
rereads the supplied sources; there are no default snapshot locations or cached
result substitutions. The interview path is explicit because verified house rules
are authoritative inputs alongside the guide and employer records.

Text previews on stdout show verified class totals, employee payroll, OPEN wages,
unresolved adjustment payment basis, unapproved proposals, human questions, source
citations/SHA-256, reconciliation and employer-reported differences. Employee rows
show verified payroll including verified travel additions; original wages and
additions remain separate in the detailed data. Proposed money never enters
verified totals. An empty adjustment set is labeled NOT EVALUATED, rather than
asserting that no adjustments exist.

Add `--format json` for the same preview as structured data, including separate
wage/addition totals, original employee/part IDs, weekly dates, detailed controls,
adjustment rows and a deduplicated citation catalog. Decimal values are strings;
dates use ISO format. Citation IDs are local to each employer. Reconciliation
records retain their computed `reconciled` property; non-string control keys use
explicit key/value entries. No final CSVs, reports or other output files are written.

Use `--file payroll=wages.csv` to override any existing `EmployerFiles` filename;
repeat for distinct fields. Relative paths such as `records/wages.csv` and
`./wages.csv` are supported. All-mode overrides apply to every selected employer.
Absolute filenames, parent traversal and duplicate/unknown field overrides are
usage errors. All mode sorts folders, reports excluded root files/hidden entries,
includes malformed employer folders as errors, and reports duplicate directory
aliases. It does not search recursively for employers or merge their money totals.

Exit codes:

- `0`: preview completed with status OK or REVIEW; REVIEW still requires human action.
- `1`: source, execution or reconciliation error; valid employers remain in the preview.
- `2`: invalid command-line arguments.

Missing required shared sources stop the run explicitly. Missing base employer
files, malformed records or an unexpected employer exception produce an ERROR
entry without substituting zero payroll or another employer's result. Some missing
industry-specific evidence remains REVIEW under the existing conservative adapters.
Source authenticity/completeness and unsupported narratives still need auditor
review. Keep sources stable during a batch: there is no atomic snapshot or source
locking. Hashes identify the documents used for each employer.

See [EMPLOYER_PROCESSING.md](EMPLOYER_PROCESSING.md) for supported business schemas.

```bash
python3 -B skills/class-code-assistant/preview.py --help
python3 -B -m unittest discover -s skills/class-code-assistant/tests -v
```

## Input reader — Step 1

Requires Python 3.10+ and its standard library. The reader only loads and validates
source documents. Its CLI prints an input inventory to stdout.

From the repository root:

```bash
python3 -B skills/class-code-assistant/input_reader.py \
  --guide /path/to/classification-guide.md \
  --employers /path/to/employer-records

python3 -B -m unittest discover -s skills/class-code-assistant/tests -v
```

`--employers` can point to a single employer directory or a directory containing
any number of employer directories. Markdown (`.md`) and CSV (`.csv`) files are
discovered recursively in deterministic path order, without named employer lists
or assumptions about how many employers must exist. Other extensions are ignored.
There is no prescribed per-employer file list at this input-reading stage.

`read_inputs(guide_path, employer_records_path, *, money_columns=...)` returns an
`Inputs` object. `read_markdown(path)` and `read_csv(path, *, money_columns=...)`
can also read explicitly named files. Each document retains its `path` (including
the original filename) and decoded `text`, preserving BOMs and line endings.
Markdown documents expose paragraph-definition identifiers such as `CG-01` in
source order; references inside paragraph prose are not counted as definitions.
CSV documents expose `columns` and `rows`; every row has a starting physical
`line_number` and a `values` dictionary for later source citations.

Money values are constructed directly from strings with `Decimal`. Defaults are
`wages_paid`, `gross_pay`, `travel_allowance_paid`, `amount_paid`,
`dine_in_receipts` and `offsite_catering_receipts`. These are field names rather
than classification rules. CLI `--money-column total_compensation` adds a money
column; repeat the option for more columns. In Python, `money_columns` replaces
the default set; pass a union with `DEFAULT_MONEY_COLUMNS` to extend it.
Unconfigured fields remain strings, so new schemas must identify their money
columns explicitly. Money written inside Markdown remains source text.

The money input format is signed plain decimal dollars with zero, one or two
fractional digits (for example `0`, `12.3`, `12.34`, `-1.25`). Surrounding money
whitespace is ignored during conversion and retained in source text. Negative
entries are preserved for review; the reader makes no business decision about
them. Empty amounts, currency signs, thousands separators, scientific notation,
non-finite values and excess fractional digits are rejected without rounding.

Inputs must be UTF-8; UTF-8 BOMs and CRLF are supported. CSV uses comma delimiters,
standard quoting and unique nonblank headers without surrounding whitespace.
Rows must have the header's field count. Blank physical rows are ignored, and a
valid header with no data rows is accepted. Missing/unreadable sources, malformed
CSV, absent guide paragraph identifiers and an empty records directory raise
`InputError`. CSV errors include the source path and line, and money errors also
identify the column and original value. The CLI prints one contextual error to
stderr and exits nonzero without an inventory or traceback.

Each invocation rereads the supplied locations. The component has no source cache
or built-in snapshot path, employer names, classification, allocation or output-file
generation. `/home/maxg/insurance01-inputs` is a development snapshot only. A future
authoritative-source adapter can refresh documents from auditor-provided locations
and pass their paths to this reader; network retrieval is outside this step.
