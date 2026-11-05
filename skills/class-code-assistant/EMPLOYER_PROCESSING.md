# Employer processing workflow

Use [preview.py](preview.py) for unified read-only execution from the command line:

```bash
python3 -B skills/class-code-assistant/preview.py \
  --guide /path/to/classification-guide.md \
  --interview /path/to/verified-interview.md \
  --all-employers /path/to/employer-folders
```

Replace `--all-employers` with `--employer` to select one directory. The CLI wrapper
rereads sources and calls the unchanged workflow below independently for every
employer. It prints a preview to stdout and preserves OPEN findings; it generates
no final deliverable files. [README.md](README.md) documents text/JSON output,
filename overrides, deterministic immediate-folder discovery and exit codes.

`employer_processing.py` adds in-memory restaurant/catering, legal-office, roofing/siding, homebuilding, courier and electrical paths without
changing the reader, evaluator, allocator or adjustment component. It never writes
allocations, CSVs, reports or source documents. Call:

```python
from employer_processing import EmployerFiles, process_employer

result = process_employer(guide_path, employer_directory, interview_path)
```

All paths come from the caller and are reread on every invocation. `EmployerFiles`
can change the relative filenames for business description, notes, application,
payroll, receipts, site sign-ins, crew timesheets, subcontractor payments, certificates,
routes and weekly payroll. The production modules contain no employer names, employee
IDs, current payroll answers or development-root paths.

The result retains loaded inputs, audit period, exact original payroll records,
Decimal receipt totals/percentage, employee decisions, base allocation, adjustment
result, verified totals by code, application comparison, independent register
reconciliation and OPEN questions. Legal-office results also retain observed
distinct visit dates and separate conditional classification proposals. Decisions retain source filename, locator,
line span, excerpt and SHA-256 through the existing source-reference type.

## Supported evidence schema

- Business description: an unambiguous `Audit period Month D, YYYY to Month D,
  YYYY`, and an affirmative description of a restaurant business.
- Payroll CSV: `employee_id,name,position,wages_paid`; amounts use the reader's
  exact Decimal parser. Additional columns require adapter review.
- Field notes: corroborating restaurant kitchen/dining observations for familiar
  meal-preparation/service roles. Catering/event roles additionally require
  observed food preparation, service at a venue, and restaurant shifts.
- Receipt CSV: `month,dine_in_receipts,offsite_catering_receipts`. Months must be
  unique, canonical `YYYY-MM`; all amounts must be nonnegative and total positive.
- Application Markdown: one class table with `Class code…`, employee count and
  payroll columns. Malformed or duplicate rows remain OPEN.

The restaurant-specific requirements above apply to the restaurant path. The
legal-office adapter below does not require a gross-receipts file and does not
apply catering rules.

This is a deliberately narrow evidence adapter, not a general natural-language
interpreter. An isolated title is insufficient. The business description and field
observations must corroborate the register role. Unknown roles/industries,
detected negations, employee duty exceptions, other occupations and unmapped
sources/columns require human review instead of a guessed code. New narrative
formats need a reviewed adapter; the current recognizers do not establish the
truth or completeness of arbitrary prose. Source authenticity and the employer's
record completeness remain auditor responsibilities.

## Catering rule and incomplete evidence

The existing `RuleEvaluator` applies Nadia's 40-percent rule for mixed restaurant
and catering duties **without employee timesheets**. Its integer-ratio comparison
is exact at the threshold. This workflow also checks current CG-02, CG-07, CG-41
and CG-42 wording against the verified definitions; moved, missing or changed
definitions require review.

Missing timesheet files do not prove that no employee timesheets exist. An explicit
no-timesheets statement is required for the narrow automated path, and conflicting
availability statements or supplied timesheets prevent that assumption.

Monthly receipts establish audit-period coverage automatically only for an audit
period spanning whole calendar months with exactly matching, complete monthly
rows. Partial-month boundaries require exact-date receipts or auditor evidence
explaining the summary's coverage; this adapter does not infer boundary receipts.
Available totals and percentage are retained as diagnostic calculations even when
coverage is OPEN. They cannot silently authorize a catering classification.

