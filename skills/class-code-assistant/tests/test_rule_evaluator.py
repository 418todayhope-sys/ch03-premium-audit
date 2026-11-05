"""Synthetic rule evidence; no employer answers or final payroll allocations."""

import importlib
from datetime import date, timedelta
from decimal import Decimal, localcontext
from pathlib import Path
import sys
import tempfile
import unittest


COMPONENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPONENT))

GUIDE = """# Synthetic Classification Guide
**CG-02. Assigning codes.** Use actual business and duties.

**CG-04. C-110 Clerical office employees.** Office duties.

**CG-07. Division of payroll.** Records govern division.

**CG-11. R-310 Roofing.** Roof work.

**CG-12. R-320 Siding and gutters.** Siding work.

**CG-15. H-420 Residential homebuilding.** Building dwellings.

**CG-21. E-510 Electrical wiring.** Electrical work.

**CG-31. T-610 Courier and delivery drivers.** Drivers and helpers.

**CG-41. F-710 Restaurants.** Restaurant meals.

**CG-42. F-720 Off-site caterers.** Off-site food service.
"""

# Independently transcribed verified statements; fixture wording is not imported
# from implementation constants, so a wrong threshold/source cannot rewrite the test.
INTERVIEW = """# Synthetic interview fixture
**Nadia Brennan** · Voice · 06:03 PM

An office employee keeps the clerical code C-110 only if the site sign-in log shows them on a job site on four days or fewer in the audit period.

**Nadia Brennan** · Voice · 06:10 PM

If an office employee is on a job site for five or more days, their entire payroll moves to the employer's governing field code carrying the most payroll.

**Nadia Brennan** · Voice · 09:06 PM

Our sign-in day count rule was set up for contractors' office staff, and I have never applied it at an employer with no field code, so I have no practice for it.

**Nadia Brennan** · Voice · 09:04 PM

Contractors doing both roofing and siding classify field workers with 15 or more days on a roof entirely under R-310, and those with fewer days entirely under R-320.

**Nadia Brennan** · Voice · 09:16 PM

The 15-day roofing rule applies specifically to contractors who perform both roofing and siding work within the audit period.

**Nadia Brennan** · Voice · 09:05 PM

When an inside employee rides on a delivery route on two or more days in a Monday-to-Sunday pay week, their whole week's pay is allocated as driver payroll under T-610; a week with only one ride day stays entirely under C-110.

**Max Gabel** · Voice · 09:02 PM

How does your team divide payroll when catering employees also work restaurant shifts but there are no employee timesheets?

**Nadia Brennan** · Voice · 09:02 PM

The caterer code F-720 applies only if off-site catering is 40 percent or more of gross receipts. Otherwise, the catering crew stays under the restaurant code F-710 with everyone else.

**Nadia Brennan** · Voice · 09:05 PM

Yes, the 40 percent threshold is based on the off-site catering gross receipts compared to the employer's total gross receipts for the audit period.

**Nadia Brennan** · Voice · 09:11 PM

You should propose how you would treat it, write down why, and mark it as an open item for me or the employer to confirm. I don't settle these in this conversation.
"""


class RuleEvaluatorTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue((COMPONENT / "rule_evaluator.py").is_file(), "Rule evaluator is not implemented")
        self.rules = importlib.import_module("rule_evaluator")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.guide = self.root / "guide.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview = self.root / "interview.md"
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        self.engine = self.rules.RuleEvaluator.from_paths(self.guide, self.interview)
        self.record = self.rules.SourceReference("synthetic/records.csv", "rows 2-30")
        self.start = date(2025, 1, 1)
        self.end = date(2025, 12, 31)

    def facts(self, **changes):
        values = dict(subject="Synthetic worker", industry="contractor", role="office", period_start=self.start, period_end=self.end, complete=True, evidence_sources=(self.record,), days=(), governing_field_code="H-420", governing_code_confirmed=True)
        values.update(changes)
        return self.rules.RuleFacts(**values)

    def days(self, count, start=None):
        start = start or self.start
        return tuple(start + timedelta(days=i) for i in range(count))

    def assert_classified(self, result, code, paragraph, scope):
        self.assertEqual(result.status, "CLASSIFIED")
        self.assertEqual(result.class_code, code)
        self.assertEqual(result.rationale_ref, paragraph)
        self.assertEqual(result.scope, scope)
        self.assertEqual(result.evidence_sources, (self.record,))
        self.assertTrue(result.rule_sources)
        self.assertTrue(result.applicability)

    def assert_open(self, result):
        self.assertEqual(result.status, "OPEN")
        self.assertIsNone(result.class_code)
        self.assertIsNone(result.rationale_ref)
        self.assertTrue(result.reason)
        self.assertTrue(result.required_confirmation)
        self.assertTrue(all("Synthetic worker" in item for item in result.required_confirmation))

    def test_office_four_five_days_and_duplicate_signins(self):
        for days, code, paragraph in [((), "C-110", "CG-04"), (self.days(4), "C-110", "CG-04"), (self.days(5), "H-420", "CG-15"), (self.days(4) * 3, "C-110", "CG-04")]:
            with self.subTest(days=days):
                result = self.engine.evaluate("contractor_office_visits", self.facts(days=days))
                self.assert_classified(result, code, paragraph, "whole_audit_period")

    def test_office_rule_never_applies_to_noncontractors_or_field_staff(self):
        for changes in [{"industry": "legal"}, {"industry": "courier"}, {"industry": None}, {"role": "field"}, {"role": None}]:
            with self.subTest(changes=changes):
                self.assert_open(self.engine.evaluate("contractor_office_visits", self.facts(days=self.days(6), **changes)))

    def test_office_five_days_requires_confirmed_unique_known_field_code(self):
        for changes in [{"governing_field_code": None}, {"governing_code_confirmed": False}, {"governing_field_code": "C-110"}, {"governing_field_code": "UNKNOWN"}]:
            with self.subTest(changes=changes):
                self.assert_open(self.engine.evaluate("contractor_office_visits", self.facts(days=self.days(5), **changes)))

    def test_roofing_fourteen_fifteen_and_zero_days(self):
        for count, code, paragraph in [(0, "R-320", "CG-12"), (14, "R-320", "CG-12"), (15, "R-310", "CG-11"), (16, "R-310", "CG-11")]:
            with self.subTest(count=count):
                facts = self.facts(role="field", roofing_and_siding=True, days=self.days(count))
                self.assert_classified(self.engine.evaluate("roofing_siding", facts), code, paragraph, "whole_audit_period")

    def test_roofing_requires_both_employer_activities_and_field_role(self):
        for changes in [{"roofing_and_siding": False}, {"roofing_and_siding": None}, {"industry": "home_health"}, {"role": "office"}]:
            with self.subTest(changes=changes):
                values = dict(role="field", roofing_and_siding=True, days=self.days(15))
                values.update(changes)
                self.assert_open(self.engine.evaluate("roofing_siding", self.facts(**values)))

    def test_roof_days_are_distinct_calendar_days_not_timesheet_rows(self):
        facts = self.facts(role="field", roofing_and_siding=True, days=self.days(14) * 4)
        self.assert_classified(self.engine.evaluate("roofing_siding", facts), "R-320", "CG-12", "whole_audit_period")

    def courier(self, **changes):
        values = dict(industry="courier", role="inside", period_start=date(2025, 1, 6), period_end=date(2025, 1, 12))
        values.update(changes)
        return self.facts(**values)

    def test_courier_zero_one_two_days_and_duplicate_routes(self):
        monday = date(2025, 1, 6)
        for days, code, paragraph in [((), "C-110", "CG-04"), ((monday,), "C-110", "CG-04"), ((monday, monday), "C-110", "CG-04"), ((monday, monday + timedelta(days=1)), "T-610", "CG-31")]:
            with self.subTest(days=days):
                self.assert_classified(self.engine.evaluate("courier_week", self.courier(days=days)), code, paragraph, "whole_pay_week")

    def test_courier_rejects_wrong_week_role_industry_and_cross_week_days(self):
        for changes in [{"period_start": date(2025, 1, 7)}, {"period_end": date(2025, 1, 19)}, {"days": (date(2025, 1, 13),)}, {"role": "driver"}, {"industry": "restaurant"}]:
            with self.subTest(changes=changes):
                self.assert_open(self.engine.evaluate("courier_week", self.courier(**changes)))

    def catering(self, **changes):
        values = dict(industry="restaurant", role="catering_crew", mixed_catering_restaurant_duties=True, employee_timesheets_available=False, total_gross_receipts=Decimal("100.00"), offsite_catering_receipts=Decimal("40.00"))
        values.update(changes)
        return self.facts(**values)

    def test_catering_threshold_below_equal_above_and_no_catering_receipts(self):
        for amount, code, paragraph in [("0", "F-710", "CG-41"), ("39.99", "F-710", "CG-41"), ("40.00", "F-720", "CG-42"), ("40.01", "F-720", "CG-42")]:
            with self.subTest(amount=amount):
                facts = self.catering(offsite_catering_receipts=Decimal(amount))
                self.assert_classified(self.engine.evaluate("catering_receipts", facts), code, paragraph, "whole_audit_period")

    def test_catering_comparison_is_exact_even_with_low_decimal_context_precision(self):
        with localcontext() as context:
            context.prec = 3
            facts = self.catering(total_gross_receipts=Decimal("1000000000000000000000000.00"), offsite_catering_receipts=Decimal("399999999999999999999999.99"))
            self.assert_classified(self.engine.evaluate("catering_receipts", facts), "F-710", "CG-41", "whole_audit_period")

    def test_catering_invalid_missing_or_inconsistent_receipts_stay_open(self):
        for changes in [{"total_gross_receipts": None}, {"offsite_catering_receipts": None}, {"total_gross_receipts": Decimal("0")}, {"offsite_catering_receipts": Decimal("-1")}, {"offsite_catering_receipts": Decimal("101")}, {"total_gross_receipts": Decimal("NaN")}, {"offsite_catering_receipts": Decimal("Infinity")}, {"offsite_catering_receipts": 40.0}, {"industry": "other"}, {"role": "kitchen"}]:
            with self.subTest(changes=changes):
                self.assert_open(self.engine.evaluate("catering_receipts", self.catering(**changes)))

    def test_catering_outside_documented_mixed_duties_without_timesheets_stays_open(self):
        for changes in [{"mixed_catering_restaurant_duties": False}, {"mixed_catering_restaurant_duties": None}, {"employee_timesheets_available": True}, {"employee_timesheets_available": None}]:
            with self.subTest(changes=changes):
                self.assert_open(self.engine.evaluate("catering_receipts", self.catering(**changes)))

    def test_catering_preserves_question_context_and_missing_context_stays_open(self):
        result = self.engine.evaluate("catering_receipts", self.catering())
        self.assertTrue(any("no employee timesheets" in ref.excerpt for ref in result.rule_sources))
        self.interview.write_text(INTERVIEW.replace("but there are no employee timesheets", "with a different evidence situation"), encoding="utf-8")
        engine = self.rules.RuleEvaluator.from_paths(self.guide, self.interview)
        self.assert_open(engine.evaluate("catering_receipts", self.catering()))

    def test_every_rule_requires_complete_evidence_dates_and_record_citations(self):
        cases = {"contractor_office_visits": self.facts(), "roofing_siding": self.facts(role="field", roofing_and_siding=True), "courier_week": self.courier(), "catering_receipts": self.catering()}
        for rule, facts in cases.items():
            for changes in [{"complete": False}, {"complete": None}, {"evidence_sources": ()}, {"period_start": None}, {"period_end": None}, {"period_end": date(2024, 1, 1)}]:
                with self.subTest(rule=rule, changes=changes):
                    from dataclasses import replace
                    self.assert_open(self.engine.evaluate(rule, replace(facts, **changes)))

    def test_day_rules_reject_missing_invalid_or_out_of_period_days(self):
        for rule, changes in [("contractor_office_visits", {}), ("roofing_siding", {"role": "field", "roofing_and_siding": True}), ("courier_week", {"industry": "courier", "role": "inside", "period_start": date(2025, 1, 6), "period_end": date(2025, 1, 12)})]:
            for days in [None, ("2025-01-06",), (date(2024, 1, 1),)]:
                with self.subTest(rule=rule, days=days):
                    self.assert_open(self.engine.evaluate(rule, self.facts(days=days, **changes)))

    def test_unknown_rule_is_open_with_human_confirmation_and_no_invented_code(self):
        result = self.engine.evaluate("uncovered_certificate_name_mismatch", self.facts())
        self.assert_open(result)
        self.assertIn("no verified rule", result.reason.lower())
        self.assertTrue(any("09:11 PM" in source.locator for source in result.rule_sources))

    def test_decisions_cite_actual_guide_and_nadia_boundary_statements(self):
        result = self.engine.evaluate("roofing_siding", self.facts(role="field", roofing_and_siding=True, days=self.days(15)))
        self.assertTrue(any(source.source == str(self.guide) and source.locator == "CG-11" for source in result.rule_sources))
        boundaries = [source for source in result.rule_sources if "09:16 PM" in source.locator]
        self.assertEqual(len(boundaries), 1)
        source = boundaries[0]
        self.assertEqual(source.source, str(self.interview))
        self.assertIn("both roofing and siding", source.excerpt)
        lines = self.interview.read_text().splitlines()
        self.assertIn(source.excerpt, "\n".join(lines[source.line_start - 1:source.line_end]))
        self.assertEqual(len(source.sha256), 64)
        self.assertTrue(any("both roofing and siding" in boundary for boundary in result.applicability))

    def test_missing_rule_anchor_or_boundary_prevents_classification(self):
        for old in ["Contractors doing both roofing and siding classify", "The 15-day roofing rule applies specifically"]:
            with self.subTest(old=old):
                self.interview.write_text(INTERVIEW.replace(old, "UNVERIFIED"), encoding="utf-8")
                engine = self.rules.RuleEvaluator.from_paths(self.guide, self.interview)
                result = engine.evaluate("roofing_siding", self.facts(role="field", roofing_and_siding=True, days=self.days(15)))
                self.assert_open(result)
                self.assertIn("source", result.reason.lower())

    def test_participant_assertions_do_not_substitute_for_auditor_rules(self):
        self.interview.write_text(INTERVIEW.replace("**Nadia Brennan**", "**Participant**"), encoding="utf-8")
        engine = self.rules.RuleEvaluator.from_paths(self.guide, self.interview)
        self.assert_open(engine.evaluate("contractor_office_visits", self.facts()))

    def test_missing_guide_code_or_entire_source_stays_open(self):
        self.guide.write_text(GUIDE.replace("CG-11. R-310", "CG-11. UNVERIFIED"), encoding="utf-8")
        engine = self.rules.RuleEvaluator.from_paths(self.guide, self.interview)
        self.assert_open(engine.evaluate("roofing_siding", self.facts(role="field", roofing_and_siding=True, days=self.days(15))))
        engine = self.rules.RuleEvaluator.from_paths(self.root / "missing.md", self.interview)
        self.assert_open(engine.evaluate("contractor_office_visits", self.facts()))

    def test_ambiguous_governing_code_or_paragraph_stays_open(self):
        for extra in ["\n**CG-15. H-420 Repeated paragraph.** Unresolved duplicate.\n", "\n**CG-99. H-420 Different paragraph.** Unresolved code definition.\n"]:
            with self.subTest(extra=extra):
                self.guide.write_text(GUIDE + extra, encoding="utf-8")
                engine = self.rules.RuleEvaluator.from_paths(self.guide, self.interview)
                self.assert_open(engine.evaluate("contractor_office_visits", self.facts(days=self.days(5))))

    def test_fixed_rule_code_cannot_move_to_a_conflicting_guide_paragraph(self):
        self.guide.write_text(GUIDE.replace("CG-11. R-310 Roofing.", "CG-11. R-999 Different code.") + "\n**CG-99. R-310 Non-roof activity.** Does not cover roofing.\n", encoding="utf-8")
        engine = self.rules.RuleEvaluator.from_paths(self.guide, self.interview)
        result = engine.evaluate("roofing_siding", self.facts(role="field", roofing_and_siding=True, days=self.days(15)))
        self.assert_open(result)
        self.assertIn("CG-11", result.reason)

    def test_factory_rereads_changed_documents_instead_of_using_stale_rules(self):
        self.interview.write_text(INTERVIEW.replace("four days or fewer", "three days or fewer"), encoding="utf-8")
        engine = self.rules.RuleEvaluator.from_paths(self.guide, self.interview)
        self.assert_open(engine.evaluate("contractor_office_visits", self.facts(days=self.days(4))))


if __name__ == "__main__":
    unittest.main()
