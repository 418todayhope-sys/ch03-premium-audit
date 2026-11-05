"""Conservative legal-office evidence adapter; no invented site-visit rule."""

from dataclasses import dataclass
from datetime import date
import io
import re

from employer_processing import ClassificationProposal, OpenItem, _adjustment_evidence, _pending, _source
from rule_evaluator import Decision, _reference


@dataclass(frozen=True)
class OfficeEvaluation:
    decisions: dict
    proposals: dict
    site_visits: dict
    open_items: tuple[OpenItem, ...]


_OFFICE_POSITION = re.compile(r"(?:associate attorney|attorney|paralegal|legal secretary|legal assistant|office manager|bookkeeper|receptionist)", re.I)
_GUIDE_WORDING = {
    "CG-02": "**CG-02. Assigning codes.** An employer is assigned the class code that describes its principal business. An employee whose work is described by another code in this guide is reported under that code. An employer may carry several codes.",
    "CG-04": "**CG-04. C-110 Clerical office employees.** Employees whose duties are confined to an office: correspondence, bookkeeping, dispatching by telephone or radio, drafting and estimating at a desk, and professional staff who work in the office.",
}
_NO_PHYSICAL_WORK = "no one on staff does physical work outside the office"
_PHYSICAL_ABSENCE_STATEMENT = re.compile(r"(?:^|[.!?]\s+)" + re.escape(_NO_PHYSICAL_WORK) + r"[.!?]")


def _row_references(table):
    lines = list(io.StringIO(table.text, newline=""))
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    for index, row in enumerate(table.rows):
        end = table.rows[index + 1].line_number - 1 if index + 1 < len(table.rows) else len(lines)
        yield row, _reference(table, offsets[row.line_number - 1], offsets[end], f"CSV line {row.line_number}")