Money totals use integer cents converted to Decimal, preserving precision under a
caller's low Decimal context. The displayed percentage uses a local high-precision
Decimal division and may be recurring; classification uses the existing exact
comparison, not a rounded displayed percentage.

## Legal offices and noncontractor site visits

`legal_office_processing.py` handles an affirmative law-office business description,
the shared payroll/application schema, corroborating office observations and a
configurable `EmployerFiles.site_signins` CSV. Required sign-in columns are
`date,employee_id,name,site,signed_in_at`. Every original row reference is retained;
visits count distinct in-period dates rather than sign-in rows. Counts describe
observed dates in the supplied records, not an independent guarantee that all
activity was recorded.

CG-02/CG-04 support documented office/professional roles when the field notes
affirm office observations and no physical work outside the office. Ordinary court
and closing activities are accepted only in the documented context distinguishing
them from job sites. Missing/qualified/negated observations, unknown roles,
contradictory duties, extra source files or unmapped columns require review.
Complete CG-02/CG-04 wording is checked against the verified policy; changed or
moved definitions and added policy beneath headings stay OPEN.

The existing evaluator supplies the code catalog and source-bound contractor-rule
references, including Nadia's 09:06 PM applicability clarification. **No contractor
day threshold is applied to legal-office staff.** Every employee with a recorded
site exception remains OPEN at any visit count; no construction or governing field
code is inferred. Missing logs do not mean zero visits. Unknown log identities or
conflicting IDs/names make the log unreliable and keep classifications OPEN until
identity is resolved. Invalid dates, outside-period records and incomplete visit
details remain attached for confirmation.

`ProcessingResult.proposals[employee_id]` holds a `ClassificationProposal` separately
from the original evaluator `Decision` and the allocator. An OPEN question also
links its proposal through `OpenItem.proposed_treatment`. Where office duties and
the guide support it, the candidate is the entire employee wage basis under C-110,
conditional on legal/client-document activities and explicit auditor approval of
treatment. A candidate is never a final classification or a verified house rule.
Missing duty/guide support leaves the proposed code unset. Proposals preserve rule
and record references, reasoning and confirmation requests; they never contribute
to `by_code`, allocated wages or reconciliation a second time.

The shared finalization function retains the established allocation, independent
register reconciliation, adjustment handling and application comparison. This
extension leaves the four foundational modules and the restaurant evidence path
unchanged.

## Roofing/siding contractors

`contractor_processing.py` handles the documented dual roofing/siding contractor
schema. `EmployerFiles.crew_timesheets` selects a CSV with
`date,employee_id,name,job_id,work_type,hours`; work types are roofing, siding and
gutters. Dates must belong to the audit period, IDs/names must match the register,
and hours must be finite positive Decimal values no greater than 24 per row.
Unsupported work, missing records, identity conflicts and unmapped evidence stay
OPEN. Hours validate actual work evidence; no wage proration or hour allocation is
performed. Multiple jobs or rows on a date contribute only one roofing day.
Explicit missing/incomplete-record statements prevent the adapter from asserting
complete evidence even when all configured files exist.

Actual crew records establish field membership, independently of job titles. A
positive siding record with zero roofing dates supports a zero count; an absent
worker's timesheets do not. Physical-work records conflicting with documented
office duties require scope review. The existing `roofing_siding` evaluator assigns
the entire wage basis to R-310 at 15 or more distinct roofing dates, otherwise
R-320, only with verified dual-operation context and rule sources. Complete current
CG-02/CG-07/CG-11/CG-12 policy text is checked; new policy beneath a heading cannot
be silently discarded.

`ProcessingResult.governing_field` records field-worker code totals, member IDs,
source/rule references and the unique largest code. This stage excludes office
payroll and must have complete classified field membership; ties or unresolved
workers do not select a code. Office workers then use the existing contractor
sign-in evaluator. Affirmative estimator/bookkeeper observations must corroborate
their office roles; neither title supplies a classification on its own.
Singular role observations bind only when exactly one register employee holds that
role; additional unobserved employees require individual evidence. Conflicting
installation duties also prevent relying on the office observation. Governing
evidence retains all contributing field-decision records, including timesheet rows,
and dependent office decisions inherit those references.

