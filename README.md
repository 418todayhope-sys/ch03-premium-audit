# Class Code and Premium Audit Assistant — INSURANCE-01

This reusable Agent Skill reads employer records, applies Linden Shore Mutual's
verified company rules, allocates payroll with Decimal, and produces classification
CSVs, confirmation questions and an audit report. Unsupported decisions remain
OPEN for human review. It calculates no rates or insurance premiums.

The Skill instructions are in
[skills/class-code-assistant/SKILL.md](skills/class-code-assistant/SKILL.md).
The CLI uses the same existing processing engine; another employer using a
supported evidence schema needs different input paths, not Python source edits.

## Setup

Use Python **3.10 or newer**. The runtime and unittest suite use only the Python
standard library, including `decimal`, `csv`, `json`, `hashlib`, `pathlib` and
`unittest`. No pip installation, virtual environment, API key or network service
is required. Verification for this checkout used Python 3.12.3 on Linux/WSL.

Open a Bash-compatible terminal at the repository root, where this README and
`skills/` are located. Check the interpreter:

```bash
python3 -B -c 'import sys; assert sys.version_info >= (3, 10), "Python 3.10+ required"; print(sys.version)'
```

`-B` avoids writing Python bytecode into the source tree. Paths may contain spaces;
keep the quotes used below. Bash and `mktemp` are used by the example shell setup;
the Python components themselves require neither Bash nor `mktemp`.

## Current sources and preserved development snapshots

For each new audit, obtain the authoritative source locations from the auditor.

| Input | Requirement |
| --- | --- |
| Classification Guide | Current readable UTF-8 Markdown with original `CG-xx` paragraph definitions. Use company rules; public manuals are not substitutes. |
| Interview evidence | Complete original Markdown export containing verified house practices, timestamps and applicability clarifications. Preserve original bytes and metadata. |
| Employer records | One employer directory, or a container of employer directories. Base files are `business-description.md`, `field-notes.md`, `payroll-register.csv` and `application.md`. |
| Supporting records | Activity, receipts, certificates, subcontractor payments, weekly payroll and travel evidence required by that business; see the schema reference below. |
| Original assignment | Retain as the output/scope authority. It is a human reference; the runtime does not parse its DOCX or extract a ZIP. |

Every invocation rereads the selected Guide, interview and employer records.
Question/report generation obtains their locations from the supplied review-state
file, rereads them, and rejects results that disagree with that state. There is no
automatic fallback to a development snapshot. Keep sources stable during a run;
SHA-256 checks detect changes but do not authenticate documents.

This workstation has local development snapshots at
`/home/maxg/insurance01-inputs/classification-guide.md` and
`/home/maxg/insurance01-inputs/employer-files/` (six employer folders, 34 records).
The original assignment, Guide and employer ZIP remain unchanged under
`/mnt/c/Users/PC/Downloads/`. These external files are not bundled into the
repository or guaranteed available on another computer. The preserved final
interview export is
[interviews/ch03-premium-audit-20261105-0222(1).md](<interviews/ch03-premium-audit-20261105-0222(1).md>).
The preserved repository deliverables are results from those snapshots, not a
source of classification answers for a new run.

Set these shell variables to current auditor-supplied locations:

| Variable | Meaning |
| --- | --- |
| `AUDIT_GUIDE_PATH` | Absolute path to the current Guide Markdown. |
| `AUDIT_INTERVIEW_PATH` | Absolute path to the complete original interview Markdown. |
| `AUDIT_EMPLOYER_DIR` | One selected employer directory. |
| `AUDIT_EMPLOYERS_ROOT` | Container holding employer directories for an all-employer run. |
| `AUDIT_OUTPUT_DIR` | Fresh output directory, outside authoritative sources. |

To reproduce the preserved six-employer development run on **this workstation**,
use the explicit snapshot configuration below. For another audit, replace the
source values with the auditor's current locations; these examples are not
authoritative defaults. The temporary output directory protects existing deliverables:

