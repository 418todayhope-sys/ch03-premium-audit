"""Evaluate source-verified house practices; never allocate payroll or guess codes."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
import hashlib
from pathlib import Path
import re

from input_reader import InputError, MarkdownSource, read_markdown


@dataclass(frozen=True)
class SourceReference:
    source: str
    locator: str
    line_start: int = 0
    line_end: int = 0
    excerpt: str = ""
    sha256: str = ""


@dataclass(frozen=True)
class RuleFacts:
    subject: str
    industry: str | None = None
    role: str | None = None
    period_start: date | None = None
    period_end: date | None = None
    complete: bool = False
    evidence_sources: tuple[SourceReference, ...] = ()
    days: tuple[date, ...] | None = None
    governing_field_code: str | None = None
    governing_code_confirmed: bool = False
    roofing_and_siding: bool | None = None
    mixed_catering_restaurant_duties: bool | None = None
    employee_timesheets_available: bool | None = None
    total_gross_receipts: Decimal | None = None
    offsite_catering_receipts: Decimal | None = None


@dataclass(frozen=True)
class RuleDefinition:
    applicability: tuple[str, ...]
    scope: str
    guide_ids: tuple[str, ...]
    interview_anchors: tuple[tuple[str, str], ...]
    context_anchors: tuple[tuple[str, str, str], ...] = ()


@dataclass(frozen=True)
class Decision:
    rule: str
    status: str
    class_code: str | None
    rationale_ref: str | None
    reason: str
    required_confirmation: tuple[str, ...]
    rule_sources: tuple[SourceReference, ...]
    evidence_sources: tuple[SourceReference, ...]
    applicability: tuple[str, ...]
    scope: str


# Internal rule names are not company paragraph identifiers. These policies are
# manually verified against Nadia's statements; source matching does not infer rules.
RULES = {
    "contractor_office_visits": RuleDefinition(
        ("contractor employer", "office employee by actual duties", "complete audit-period site sign-in evidence", "five or more days requires an evidenced unique governing field code"),
        "whole_audit_period", ("CG-02", "CG-04"), (
            ("06:03 PM", "An office employee keeps the clerical code C-110 only if the site sign-in log shows them on a job site on four days or fewer in the audit period."),
            ("06:10 PM", "If an office employee is on a job site for five or more days, their entire payroll moves to the employer's governing field code carrying the most payroll."),
            ("09:06 PM", "Our sign-in day count rule was set up for contractors' office staff, and I have never applied it at an employer with no field code, so I have no practice for it."),
        ),
    ),
    "roofing_siding": RuleDefinition(
        ("contractor employer performing both roofing and siding within the audit period", "field worker by actual duties", "complete audit-period roof-day evidence"),
        "whole_audit_period", ("CG-02", "CG-07", "CG-11", "CG-12"), (
            ("09:04 PM", "Contractors doing both roofing and siding classify field workers with 15 or more days on a roof entirely under R-310, and those with fewer days entirely under R-320."),
            ("09:16 PM", "The 15-day roofing rule applies specifically to contractors who perform both roofing and siding work within the audit period."),
        ),
    ),
    "courier_week": RuleDefinition(
        ("courier employer", "inside employee by actual duties", "one complete Monday-to-Sunday pay week", "complete route and pay-week evidence"),
        "whole_pay_week", ("CG-02", "CG-04", "CG-07", "CG-31"), (
            ("09:05 PM", "When an inside employee rides on a delivery route on two or more days in a Monday-to-Sunday pay week, their whole week's pay is allocated as driver payroll under T-610; a week with only one ride day stays entirely under C-110."),
        ),
    ),
    "catering_receipts": RuleDefinition(
        ("restaurant employer with a catering crew", "mixed catering and restaurant duties without employee timesheets (documented interview context)", "complete audited-period off-site and total gross receipts"),
        "whole_audit_period", ("CG-02", "CG-07", "CG-41", "CG-42"), (
            ("09:02 PM", "The caterer code F-720 applies only if off-site catering is 40 percent or more of gross receipts. Otherwise, the catering crew stays under the restaurant code F-710 with everyone else."),
            ("09:05 PM", "Yes, the 40 percent threshold is based on the off-site catering gross receipts compared to the employer's total gross receipts for the audit period."),
        ),
        (("Max Gabel", "09:02 PM", "How does your team divide payroll when catering employees also work restaurant shifts but there are no employee timesheets?"),),
    ),
}
_OPEN_ANCHOR = ("09:11 PM", "You should propose how you would treat it, write down why, and mark it as an open item for me or the employer to confirm. I don't settle these in this conversation.")
_FIXED_CODE_PARAGRAPHS = {
    "C-110": "CG-04", "R-310": "CG-11", "R-320": "CG-12",
    "T-610": "CG-31", "F-710": "CG-41", "F-720": "CG-42",
}
_GUIDE_HEADING = re.compile(r"(?m)^\*\*(CG-[0-9]+)\.")
_CODE_HEADING = re.compile(r"\*\*(CG-[0-9]+)\.\s+([A-Z]-[0-9]+)\b")
_MESSAGE = re.compile(r"(?m)^\*\*([^*]+)\*\* · (?:Voice|Text) · ([0-9:]+ [AP]M)[ \t]*$")


def _reference(document: MarkdownSource, start: int, end: int, locator: str) -> SourceReference:
    excerpt = document.text[start:end].rstrip()
    return SourceReference(
        str(document.path), locator,
        document.text.count("\n", 0, start) + 1,
        document.text.count("\n", 0, start + len(excerpt)) + 1,
        excerpt, hashlib.sha256(document.text.encode("utf-8")).hexdigest(),
    )


class RuleEvaluator:
    """A rule set bound to freshly loaded guide/interview evidence for one run."""

    @classmethod
    def from_paths(cls, guide_path: str | Path, interview_path: str | Path) -> RuleEvaluator:
        documents = []
        errors = []
        for path in (guide_path, interview_path):
            try:
                documents.append(read_markdown(path))
            except InputError as exc:
                documents.append(None)
                errors.append(str(exc))
        return cls(*documents, source_errors=tuple(errors))

    def __init__(
        self, guide: MarkdownSource | None, interview: MarkdownSource | None,
        *, source_errors: tuple[str, ...] = (),
    ):
        paragraphs: dict[str, list[SourceReference]] = {}
        self.code_sources: dict[str, list[SourceReference]] = {}
        if guide is not None:
            matches = list(_GUIDE_HEADING.finditer(guide.text))
            for index, match in enumerate(matches):
                end = matches[index + 1].start() if index + 1 < len(matches) else len(guide.text)
                source = _reference(guide, match.start(), end, match.group(1))
                paragraphs.setdefault(match.group(1), []).append(source)
                code = _CODE_HEADING.match(source.excerpt)
                if code:
                    self.code_sources.setdefault(code.group(2), []).append(source)
        self.ambiguous_paragraphs = {name for name, found in paragraphs.items() if len(found) != 1}
        self.code_errors = {}
        for code, paragraph in _FIXED_CODE_PARAGRAPHS.items():
            found = self.code_sources.get(code, [])
            if len(found) != 1 or found[0].locator != paragraph or paragraph in self.ambiguous_paragraphs:
                self.code_errors[code] = f"guide source must uniquely define {code} in its verified paragraph {paragraph}; changed or conflicting definitions require auditor confirmation"
        messages = []
        if interview is not None:
            matches = list(_MESSAGE.finditer(interview.text))
            for index, match in enumerate(matches):
                end = matches[index + 1].start() if index + 1 < len(matches) else len(interview.text)
                source = _reference(interview, match.start(), end, f"{match.group(1)} · {match.group(2)}")
                messages.append((match.group(1), match.group(2), interview.text[match.end():end], source))

        def find_statement(anchor, speaker="Nadia Brennan"):
            time, wording = anchor
            return [source for author, stamp, body, source in messages if author == speaker and stamp == time and wording in body]

        self.rule_sources: dict[str, tuple[SourceReference, ...]] = {}
        self.source_errors: dict[str, tuple[str, ...]] = {}
        for name, definition in RULES.items():
            sources = []
            errors = list(source_errors)
            errors.extend(self.code_errors[code] for code, paragraph in _FIXED_CODE_PARAGRAPHS.items() if paragraph in definition.guide_ids and code in self.code_errors)
            for paragraph in definition.guide_ids:
                found = paragraphs.get(paragraph, [])
                if len(found) != 1:
                    errors.append(f"guide source paragraph {paragraph} is missing or ambiguous")
                else:
                    sources.extend(found)
            for speaker, time, wording in definition.context_anchors:
                found = find_statement((time, wording), speaker)
                if len(found) != 1:
                    errors.append(f"interview source context at {time} is missing, changed or ambiguous: {wording}")
                else:
                    sources.extend(found)
            for anchor in definition.interview_anchors:
                found = find_statement(anchor)
                if len(found) != 1:
                    errors.append(f"Nadia source statement at {anchor[0]} is missing, changed or ambiguous: {anchor[1]}")
                else:
                    sources.extend(found)
            self.rule_sources[name] = tuple(sources)
            self.source_errors[name] = tuple(errors)
        self.fallback_sources = tuple(paragraphs.get("CG-02", [])) + tuple(find_statement(_OPEN_ANCHOR))

    def evaluate(self, rule: str, facts: RuleFacts) -> Decision:
        definition = RULES.get(rule)
        sources = self.rule_sources.get(rule, self.fallback_sources)

        def open_decision(reason: str) -> Decision:
            return Decision(
                rule, "OPEN", None, None, reason,
                (f"Auditor or employer must confirm {facts.subject}: {reason}",),
                sources, facts.evidence_sources,
                definition.applicability if definition else (),
                definition.scope if definition else "unresolved",
            )

        def classified(code: str, reason: str) -> Decision:
            if code in self.code_errors:
                return open_decision(self.code_errors[code])
            code_sources = self.code_sources.get(code, [])
            if len(code_sources) != 1 or code_sources[0].locator in self.ambiguous_paragraphs:
                return open_decision(f"Classification Guide source does not uniquely verify code {code}; obtain the applicable unambiguous code paragraph.")
            code_source = code_sources[0]
            refs = sources if code_source in sources else sources + (code_source,)
            return Decision(rule, "CLASSIFIED", code, code_source.locator, reason, (), refs, facts.evidence_sources, definition.applicability, definition.scope)

        if definition is None:
            return open_decision("No verified rule exists for this case; obtain the auditor's treatment before assigning a classification.")
        if self.source_errors[rule]:
            return open_decision("Rule source evidence is not verified: " + "; ".join(self.source_errors[rule]))
        if not facts.evidence_sources or not all(isinstance(source, SourceReference) and source.source and source.locator for source in facts.evidence_sources):
            return open_decision("Provide source filenames and record locators supporting the actual duties, industry and rule facts.")
        if facts.complete is not True:
            return open_decision("Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity.")
        if type(facts.period_start) is not date or type(facts.period_end) is not date or facts.period_start > facts.period_end:
            return open_decision("Confirm the exact start and end dates of the relevant audit period or pay week.")
        expected = {
            "contractor_office_visits": ("contractor", "office"),
            "roofing_siding": ("contractor", "field"),
            "courier_week": ("courier", "inside"),
            "catering_receipts": ("restaurant", "catering_crew"),
        }[rule]
        if (facts.industry, facts.role) != expected:
            return open_decision(f"This rule applies only to {expected[0]} employers and {expected[1]} staff by actual duties; confirm applicability or obtain an auditor rule for this case.")
        if rule == "roofing_siding" and facts.roofing_and_siding is not True:
            return open_decision("Confirm this contractor performs both roofing and siding within the audit period; the 15-day rule is not established for other contractors.")
        if rule == "courier_week" and (facts.period_start.weekday() != 0 or (facts.period_end - facts.period_start).days != 6):
            return open_decision("Confirm one Monday-to-Sunday pay week; do not apply the ride-day threshold to an annual total or another week boundary.")

        if rule == "catering_receipts":
            if facts.mixed_catering_restaurant_duties is not True or facts.employee_timesheets_available is not False:
                return open_decision("Confirm mixed catering and restaurant duties with no employee timesheets, as in the documented interview case; obtain auditor confirmation for other contexts or time-record-based treatment under CG-07.")
            total = facts.total_gross_receipts
            offsite = facts.offsite_catering_receipts
            if not all(isinstance(value, Decimal) and value.is_finite() for value in (total, offsite)):
                return open_decision("Provide finite Decimal off-site catering and total gross receipts for the same complete audit period.")
            if total <= 0 or offsite < 0 or offsite > total:
                return open_decision("Confirm consistent gross receipts: total must be positive and off-site receipts must be between zero and total.")
            # Integer ratios avoid rounding even under a caller's low Decimal precision.
            off_num, off_den = offsite.as_integer_ratio()
            total_num, total_den = total.as_integer_ratio()
            qualifies = off_num * total_den * 5 >= total_num * off_den * 2
            return classified("F-720" if qualifies else "F-710", "Off-site catering is at least 40 percent of audit-period gross receipts." if qualifies else "Off-site catering is below 40 percent of audit-period gross receipts.")

        if facts.days is None or not all(type(day) is date for day in facts.days):
            return open_decision("Provide the actual calendar dates from the complete relevant activity log; an absent log is not zero days.")
        if any(day < facts.period_start or day > facts.period_end for day in facts.days):
            return open_decision("Confirm activity dates and the relevant period; cited dates fall outside that period.")
        count = len(set(facts.days))
        if rule == "contractor_office_visits":
            if count <= 4:
                return classified("C-110", f"{count} distinct job-site days is at most four in the audit period.")
            if facts.governing_code_confirmed is not True or not facts.governing_field_code or facts.governing_field_code == "C-110":
                return open_decision("Confirm the unique governing field code carrying the most payroll and cite its supporting records; no governing code or tie treatment is inferred.")
            return classified(facts.governing_field_code, f"{count} distinct job-site days is at least five; use the evidenced governing field code for the whole audit period.")
        if rule == "roofing_siding":
            return classified("R-310" if count >= 15 else "R-320", f"{count} distinct roof days is {'at least' if count >= 15 else 'fewer than'} 15 for this roofing-and-siding contractor's field worker.")
        return classified("T-610" if count >= 2 else "C-110", f"{count} distinct ride days in this Monday-to-Sunday pay week; the {'driver' if count >= 2 else 'clerical'} code applies to the whole week.")