`roofing_days` and `site_visits` retain distinct observed dates. Unmatched sign-ins
remain in `unassigned_site_records` and on the OPEN source-question list. No name
alias, nonemployee status or employee identity is assumed. For each office worker,
the adapter evaluates the existing rule at both the confirmed-date set and the
largest possible set including all unattributed dates. Only the same verified code
at both endpoints permits classification; a possible threshold crossing stays
OPEN. The hypotheses are bounds, not assertions that unattributed visits belong to
any worker. Record completeness/authenticity remains an auditor responsibility.

`employee_comparisons` compares each calculated code and wage amount against the
application. When it contains aggregate counts/amounts only, former employee codes
are inferred only if each code has exactly one matching headcount/wage subset and
those subsets form a complete disjoint partition. Every inferred assignment is
explicitly marked and requires employer confirmation. Ambiguous, missing or
search-limited mappings stay OPEN; titles are never used to fill former codes.
The search is bounded to 100,000 examined subsets. Source questions and inferred
application attribution remain separate from verified wage classification and do
not double-count payroll.
Impossible application headcounts are rejected before constructing subsets.

The original common allocator, independent reconciliation, adjustment component and
application totals comparison are reused. Previous employer paths are unchanged.

## Homebuilding employees and subcontractors

`homebuilding_processing.py` handles corroborated own-crew construction duties
under CG-02/CG-15. It does not apply the roofing/siding 15-day rule to homebuilding
or trade invoices. Office observations must corroborate the payroll role; negated
or contradictory duties, missing sign-in pages and unmapped evidence require review.
The existing contractor rule evaluates confirmed and possible distinct visit-day
bounds. An unattributed visitor is never assigned to an employee. When the bounds
cross the four/five-day threshold, the employee stays OPEN with a separate proposal.

The governing field code comes from verified field wages, excluding office staff
to avoid circular assignment. H-420 is established only when those wages exceed
even the full recorded competing subcontractor payment basis. Otherwise the code
is OPEN. This conservative evidence bound is not a new classification rule.

Configurable `EmployerFiles.subcontractor_payments` and `.certificates` default to
`subcontractor-payments.csv` and `insurance-certificates.csv`. Payment columns are
`date,subcontractor,work,invoice,amount_paid`; certificate columns are
`subcontractor,certificate_no,coverage_from,coverage_to`. Every row preserves its
original reference and raw reader record. Framing/drywall map to H-420 (CG-15),
roofing to R-310 (CG-11); unsupported work remains OPEN. Duplicate invoice IDs or
invalid monetary evidence prevent a partial confirmed combined total.
Empty payroll/payment tables cannot substantiate zero monetary basis in this
documented active-employer context. Empty sign-ins conflict with observed visits
and remain OPEN. Zero observed visits retain a reference to the full examined log.

The existing adjustment component excludes payments with an exactly named,
full-period certificate. A supplied inventory and documented certificate search
support Nadia's 60-percent rule for missing/expired full-period coverage, without
proration. A missing inventory is unknown evidence. Related but different names
are retrieved solely as OPEN review candidates, never accepted aliases. Conditional
60-percent proposals contribute no verified payroll; other identity discrepancies
require manual inventory review. The adapter is not an entity-resolution service.

`owner_assessment` checks the business record's filed-election assertion under
CG-05 against the register. It does not imply a separate election form was supplied.
Conflicting owner wages stay in the register and OPEN. No absent owner wage is
invented or subtracted.

Employee wages reconcile separately from all subcontractor payments. The latter
balance into verified additions, nonpayroll and OPEN payment basis.
`combined_reconciliation.confirmed_payroll` is register wages plus verified
subcontractor additions, including employee wages whose classification is OPEN.
It equals verified class totals plus OPEN employee wages. Unresolved subcontractor
payment basis and proposed additions remain separate. Missing/invalid critical
payment evidence leaves the combined reconciliation unset. Application differences
remain provisional while employees or adjustments are OPEN; employee-level former
codes retain the existing inferred count/wage attribution and confirmation requirement.