```bash
export AUDIT_GUIDE_PATH='/home/maxg/insurance01-inputs/classification-guide.md'
export AUDIT_INTERVIEW_PATH="$PWD/interviews/ch03-premium-audit-20261105-0222(1).md"
export AUDIT_EMPLOYERS_ROOT='/home/maxg/insurance01-inputs/employer-files'
export AUDIT_EMPLOYER_DIR="$AUDIT_EMPLOYERS_ROOT/patuxent-electric"
export AUDIT_OUTPUT_DIR="$(mktemp -d /tmp/insurance01-rerun.XXXXXX)"
```

## Preview one employer or every discovered employer

Preview one selected employer; this writes only to stdout:

```bash
python3 -B skills/class-code-assistant/preview.py \
  --guide "$AUDIT_GUIDE_PATH" \
  --interview "$AUDIT_INTERVIEW_PATH" \
  --employer "$AUDIT_EMPLOYER_DIR"
```

Preview all immediate nonhidden employer directories. With the development
configuration above, this discovers all six employers:

```bash
python3 -B skills/class-code-assistant/preview.py \
  --guide "$AUDIT_GUIDE_PATH" \
  --interview "$AUDIT_INTERVIEW_PATH" \
  --all-employers "$AUDIT_EMPLOYERS_ROOT"
```

Add `--format json` for structured stdout with Decimal amounts encoded as strings.
Discovery is sorted, does not recurse into nested employer containers, and keeps
employer identities/results separate. Root files and hidden entries are excluded
and reported; incomplete employer directories produce errors, not silent skips.

For a new employer, put its current records in a separate directory, set
`AUDIT_EMPLOYER_DIR` to that location, and run the first command. For a new batch,
change `AUDIT_EMPLOYERS_ROOT` and run the second. No employer list or answer table
needs editing. Existing adapters support restaurant/catering, legal offices,
roofing/siding contractors, residential homebuilders, couriers and electrical work.
This is a narrow evidence adapter: unknown duties, other industries and
unrecognized evidence need human review.

The base payroll schema is `employee_id,name,position,wages_paid`. CSVs must be
UTF-8, comma-delimited, correctly quoted and have unique nonblank headers and
consistent field counts. Currency is plain decimal dollars with at most two
fractional digits; dollar signs, thousands separators, scientific notation and
non-finite amounts are invalid. Negative inputs are retained for review, not
automatically accepted by every calculation. See
[EMPLOYER_PROCESSING.md](skills/class-code-assistant/EMPLOYER_PROCESSING.md) for
the exact supported narrative/activity schemas and supporting files.

Use `--file payroll=records/wages.csv` when a supported record has a different
relative filename. Repeat `--file FIELD=RELATIVE_PATH` for distinct fields, using
the same overrides in the CSV, question and report commands. All-employer
overrides apply to every selected folder. This changes filenames, not column
schemas or business rules. Absolute paths, parent traversal and unknown/duplicate
override fields are rejected. A new schema may require a separately reviewed
adapter; do not edit code or borrow another industry's rule to force a result.

## Regenerate the CSVs, review state, questions and report

Run these commands in order using the variables above. The regenerated set goes
into `AUDIT_OUTPUT_DIR`, leaving the repository's existing `deliverables/` untouched.

First generate all discovered employer CSVs and the required machine-readable state:

```bash
python3 -B skills/class-code-assistant/generate_codes.py \
  --guide "$AUDIT_GUIDE_PATH" \
  --interview "$AUDIT_INTERVIEW_PATH" \
  --all-employers "$AUDIT_EMPLOYERS_ROOT" \
  --output-dir "$AUDIT_OUTPUT_DIR/codes" \
  --review-state "$AUDIT_OUTPUT_DIR/classification-review.json"
```

For a single-employer deliverable set, replace `--all-employers
"$AUDIT_EMPLOYERS_ROOT"` with `--employer "$AUDIT_EMPLOYER_DIR"` and choose a
fresh output directory. Later commands infer that selection from the review state
and work for either mode.

Generate the unanswered confirmation questions from current sources and validated
CSVs/review state:

