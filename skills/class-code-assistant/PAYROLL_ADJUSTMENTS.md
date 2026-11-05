# Source-bound payroll adjustments

Load each run with `PayrollAdjuster.from_paths(guide_path, interview_path)` from
`payroll_adjustments.py`. This companion uses the existing reader, evaluator code
catalog, allocator money/decision checks and `SourceReference`; it does not modify
those components. It returns in-memory adjustments only and does not merge them
into final employer allocations or write deliverables.

`subcontractor(SubcontractorCase(...))` and `travel(TravelCase(...))` evaluate one
case. `evaluate_batch(subcontractors, travel)` evaluates and reconciles a collection.
`summarize_adjustments(lines, expected_cases=cases)` and
`reconcile_adjustments(lines, expected_cases=cases)` also accept previously
evaluated lines and independent original cases. Every record uses an
`AuditPeriod(start, end)`.

## Subcontractor payments

A `SubcontractorPayment` contains a unique payment ID, original payee name,
payment date, documented work, Decimal amount, original source reference and a
verified work-code `Decision` for positive payroll additions. A `Certificate`
retains its original number/name, coverage dates and source. Each may also retain
the reader's original `CSVRow` as `raw_record`.

Supply **candidate certificates for this payee**, not a global list of unrelated
vendors. Names must match exactly; no abbreviations, case folding or inferred
aliases establish legal identity. A mismatched candidate remains OPEN and all
candidate records remain attached. No candidates (`certificates=()`) means a
documented missing-certificate search; `None` means evidence is unavailable.
Missing proof requires `search_complete=True` and a `search_source` reference.

One exactly named certificate covering the entire period, inclusive of both
endpoints, excludes the payment. No exhaustive search is needed when full-period
proof exists. Without it, missing, expired, late-start or early-end coverage invokes
60 percent under the documented work code, without prorating by payment date or
uninsured days. Malformed/missing dates remain OPEN. A chain of partial certificates
that might establish continuous coverage remains OPEN: Nadia did not supply a rule
for stitching renewal documents together. Identity, missing-document and lapse
treatment cite CG-06 and Nadia's 06:12 PM, 09:08 PM and 09:09 PM statements.

## Travel allowances

A `TravelAllowance` represents **one worker's allowance total for one audit period**.
It contains a unique allowance ID, worker ID/name, Decimal amount, documented day
count, amount source, day-count source, completeness flag, whether the amount is
separate from base wages, and a verified employee classification for positive
excess. The day count must be an actual nonnegative integer, supported by records
for this worker and period, and cannot exceed its calendar length; absence of
evidence is not a count of zero. Worker and monetary record IDs must be nonblank
strings without surrounding whitespace; malformed IDs are rejected, not normalized.

Supply either `daily_payments`, a tuple of `DailyAllowance(day, amount, source)`
with exactly one amount per distinct documented travel day (including zero-paid
days), or `uniform_daily_amount` with its supporting `rate_source`. Daily dates
must belong to the audit period, their sources must be distinct, and their amounts
must reconcile to the allowance total. A uniform rate must reconcile exactly as
rate times days. Supplying both bases requires review. A period total and day count
alone remain OPEN: an unused exclusion on one day cannot offset another day's
excess. For example, $90 and $10 on two days excludes $57 and includes $43.

Exclude at most $47 of each day's payment. Add the remaining excess only under a
verified whole-period employee classification. Positive allowances with zero documented days stay
OPEN. A separate `ProposedTreatment` proposes full inclusion pending confirmation;
the proposal is never part of verified money or class totals. Zero allowance paid
has no monetary movement and creates no artificial open exposure. The rule cites
CG-03 and Nadia's 06:05 PM limit and 09:09 PM zero-day clarification.

`separate_from_base=True` must be evidenced before any positive allowance is treated
as a separate monetary basis. If it is already in gross base wages or its basis is
unknown, keep the case OPEN rather than adding it again or silently altering base
payroll. Multiple payments must first be assembled into one evidenced worker-period
total. Duplicate/overlapping totals for the same worker are rejected, so the daily
cap is never repeated on two allowance records for the same period. Multiple
employee codes require a verified treatment; this component does not invent an
allocation of allowance excess among them.

## Verified amounts, proposals and reconciliation

Each `AdjustmentLine` retains its exact original input object, certificates,
rule/evidence references, status and reason. Rule references include original
paragraph identifiers, interview time, line span, excerpt and document SHA-256.
Positive additions require a decision citing the current configured guide's code
definition, source filename and SHA-256. Stale code definitions stay OPEN. Decision
employee/period binding and truthful record completeness remain caller
responsibilities, as in the existing evaluator/allocator. Sources are provided as
evidence references and assertions, not independently authenticated certificates or
travel records.

VERIFIED lines have `payroll_added` and `nonpayroll`, zero `unresolved_basis`, and
no proposal. OPEN lines have zero verified portions, no assigned code, the full
original monetary basis in `unresolved_basis`, and a human confirmation request.
This unresolved basis is **not** a claim that the entire amount belongs in payroll.
Even when the arithmetic is known but the code is not, the whole case remains
pending; its calculated candidate can be shown separately as an unapproved proposal.

`AdjustmentResult.by_code` contains only verified additions, not base wages or
proposals. Its reconciliation checks:

```text
original monetary basis = verified payroll + verified nonpayroll + unresolved basis
```

Both record-level and global differences must be zero. `evaluate_batch` always
reconciles against its original input cases. When rechecking exported/in-memory
lines, supply `expected_cases` to detect omitted outputs, including zero-amount
records. Without that argument, reconciliation checks only the supplied lines and
cannot establish completeness. Unknown or changed input records are rejected.
Duplicate IDs or monetary
source rows, even under different labels or workers, are rejected. Daily payment
rows belong to only one adjustment case; its own aggregate may reference that same
row. Reusing a certificate or uniform-rate policy as
support for several distinct payments is allowed; certificates are not counted as
additional money. Return statuses express evidence approval; `reconciled=True`
alone means accounting balances, not that OPEN cases are resolved.

Amounts are finite Decimal values at exact cents; integer-cent arithmetic prevents
context rounding and no floats are used. If 60 percent creates fractional cents,
the case stays OPEN with the exact unrounded Decimal proposal (for example, $0.01
produces $0.006). No rounding policy is invented. Signed/negative correction
treatment is also OPEN pending auditor confirmation. These are deliberate limits.
Missing or changed source anchors prevent that policy from being verified. CG-03
and CG-06 must retain their verified written wording (ignoring whitespace); changed
wording requires auditor review. A new factory call rereads the configured source
documents. Paths and employer identities are never hard-coded.

Run the complete synthetic suite:

```bash
python3 -B -m unittest discover -s skills/class-code-assistant/tests -v
```