## Courier payroll by week

`courier_processing.py` reads configurable `EmployerFiles.routes` (default
`route-log.csv`) and `.weekly_payroll` (default `weekly-payroll.csv`). Required
columns are `date,route_id,driver_id,ride_along_id,stops` and
`week_start,week_end,employee_id,gross_pay`. The existing reader parses money into
Decimal; integer-cent sums avoid caller-context rounding. Inputs are reread on
every run, with no employer IDs, names, answers or development paths in the adapter.

The supported narrative describes same-day document/parcel delivery, a documented
number of van routes and operating days per week, a dispatch office/radio, an
affirmative exhaustive-route-log observation, and Monday-to-Sunday pay weeks.
Register driver roles require corroborating actual driving records. Dispatch and
bookkeeping roles use the documented office context and complete vehicle activity
records to establish inside duties. Negated observations, extra named duty prose,
manual/warehouse exceptions or unsupported roles remain OPEN. Recognizers cover
reviewed source formats; they are not a general natural-language duty interpreter.

Every inside employee's distinct ride dates are evaluated separately in each pay
week by the existing `courier_week` evaluator. Nadia's 09:05 PM statement and current
CG-02/04/07/31 definitions support the whole-week treatment: two or more days T-610,
zero or one C-110. Regular drivers use documented duties under CG-02/CG-31. No
annual ride-day threshold or time-ratio allocation substitutes for weekly evidence.

The adapter checks unique date/route records and the repeated route/day matrix
against the documented route count and days per week. Missing, conflicting or
duplicate route records keep affected weeks OPEN. Unmatched rider IDs remain
unattributed: their dates only bound possible additional inside ride days. Where
both bounds produce the same code it remains verified; otherwise a separate
conditional proposal uses only observed dates, pending identity/completeness
confirmation. Unmatched drivers and invalid dates require review. Zero-ride findings
cite the complete examined log, as well as relevant week rows. Record authenticity,
coverage and scheduling exceptions remain auditor responsibilities.

`weekly_results` retain employee IDs, Monday/Sunday dates, exact pay, raw payroll
row, distinct observed ride dates, route references, rule decision and separate
proposal. `decisions` are keyed by source-bound part ID on this path, rather than
annual employee ID. `employee_totals` aggregate verified codes and an `OPEN` bucket
for each employee. The existing allocator's `allocate_parts` handles these weekly
parts; the common finalizer independently reconciles them to the annual register.

`weekly_reconciliation` separately retains the original weekly total, each
employee's total/difference, missing and duplicate weeks, unmatched payment basis
and source errors. All calendar weeks require explicit rows, including zero-pay
weeks. A missing/duplicate/invalid employee partition or wage difference retains
that employee's entire register wages OPEN, without calculating residual weekly
pay. Original weekly diagnostics remain available. Orphan monetary rows are never
assigned a guessed employee, omitted from the raw control total, or mixed into
verified register wages; they prevent a definitive application comparison. Empty
annual registers return a source error without a fabricated reconciled zero basis.
Conditional proposals never contribute to verified totals or reconcile twice.

## Electrical duties and travel allowances

`electrical_processing.py` supports the reviewed residential/light-commercial
wiring narrative, corroborating shop/office and electrician field observations,
the existing configurable site-sign-in file, and register columns
`employee_id,name,position,wages_paid,travel_days,travel_allowance_paid`. Source
locations and filenames remain caller-supplied and are reread on each run. Unknown
columns, extra records, unsupported narrative formats and duty conflicts require
review; there are no employer names, IDs, answers or development paths in production.

Current complete CG-02/04/05/21 definitions are verified before classification.
An included owner requires matching business/register identity, explicit absence
of an exclusion election, named wire-pulling observations and consistent site
records. A later conflicting election statement keeps the owner's full recorded
wages OPEN; management descriptions on an application do not override field duties.
The named office administrator requires affirmative office-only observations and
no conflicting site visits. Missing sign-in pages, unmatched identities, additional
named duties in either prose source and collective duty exceptions require review.
No contractor-office threshold is substituted for resolving contradictory duties.