```bash
python3 -B skills/class-code-assistant/audit_questions.py \
  --review-state "$AUDIT_OUTPUT_DIR/classification-review.json" \
  --codes-dir "$AUDIT_OUTPUT_DIR/codes" \
  --output "$AUDIT_OUTPUT_DIR/audit-questions.md"
```

Generate the report using those same dependencies:

```bash
python3 -B skills/class-code-assistant/audit_report.py \
  --review-state "$AUDIT_OUTPUT_DIR/classification-review.json" \
  --codes-dir "$AUDIT_OUTPUT_DIR/codes" \
  --questions "$AUDIT_OUTPUT_DIR/audit-questions.md" \
  --output "$AUDIT_OUTPUT_DIR/audit-report.md"
```

The existing required outputs are:

| Location | Contents |
| --- | --- |
| `deliverables/codes/` | `annapolis-courier.csv`, `bay-crest-exteriors.csv`, `harbor-point-legal.csv`, `larkspur-lane-bistro.csv`, `patuxent-electric.csv`, `severn-homebuilders.csv`. |
| `deliverables/classification-review.json` | Verified-only scope, complete processing/source state, OPEN amounts, proposals, reconciliations, CSV rows/paths/hashes. |
| `deliverables/audit-questions.md` | Unanswered questions, payment/employee identifiers, recorded priorities, source/record coverage index. |
| `deliverables/audit-report.md` | Reported versus verified payroll/differences, every adjustment, evidence, human-review requirements, reconciliations and separate OPEN/proposed treatments. |

The regenerated set uses the same filenames under your chosen directory. CSV
filenames derive from employer folder slugs; conflicting/empty slugs are errors.
Each CSV has exactly `class_code,payroll_allocated,rationale_ref`, one nonzero
verified row per code, two-decimal payroll and the exact original Guide paragraph
defining that code. The JSON state is a required supporting artifact, not a
substitute for either Markdown deliverable.

See [CSV_GENERATION.md](skills/class-code-assistant/CSV_GENERATION.md),
[AUDIT_QUESTIONS.md](skills/class-code-assistant/AUDIT_QUESTIONS.md) and
[AUDIT_REPORT.md](skills/class-code-assistant/AUDIT_REPORT.md) for validation/API details.

## Interpret results and obtain human approval

- **VERIFIED**: current evidence supports the calculation/classification; this
  is not employer confirmation or final audit sign-off. Verified corrections
  remain in the report and CSVs even when another item for that employer is OPEN.
- **OPEN**: classification, identity, rule applicability or evidence needs human
  resolution. OPEN wages remain in register reconciliation but are excluded from
  verified CSVs. Unresolved payment basis is separate and is not automatically payroll.
- **PROPOSED**: a conditional, unapproved alternative with specific evidence and
  approval requirements. Never add it to verified totals. No supported proposal
  means no guessed treatment.

Employee payroll must reconcile to the cent: verified base wages plus OPEN wages
equal the register. Verified adjustments are then added once. Evaluated payments
equal payroll additions plus excluded/nonpayroll amounts plus unresolved payment
basis. Known payroll may include OPEN wages; it is not all verified/classified.
An absent adjustment check is NOT EVALUATED, not a verified zero. A negative
application difference caused by omitted OPEN wages is provisional, not a verified
wage reduction. Code transfers do not add the same wages a second time.

References preserve original filenames, employee/payment IDs, dates/pay weeks,
exact `CG-xx` identifiers, interview timestamps, line spans and SHA-256. Source IDs
are local to each employer. The questions' record index maps physical CSV rows to
confirmations. Hashes identify bytes; they do not establish authentic/complete
evidence, insurance coverage or employee identity.

The employer payroll/records contact confirms facts and supplies records. The
assigned human auditor decides policy applicability and approves proposed
treatments and application corrections. Capture confirmations without rewriting
original evidence, then rerun with supported current inputs. The report generator
validates the exact **unanswered** question document; edited/answered questions
are not an implemented approval ledger and will be rejected as changed.
Arithmetic balance and exit code 0 never approve an OPEN case.

## Errors, reruns and limitations