def evaluate_legal_office(inputs, business, notes, log, payroll, register, period, evaluator, files):
    """Use actual legal-office observations and retain all site exceptions OPEN."""
    issues = []
    employees = {employee.employee_id: employee for employee in register}
    rows = {employee: [] for employee in employees}
    dates = {employee: set() for employee in employees}
    record_issues = {employee: [] for employee in employees}
    global_issues = []
    orphan_refs = []
    context_refs = tuple(_source(doc, "business description" if doc is business else "auditor field notes") for doc in (business, notes) if doc is not None)
    text = " ".join((business.text + " " + (notes.text if notes else "")).lower().split())
    note_text = " ".join(notes.text.lower().split()) if notes else ""
    observed = notes is not None and "office suite" in note_text and bool(_PHYSICAL_ABSENCE_STATEMENT.search(note_text))
    if re.search(r"\bcourt\b|\bclosings\b", note_text) and "neither is a job site" not in note_text:
        observed = False
    # Remove only a complete affirmative sentence, not a qualified or negated
    # occurrence of those words elsewhere in the corroborating documents.
    remaining = _PHYSICAL_ABSENCE_STATEMENT.sub(" ", text)
    negated_office = bool(re.search(r"\b(?:no|not|never|without|unknown|unconfirmed|unverified)\b[^.!?]{0,60}\b(?:office suite|office duties|professional duties|work in (?:the )?office)\b", remaining))
    if negated_office or re.search(r"\b(?:roof\w*|siding|landscap\w*|construction|carpentry|driver|metal fabrication|nurs\w*|parking|inspection|manual work|physical work|misleading|actual duties)\b", remaining):
        observed = False
        global_issues.append("Conflicting or unsupported actual-duty evidence requires review before relying on office observations.")
    if not observed:
        global_issues.append("Confirm observed office/professional duties, ordinary court/closing activities and the absence of physical field work; titles alone are insufficient.")
    mapped = {files.business, files.notes, files.payroll, files.application, files.site_signins}
    unmapped = [doc for doc in inputs.records if str(doc.path.relative_to(inputs.records_root)) not in mapped and not _adjustment_evidence(doc)]
    extra_columns = set(payroll.columns) - {"employee_id", "name", "position", "wages_paid"}
    if unmapped or extra_columns:
        global_issues.append("Unmapped employer source files or payroll columns may contain material duty evidence; review them before assigning codes.")
        orphan_refs.extend(_source(doc, "unmapped evidence") for doc in unmapped)
    guide_refs = tuple(ref for ref in evaluator.rule_sources["contractor_office_visits"] if ref.locator in _GUIDE_WORDING)
    guide_valid = "C-110" not in evaluator.code_errors and all(sum(ref.locator == identifier for ref in guide_refs) == 1 for identifier in _GUIDE_WORDING)
    # Validate all policy text. Only the known, empty structural section heading
    # may trail a paragraph; new headings and policy beneath them are not ignored.
    guide_valid = guide_valid and all(" ".join(ref.excerpt.split()) in (_GUIDE_WORDING[ref.locator], _GUIDE_WORDING[ref.locator] + " ## Class codes") for ref in guide_refs)
    if not guide_valid:
        global_issues.append("The current guide does not uniquely retain the verified CG-02/CG-04 office definitions; obtain source review.")
    if period is None:
        global_issues.append("Confirm the exact audit period before interpreting site activity.")
    log_valid = log is not None and set(log.columns) == {"date", "employee_id", "name", "site", "signed_in_at"}
    if not log_valid:
        global_issues.append("The site sign-in source is missing or its schema is unsupported; missing evidence cannot establish zero visits.")
    else:
        for row, ref in _row_references(log):
            employee = row.values["employee_id"]
            if employee not in employees:
                global_issues.append("A sign-in identity does not match a register employee; confirm original identity without assuming an alias.")
                orphan_refs.append(ref)
                continue
            rows[employee].append(ref)
            if row.values["name"] != employees[employee].name:
                record_issues[employee].append("Sign-in and payroll names conflict; confirm identity without assuming an alias.")
                global_issues.append("A sign-in ID/name identity conflict makes the log unreliable for identifying which employees visited; resolve it before treating anyone as unvisited.")
                orphan_refs.append(ref)
            try:
                day = date.fromisoformat(row.values["date"])
                if day.isoformat() != row.values["date"] or period is None or not period.start <= day <= period.end:
                    raise ValueError
                dates[employee].add(day)
            except (ValueError, TypeError):
                record_issues[employee].append("A sign-in date is invalid or outside the audit period; confirm the original record and relevant dates.")
            if not row.values["site"].strip() or not row.values["signed_in_at"].strip():
                record_issues[employee].append("Site or sign-in evidence is incomplete; confirm the recorded visit.")
    scope_refs = tuple(ref for ref in evaluator.rule_sources["contractor_office_visits"] if ref not in guide_refs)
    scope_refs += tuple(ref for ref in evaluator.fallback_sources if ref not in guide_refs and ref not in scope_refs)
    decisions = {}
    proposals = {}
    for employee in register:
        key = employee.employee_id
        evidence = tuple(dict.fromkeys((employee.source, *context_refs, *rows[key], *orphan_refs)))
        reasons = list(global_issues) + record_issues[key]
        role_supported = bool(_OFFICE_POSITION.fullmatch(str(employee.raw_record.values.get("position", ""))))
        if not role_supported:
            reasons.append("The register role is outside the corroborated legal-office schema; confirm this employee's actual duties.")
        if rows[key]:
            reasons.append(f"{len(dates[key])} distinct in-period site-visit dates are recorded. Nadia's sign-in practice is for contractors' office staff; no verified application exists for this legal office without a field code. Do not apply the contractor threshold or invent a field classification.")
            if evaluator.source_errors["contractor_office_visits"]:
                reasons.append("The authoritative scope source is not verified: " + "; ".join(evaluator.source_errors["contractor_office_visits"]))
        if reasons:
            reason = " ".join(dict.fromkeys(reasons))
            confirmations = (
                f"Confirm {employee.name} [{key}]'s actual work during every recorded site visit, including whether it was legal/client-document work or physical/inspection work.",
                "Confirm the complete audit-period log and resolve any identity, date or duty-evidence conflicts.",
                "Nadia or the auditor must approve treatment under CG-04 for legal-office visits; the contractor day-count threshold supplies no answer here.",
            )
            decision = _pending(reason, evidence, (*guide_refs, *scope_refs))
            decision = Decision(decision.rule, decision.status, None, None, reason, confirmations,
                                decision.rule_sources, evidence, ("legal office, not a contractor", "office-professional duties with unresolved exceptions"), "whole_audit_period")
            candidate = "C-110" if guide_valid and observed and role_supported else None
            proposal = ClassificationProposal(candidate, "CG-04" if candidate else None, employee.wages,
                "Propose retaining the entire wage basis under C-110 if the visits were solely legal/office-related work and the auditor confirms that treatment; office/professional observations support this candidate, but it is not an established house rule." if candidate else "Obtain verified duty and guide evidence before proposing a classification; no code is guessed.",
                confirmations, (*guide_refs, *scope_refs), evidence)
            proposals[key] = proposal
            issues.append(OpenItem(f"{employee.name} [{key}]", reason, "; ".join(confirmations), evidence + decision.rule_sources, proposal))
        else:
            decision = Decision("legal_office_actual_duties", "CLASSIFIED", "C-110", "CG-04",
                "Law-office operations and observed office/professional duties support CG-02/CG-04; court/closings are documented as not job sites and no site exception is recorded for this employee.", (), guide_refs, evidence,
                ("law office", "corroborated office/professional duties", "no recorded site-duty exception"), "whole_audit_period")
        decisions[key] = decision
    visits = {key: tuple(sorted(days)) for key, days in dates.items()} if log_valid else {}
    return OfficeEvaluation(decisions, proposals, visits, tuple(issues))