Each original allowance row becomes a native `TravelCase`. The existing
`PayrollAdjuster` applies CG-03 and Nadia's 06:05 PM $47/day rule, preserving the
09:09 PM zero-day exception. Before any addition, affirmative field evidence must
establish payment on top of wages and in its own register column; conflicting
inclusion statements in either business description or notes prevent verification.
Separate columns alone do not prove that amounts are additional.

A documented flat daily payment permits exact per-worker rate derivation from
the original total and day count. It is not an assumption of averaging: variable,
negated, contradictory or fractional-cent rates remain OPEN until daily amounts or
a supported rate are supplied. Valid integer day counts must also have no disclosed
incompleteness, omissions or estimates. That completeness gate applies even below
the cap, where the native adjustment component correctly requires no work code
for a full expense exclusion. Missing columns prevent a fabricated complete zero
adjustment set; missing/invalid counts are not zero days.

Zero-day positive allowances remain OPEN with separate native monetary proposals.
Confirmation questions cover the count and missing travel dates, payment purpose,
supporting records, potential inclusion in wages, and approval of the proposed work
code/treatment. Proposed inclusion never changes verified money. Original employee
IDs, raw allowance/day rows, guide paragraphs and interview timestamps remain bound
to the decision and adjustment. All register rows, including zero allowances, are
independently accounted for by the unchanged adjustment component.

`travel_reconciliation` keeps original wages, classified/OPEN wages, original
allowance basis, verified additions, expense exclusions and OPEN allowances separate.
`known_payroll` is original register wages plus verified additions; it equals code
totals plus any OPEN employee wages. If additional-payment evidence is established,
`cash_total` also checks wages plus original allowances against known payroll plus
excluded and OPEN allowances; otherwise this cash total remains unset. A balanced
reconciliation establishes accounting completeness, not approval of OPEN treatment.
`employee_totals` includes base wages and verified additions only; unresolved
allowances stay in `adjustments.reconciliation.unresolved_basis`. Application
comparisons remain provisional while any classification or adjustment is OPEN.

## Application comparison and reconciliation

The application is a comparison, not the authority for employee duties. Its total
and count are checked against the register, and each reported code is compared to
verified code totals. `verified_differences` means verified minus reported; when
payroll remains OPEN these differences are provisional. `definitive` requires no
OPEN employee statuses, OPEN adjustments or unadapted adjustment evidence, even if signed unresolved
amounts happen to net to zero. Evidence-backed differences remain on the employer
confirmation list rather than forcing the register or classification to agree.

`allocate_payroll` performs its normal reconciliation. The workflow separately
rebuilds records from the original loaded register table and calls
`reconcile_payroll` on the emitted lines. Every employee and the overall amount must
balance to the cent. The local integration test also reads the raw CSV with an
independent parser and checks a literal, hand-verified total.

The restaurant, legal-office, roofing/siding and courier paths invoke the adjustment component
for an empty evidence set. An empty result means no adjustments were evaluated; it is not a
certificate that none exist. Any candidate payment, travel or certificate source
is explicitly OPEN, and prevents a definitive comparison. The homebuilding and
electrical adapters supply source-bound subcontractor and travel cases internally; the existing standalone
adjustment component remains unchanged.

Missing critical sources or malformed inputs return OPEN source errors without
inventing zero payroll. Missing receipts or house-rule context leave catering
payroll OPEN while independently supported restaurant payroll can still allocate.

## Verification

```bash
python3 -B -m unittest discover -s skills/class-code-assistant/tests -v
```

Synthetic integration tests use unrelated names/IDs and temporary sources. The
local tests for all six employers additionally use `/home/maxg/insurance01-inputs`, or
`INSURANCE01_TEST_INPUTS` when supplied. It skips only when those development
snapshots or the preserved interview are unavailable. These test paths do not
configure the production workflow.