| Condition | Behavior / next action |
| --- | --- |
| Missing/unreadable base files, malformed CSV, invalid money | Contextual error; correct records/paths and rerun. Never substitute snapshots or zero payroll. |
| Missing activity evidence, changed rules, unknown duties, identity conflicts or unsupported scope | ERROR or OPEN/REVIEW depending on the adapter; obtain evidence and auditor decisions. No invented code. |
| One employer errors in a batch | Preview/CSV stages retain separate successful results and identify errors. Require a complete error-free CSV/review set before questions/report. |
| Current sources, CSVs or questions disagree with state | Stop dependent generation. Stabilize sources and regenerate the dependency chain into a fresh directory. |
| Identical rerun at the same paths | Identical output bytes are reused without changing output mtimes. |
| Changed results or different selection at occupied destinations | Differing outputs and symbolic-link output files are refused. Use fresh paths; preserve reviewed work. |
| New output directory | CSVs can match byte-for-byte; JSON/Markdown record new output paths and dependent hashes. Compare financial/evidence content separately from declared run metadata. |

Exit codes are `0` for successful OK/REVIEW generation, `1` for input, processing,
validation or publication errors, and `2` for invalid arguments. A CSV-stage
failure can leave valid neighboring CSVs or a partial set; only use a successful
current review state's output list with matching CSV hashes. Files publish
atomically one at a time, not as a batch transaction. There is no source locking
or atomic multi-file snapshot.

The adapters recognize limited schemas. There is no general inference engine,
automated stakeholder interview, remote source retrieval, certificate-issuer
lookup, approval ledger, rate/premium computation, deployment or submission. The
optional pinned Skill security scanner is not a runtime/test dependency and is
not installed here; tests/manual review do not constitute a successful security
scan. No publishing, synchronization or uploads are part of these commands.

## Verification

Run the complete suite from the repository root:

```bash
python3 -B -m unittest discover -s skills/class-code-assistant/tests -v
```

The suite includes portable synthetic fixtures. Real-output integration checks
also depend on the original local development locations and source paths in the
preserved review state. Their skip guards differ: some check the snapshot
directory/interview, while the report checks the recorded Guide. A present but
incomplete snapshot can fail tests rather than be skipped. A new machine must
supply current sources and regenerate outputs to verify its own audit; a
synthetic-only pass does not reproduce these six real files.

The temporary-output commands above provide the independent regeneration path.
Compare all six CSV bytes, the review state's complete `processing` object and
each CSV's rows/hash/total. In Markdown, account only for declared output-path
substitutions and hashes of relocated review/question artifacts. All monetary,
classification, OPEN/proposed, evidence and reconciliation content must remain
unchanged. Keep questions/report next to the review state to preserve relative links.

Verification on November 5, 2026: all 11 documented Python commands succeeded;
335 tests passed with no skips. All six regenerated CSVs matched byte-for-byte,
the complete processing state matched, and the JSON/questions/report matched
after only the output-path and dependent-hash substitutions described above.
Single-employer generation, identical reruns and a new synthetic employer with
custom filenames also passed. Partially unresolved employers retained their
verified corrections; original deliverables and evidence were unchanged.

CLI option help is available locally:

```bash
python3 -B skills/class-code-assistant/preview.py --help
python3 -B skills/class-code-assistant/generate_codes.py --help
python3 -B skills/class-code-assistant/audit_questions.py --help
python3 -B skills/class-code-assistant/audit_report.py --help
```

## Interview rule and preservation

**Interview rule.** You conduct the stakeholder interview yourself, and the
questions are yours. Do not connect a coding agent or any other AI to the
interview to run, script, or automate it. The interview transcript is assessed
together with the code; a project whose interview was run by an agent is not
scored. The course rule is to plan for at most three stakeholder conversations;
prepare thoroughly before each conversation.

Preserve one final complete original Markdown export per interview session under
`interviews/`, with its original contents and metadata. Do not rewrite overlapping
history into a new transcript. Preserve authoritative evidence, the existing
implementation and Entire capture. These instructions authorize local execution
only; do not commit, push, synchronize, deploy, submit or upload without a separate
explicit instruction.
