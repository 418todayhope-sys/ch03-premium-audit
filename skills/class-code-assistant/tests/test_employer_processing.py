"""Real-component integration: evidence gaps must not become classifications."""

from dataclasses import replace
from decimal import Decimal, localcontext
import csv
import hashlib
import importlib
import io
import os
from pathlib import Path
import sys
import tempfile
import unittest

COMPONENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPONENT))
from test_payroll_adjustments import INTERVIEW as ADJUSTMENT_INTERVIEW

GUIDE = """# Synthetic guide
**CG-02. Assigning codes.** An employer is assigned the class code that describes its principal business. An employee
whose work is described by another code in this guide is reported under that code. An employer may carry several codes.

**CG-03. Payroll.** Payroll is the gross remuneration paid to employees for the period: wages, salaries, commissions
and bonuses. Expense reimbursements that the employer can document, such as travel and lodging costs, are not payroll.

**CG-06. Subcontractors.** Payments to a subcontractor who does not carry workers' compensation insurance for its own
workers may be treated as payroll of the employer, under the code for the work the subcontractor performed.

**CG-07. Division of payroll.** When an employee performs work in more than one classification and the employer keeps
records of the time spent in each, the employee's payroll may be divided between the codes.

## Class codes

**CG-41. F-710 Restaurants.** Preparation and service of meals: kitchen staff, servers, hosts and dishwashers.

**CG-42. F-720 Off-site caterers.** Preparation of food and its service at events away from the employer's premises,
including the catering crew of an employer that also runs a restaurant.
"""
INTERVIEW = ADJUSTMENT_INTERVIEW + """
**Max Gabel** · Voice · 09:02 PM

How does your team divide payroll when catering employees also work restaurant shifts but there are no employee timesheets?

**Nadia Brennan** · Voice · 09:02 PM

The caterer code F-720 applies only if off-site catering is 40 percent or more of gross receipts. Otherwise, the catering crew stays under the restaurant code F-710 with everyone else.

**Nadia Brennan** · Voice · 09:05 PM

Yes, the 40 percent threshold is based on the off-site catering gross receipts compared to the employer's total gross receipts for the audit period.
"""
BUSINESS = """# Completely Different Restaurant: business description
Audit period January 1, 2025 to January 31, 2025.
This restaurant prepares meals and also caters off-site events.
"""
NOTES = """# Auditor field notes
Restaurant kitchen, dining room and catering van. The catering crew prepare food in
the kitchen and serve it at the venue; they also work restaurant shifts.
No employee timesheets are available.
"""
APPLICATION = """# Employer's payroll application
| Class code (employer's choice) | Employees | Payroll (USD) |
|---|---|---|
| F-710 | 1 | 100.01 |
| F-720 | 1 | 50.02 |
"""


class EmployerProcessingTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue((COMPONENT / "employer_processing.py").is_file(), "Reusable employer workflow is not implemented")
        self.workflow = importlib.import_module("employer_processing")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.employer = self.root / "arbitrary-employer"
        self.employer.mkdir()
        self.guide = self.root / "guide.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview = self.root / "interview.md"
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        for filename, content in {
            "business-description.md": BUSINESS,
            "field-notes.md": NOTES,
            "application.md": APPLICATION,
            "gross-receipts.csv": "month,dine_in_receipts,offsite_catering_receipts\n2025-01,60.00,40.00\n",
            "payroll-register.csv": "employee_id,name,position,wages_paid\nX9,Example Cook,Line Cook,100.01\nY2,Example Caterer,Catering Lead,50.02\n",
        }.items():
            (self.employer / filename).write_text(content, encoding="utf-8")

    def run_employer(self, **kwargs):
        return self.workflow.process_employer(self.guide, self.employer, self.interview, **kwargs)

    def test_exact_threshold_and_record_application_comparison(self):
        result = self.run_employer()
        self.assertEqual(result.receipts.percentage, Decimal("40"))
        self.assertEqual(result.allocation.by_code, {"F-710": Decimal("100.01"), "F-720": Decimal("50.02")})
        self.assertEqual(result.application.register_difference, Decimal("0.00"))
        self.assertTrue(result.independent_reconciliation.reconciled)
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("150.03"))
        self.assertEqual(result.adjustments.reconciliation.basis_total, Decimal("0.00"))
        self.assertEqual(result.open_items, ())

    def test_below_and_above_threshold_change_actual_catering_payroll(self):
        for dine, offsite, expected in [("60.01", "39.99", "F-710"), ("59.99", "40.01", "F-720")]:
            with self.subTest(offsite=offsite):
                (self.employer / "gross-receipts.csv").write_text(f"month,dine_in_receipts,offsite_catering_receipts\n2025-01,{dine},{offsite}\n", encoding="utf-8")
                result = self.run_employer()
                self.assertEqual(result.decisions["Y2"].class_code, expected)
                self.assertEqual(result.allocation.reconciliation.unresolved_total, Decimal("0.00"))
                if expected == "F-710":
                    self.assertEqual(result.by_code, {"F-710": Decimal("150.03")})
                    self.assertTrue(any("application" in item.subject.lower() for item in result.open_items))

    def test_missing_receipts_keeps_catering_open_without_losing_restaurant_payroll(self):
        (self.employer / "gross-receipts.csv").unlink()
        result = self.run_employer()
        self.assertEqual(result.allocation.by_code, {"F-710": Decimal("100.01")})
        self.assertEqual(result.allocation.reconciliation.unresolved_total, Decimal("50.02"))
        self.assertEqual(result.decisions["Y2"].status, "OPEN")
        self.assertTrue(result.open_items)

    def test_missing_timesheet_file_does_not_prove_no_timesheets_exist(self):
        (self.employer / "field-notes.md").write_text(NOTES.replace("No employee timesheets are available.", ""), encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.decisions["Y2"].status, "OPEN")
        self.assertTrue(any("timesheet" in item.reason.lower() for item in result.open_items))

    def test_partial_month_receipts_do_not_prove_audit_period_coverage(self):
        (self.employer / "business-description.md").write_text(BUSINESS.replace("January 1, 2025", "January 7, 2025"), encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.receipts.percentage, Decimal("40"))
        self.assertFalse(result.receipts.coverage_confirmed)
        self.assertEqual(result.decisions["Y2"].status, "OPEN")
        self.assertTrue(any("period" in item.reason.lower() for item in result.open_items))

    def test_open_catering_proposal_is_conditional_below_40_and_never_allocated(self):
        (self.employer / "business-description.md").write_text(BUSINESS.replace("January 1, 2025", "January 7, 2025"), encoding="utf-8")
        for dining, catering in (("60.01", "39.99"), ("60.00", "40.00"), ("59.99", "40.01")):
            with self.subTest(catering=catering):
                (self.employer / "gross-receipts.csv").write_text(
                    f"month,dine_in_receipts,offsite_catering_receipts\n2025-01,{dining},{catering}\n", encoding="utf-8")
                result = self.run_employer()
                self.assertEqual(result.decisions["Y2"].status, "OPEN")
                self.assertIsNone(result.decisions["Y2"].class_code)
                self.assertEqual(result.by_code, {"F-710": Decimal("100.01")})
                self.assertEqual(result.allocation.reconciliation.unresolved_total, Decimal("50.02"))
                self.assertTrue(result.independent_reconciliation.reconciled)
                if catering == "39.99":
                    self.assertIn("Y2", result.proposals)
                    proposal = result.proposals["Y2"]
                    self.assertEqual((proposal.class_code, proposal.rationale_ref, proposal.wages),
                                     ("F-710", "CG-41", Decimal("50.02")))
                    required = " ".join(proposal.required_confirmation)
                    for detail in ("2025-01-07", "2025-01-31", "below 40%", "timesheet", "auditor"):
                        self.assertIn(detail, required)
                    self.assertTrue(any(ref.locator == "CG-41" for ref in proposal.rule_sources))
                    self.assertTrue(any("09:02 PM" in ref.locator for ref in proposal.rule_sources))
                    finding = next(item for item in result.open_items if "[Y2]" in item.subject)
                    self.assertEqual(finding.proposed_treatment, proposal)
                else:
                    self.assertNotIn("Y2", result.proposals)

    def test_catering_proposal_requires_verified_rule_and_supported_duties(self):
        (self.employer / "business-description.md").write_text(BUSINESS.replace("January 1, 2025", "January 7, 2025"), encoding="utf-8")
        (self.employer / "gross-receipts.csv").write_text(
            "month,dine_in_receipts,offsite_catering_receipts\n2025-01,80.00,20.00\n", encoding="utf-8")
        original_guide, original_interview = self.guide.read_text(), self.interview.read_text()
        for case in ("timesheets", "duties", "guide", "interview", "invalid_receipts", "duplicate_receipts"):
            with self.subTest(case=case):
                self.guide.write_text(original_guide, encoding="utf-8")
                self.interview.write_text(original_interview, encoding="utf-8")
                (self.employer / "field-notes.md").write_text(NOTES, encoding="utf-8")
                (self.employer / "gross-receipts.csv").write_text(
                    "month,dine_in_receipts,offsite_catering_receipts\n2025-01,80.00,20.00\n", encoding="utf-8")
                if case == "timesheets":
                    (self.employer / "field-notes.md").write_text(NOTES.replace("No employee timesheets are available.", "Employee timesheets are available."), encoding="utf-8")
                elif case == "duties":
                    (self.employer / "field-notes.md").write_text("Restaurant kitchen and dining room observed.\n", encoding="utf-8")
                elif case == "guide":
                    self.guide.write_text(original_guide.replace("CG-41. F-710", "CG-99. F-710"), encoding="utf-8")
                elif case == "interview":
                    self.interview.write_text("No verified house practices supplied.\n", encoding="utf-8")
                elif case == "invalid_receipts":
                    (self.employer / "gross-receipts.csv").write_text(
                        "month,dine_in_receipts,offsite_catering_receipts\n2025-01,-80.00,20.00\n", encoding="utf-8")
                else:
                    (self.employer / "gross-receipts.csv").write_text(
                        "month,dine_in_receipts,offsite_catering_receipts\n2025-01,80.00,20.00\n2025-01,80.00,20.00\n", encoding="utf-8")
                self.assertEqual(self.run_employer().proposals, {})

    def test_duplicate_or_negative_receipts_do_not_establish_verified_threshold(self):
        for rows in ["2025-01,60.00,40.00\n2025-01,60.00,40.00\n", "2025-01,-60.00,40.00\n"]:
            with self.subTest(rows=rows):
                (self.employer / "gross-receipts.csv").write_text("month,dine_in_receipts,offsite_catering_receipts\n" + rows, encoding="utf-8")
                result = self.run_employer()
                self.assertEqual(result.decisions["Y2"].status, "OPEN")
                self.assertTrue(result.open_items)

    def test_unknown_position_is_open_and_unsupported_industry_is_not_restaurant(self):
        payroll = self.employer / "payroll-register.csv"
        payroll.write_text(payroll.read_text().replace("Line Cook", "Bookkeeper"), encoding="utf-8")
        self.assertEqual(self.run_employer().decisions["X9"].status, "OPEN")
        (self.employer / "business-description.md").write_text(BUSINESS.replace("restaurant", "metal fabrication shop").replace("Restaurant", "Shop"), encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.allocation.by_code, {})
        self.assertEqual(result.allocation.reconciliation.unresolved_total, Decimal("150.03"))

    def test_titles_without_corroborating_field_evidence_are_not_classifications(self):
        (self.employer / "field-notes.md").write_text("# Notes\nNo duties were observed.\n", encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.allocation.by_code, {})
        self.assertEqual(result.allocation.reconciliation.unresolved_total, Decimal("150.03"))

    def test_changed_guide_definition_prevents_direct_restaurant_classification(self):
        self.guide.write_text(GUIDE.replace("Preparation and service of meals: kitchen staff, servers, hosts and dishwashers.", "This code is retired."), encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.decisions["X9"].status, "OPEN")

    def test_changed_catering_definition_cannot_be_used_by_a_fresh_evaluator(self):
        self.guide.write_text(GUIDE.replace("including the catering crew of an employer that also runs a restaurant.", "This code is retired."), encoding="utf-8")
        self.assertEqual(self.run_employer().decisions["Y2"].status, "OPEN")

    def test_moved_restaurant_code_paragraph_stays_open_instead_of_crashing(self):
        self.guide.write_text(GUIDE.replace("CG-41. F-710", "CG-99. F-710"), encoding="utf-8")
        self.assertEqual(self.run_employer().decisions["X9"].status, "OPEN")

    def test_contradictory_timesheet_prose_prevents_no_timesheets_rule(self):
        (self.employer / "field-notes.md").write_text(NOTES + "Employee timesheets are available for every worker.\n", encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.decisions["Y2"].status, "OPEN")
        self.assertTrue(any("conflict" in item.subject.lower() for item in result.open_items))

    def test_business_description_can_conflict_with_field_notes(self):
        for addition in ["Employee timesheets are available for every worker.", "X9 Example Cook has a misleading register title: actual duties are exclusively bookkeeping in the office; no meal preparation or service."]:
            with self.subTest(addition=addition):
                (self.employer / "business-description.md").write_text(BUSINESS + addition + "\n", encoding="utf-8")
                result = self.run_employer()
                self.assertEqual(result.decisions["Y2"].status, "OPEN")
                self.assertFalse(result.application.definitive)

    def test_employee_duty_exceptions_require_review_instead_of_title_matching(self):
        (self.employer / "field-notes.md").write_text(NOTES + "X9 Example Cook has a misleading register title: actual duties are exclusively bookkeeping in the office; no meal preparation or service.\n", encoding="utf-8")
        self.assertEqual(self.run_employer().decisions["X9"].status, "OPEN")

    def test_negated_restaurant_observations_do_not_establish_actual_duties(self):
        for text in [NOTES.replace("Restaurant kitchen", "No restaurant kitchen"), NOTES.replace("restaurant shifts", "no restaurant shifts")]:
            (self.employer / "field-notes.md").write_text(text, encoding="utf-8")
            result = self.run_employer()
            self.assertTrue(any(item.status == "OPEN" for item in result.decisions.values()))

    def test_net_zero_open_payroll_cannot_make_application_comparison_definitive(self):
        (self.employer / "payroll-register.csv").write_text("employee_id,name,position,wages_paid\nX9,Example One,Unknown,100.01\nY2,Example Two,Unknown,-100.01\n", encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.allocation.reconciliation.unresolved_total, Decimal("0.00"))
        self.assertFalse(result.application.definitive)

    def test_invalid_application_row_is_not_silently_dropped(self):
        (self.employer / "application.md").write_text(APPLICATION.replace("F-720", "INVALID-CODE"), encoding="utf-8")
        result = self.run_employer()
        self.assertIsNone(result.application)
        self.assertTrue(any("application" in item.subject.lower() for item in result.open_items))

    def test_application_total_conflict_is_open_and_never_changes_register(self):
        (self.employer / "application.md").write_text(APPLICATION.replace("100.01", "90.00"), encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.application.register_difference, Decimal("10.01"))
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("150.03"))
        self.assertTrue(any("application" in item.subject.lower() for item in result.open_items))

    def test_configurable_filenames_preserve_sources_and_reread_new_content(self):
        (self.employer / "payroll-register.csv").rename(self.employer / "wages.csv")
        files = replace(self.workflow.EmployerFiles(), payroll="wages.csv")
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.rglob("*") if p.is_file()}
        result = self.run_employer(files=files)
        self.assertEqual(result.allocation.lines[0].employee.source.source, str(self.employer / "wages.csv"))
        self.assertTrue(all(ref.sha256 for ref in result.decisions["Y2"].rule_sources))
        self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in before})
        (self.employer / "gross-receipts.csv").write_text("month,dine_in_receipts,offsite_catering_receipts\n2025-01,80.00,20.00\n", encoding="utf-8")
        self.assertEqual(self.run_employer(files=files).decisions["Y2"].class_code, "F-710")

    def test_low_decimal_precision_does_not_change_receipt_or_payroll_cents(self):
        with localcontext() as context:
            context.prec = 3
            result = self.run_employer()
            self.assertEqual(result.receipts.total, Decimal("100.00"))
            self.assertEqual(result.independent_reconciliation.register_total, Decimal("150.03"))
            self.assertEqual(result.independent_reconciliation.difference, Decimal("0.00"))

    def test_missing_payroll_returns_open_without_fabricating_zero_payroll(self):
        (self.employer / "payroll-register.csv").unlink()
        result = self.run_employer()
        self.assertIsNone(result.allocation)
        self.assertIsNone(result.independent_reconciliation)
        self.assertTrue(result.open_items)

    def test_missing_guide_or_malformed_csv_returns_explicit_open_source_failure(self):
        missing = self.workflow.process_employer(self.root / "missing-guide.md", self.employer, self.interview)
        self.assertIsNone(missing.allocation)
        self.assertTrue(missing.open_items)
        (self.employer / "gross-receipts.csv").write_text("month,dine_in_receipts,offsite_catering_receipts\n2025-01,not-money,40.00\n", encoding="utf-8")
        malformed = self.run_employer()
        self.assertIsNone(malformed.allocation)
        self.assertTrue(any("invalid money" in item.reason for item in malformed.open_items))

    def test_unmapped_duty_source_cannot_be_silently_ignored(self):
        (self.employer / "individual-duties.md").write_text("X9 performs bookkeeping rather than cooking.\n", encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.allocation.by_code, {})
        self.assertTrue(any("unmapped" in item.subject.lower() for item in result.open_items))

    def test_extra_payroll_duty_column_requires_adapter_review(self):
        (self.employer / "payroll-register.csv").write_text("employee_id,name,position,wages_paid,actual_duties\nX9,Example Cook,Line Cook,100.01,bookkeeping\nY2,Example Caterer,Catering Lead,50.02,catering\n", encoding="utf-8")
        self.assertEqual(self.run_employer().allocation.by_code, {})

    def test_unadapted_adjustment_records_stay_open_without_assumed_claims(self):
        (self.employer / "allowance.csv").write_text("allowance_id,employee_id,amount_paid\nA1,X9,100.00\nA2,Y2,200.00\n", encoding="utf-8")
        result = self.run_employer()
        self.assertEqual(result.adjustments.reconciliation.basis_total, Decimal("0.00"))
        self.assertEqual(result.by_code, {"F-710": Decimal("100.01"), "F-720": Decimal("50.02")})
        self.assertTrue(any("adjustment" in item.subject.lower() for item in result.open_items))
        self.assertFalse(result.application.definitive)


class RestaurantDutySafeguardTests(unittest.TestCase):
    """Individual work evidence must prevail over a restaurant register title."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.employer = self.root / "willow-meal-house"
        self.employer.mkdir()
        self.guide = self.root / "guide.md"
        self.interview = self.root / "interview.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        for filename, content in {
            "business-description.md": BUSINESS.replace("Completely Different Restaurant", "Willow Meal House"),
            "field-notes.md": NOTES,
            "payroll-register.csv": "employee_id,name,position,wages_paid\nDIN-C,Iris Stone,Line Cook,31.01\nDIN-S,Theo Moss,Server,42.02\nEVT-C,Nell Vale,Catering Lead,20.03\n",
            "gross-receipts.csv": "month,dine_in_receipts,offsite_catering_receipts\n2025-01,60.00,40.00\n",
            "application.md": "# Application\n| Class code (employer's choice) | Employees | Payroll (USD) |\n|---|---|---|\n| F-710 | 2 | 73.03 |\n| F-720 | 1 | 20.03 |\n",
        }.items():
            (self.employer / filename).write_text(content, encoding="utf-8")

    def run_restaurant(self):
        return importlib.import_module("employer_processing").process_employer(
            self.guide, self.employer, self.interview)

    def test_named_nonrestaurant_work_stays_open_with_unclassified_proposal_and_question(self):
        note = "The server, Theo Moss, installs and repairs electrical wiring at customers' buildings every workday."
        path = self.employer / "field-notes.md"
        path.write_text(NOTES + note + "\n", encoding="utf-8")
        result = self.run_restaurant()
        self.assertEqual(result.decisions["DIN-S"].status, "OPEN")
        self.assertIsNone(result.decisions["DIN-S"].class_code)
        self.assertEqual(result.by_code, {"F-710": Decimal("31.01"), "F-720": Decimal("20.03")})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("42.02"))
        proposal = result.proposals["DIN-S"]
        self.assertEqual((proposal.class_code, proposal.rationale_ref, proposal.wages), (None, None, Decimal("42.02")))
        self.assertTrue({"CG-02", "CG-41"} <= {ref.locator for ref in proposal.rule_sources})
        self.assertTrue(any(ref.source == str(path) and note in ref.excerpt for ref in proposal.evidence_sources))
        required = " ".join(proposal.required_confirmation)
        self.assertTrue(all(term in required for term in ("Theo Moss", "DIN-S", "duties", "auditor")))
        finding = next(item for item in result.open_items if "[DIN-S]" in item.subject)
        self.assertEqual(finding.proposed_treatment, proposal)
        self.assertTrue(finding.required_confirmation)
        self.assertNotIn("E-510", result.by_code)
        self.assertTrue(result.independent_reconciliation.reconciled)

    def test_paraphrased_nonrestaurant_work_does_not_require_a_trade_keyword(self):
        for statement in (
            "Theo Moss spends every weekday connecting circuits in houses.",
            "The server pulls cable through building walls and fits power outlets.",
            "DIN-S maintains refrigeration equipment for other businesses.",
        ):
            with self.subTest(statement=statement):
                (self.employer / "field-notes.md").write_text(NOTES + statement + "\n", encoding="utf-8")
                result = self.run_restaurant()
                self.assertEqual(result.decisions["DIN-S"].status, "OPEN")
                self.assertIsNone(result.proposals["DIN-S"].class_code)
                self.assertEqual(result.by_code, {"F-710": Decimal("31.01"), "F-720": Decimal("20.03")})

    def test_individual_duty_conflict_in_business_description_requires_review(self):
        (self.employer / "business-description.md").write_text(
            BUSINESS + "Theo Moss connects circuits in houses each day.\n", encoding="utf-8")
        result = self.run_restaurant()
        self.assertEqual(result.decisions["DIN-S"].status, "OPEN")
        self.assertEqual(result.by_code, {"F-710": Decimal("31.01"), "F-720": Decimal("20.03")})
        self.assertTrue(any(ref.source.endswith("business-description.md") for ref in result.proposals["DIN-S"].evidence_sources))

    def test_supported_food_duty_paraphrases_preserve_restaurant_and_catering(self):
        for statement in (
            "The server, Theo Moss, serves meals in the dining room.",
            "Theo Moss prepares and serves meals in the dining room.",
            "Workers cook meals in the kitchen and wait tables in the dining room.",
            "Cooks prepare meals and servers serve customers.",
        ):
            for dine, catering, expected in (("60.00", "40.00", {"F-710": Decimal("73.03"), "F-720": Decimal("20.03")}),
                                             ("60.01", "39.99", {"F-710": Decimal("93.06")})):
                with self.subTest(statement=statement, catering=catering):
                    (self.employer / "field-notes.md").write_text(NOTES + statement + "\n", encoding="utf-8")
                    (self.employer / "gross-receipts.csv").write_text(
                        f"month,dine_in_receipts,offsite_catering_receipts\n2025-01,{dine},{catering}\n", encoding="utf-8")
                    result = self.run_restaurant()
                    self.assertEqual(result.by_code, expected)
                    self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
                    self.assertNotIn("DIN-S", result.proposals)

    def test_food_duties_do_not_mask_a_conflicting_clause_in_the_same_sentence(self):
        (self.employer / "field-notes.md").write_text(
            NOTES + "Theo Moss serves meals in the dining room and connects circuits in houses.\n", encoding="utf-8")
        result = self.run_restaurant()
        self.assertEqual(result.decisions["DIN-S"].status, "OPEN")
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("42.02"))
        self.assertIsNone(result.proposals["DIN-S"].class_code)

    def test_named_conflict_does_not_block_a_different_worker_with_the_same_title(self):
        path = self.employer / "payroll-register.csv"
        path.write_text(path.read_text() + "DIN-T,Uma Birch,Server,15.04\n", encoding="utf-8")
        (self.employer / "field-notes.md").write_text(
            NOTES + "The server, Theo Moss, connects circuits in houses.\n", encoding="utf-8")
        result = self.run_restaurant()
        self.assertEqual(result.decisions["DIN-S"].status, "OPEN")
        self.assertEqual(result.decisions["DIN-T"].class_code, "F-710")
        self.assertEqual(result.by_code, {"F-710": Decimal("46.05"), "F-720": Decimal("20.03")})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("42.02"))
        self.assertNotIn("DIN-T", result.proposals)

    def test_missing_duty_notes_require_unclassified_review_proposal(self):
        (self.employer / "field-notes.md").unlink()
        result = self.run_restaurant()
        self.assertEqual(result.by_code, {})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("93.06"))
        self.assertIn("DIN-S", result.proposals)
        self.assertIsNone(result.proposals["DIN-S"].class_code)
        self.assertTrue(result.proposals["DIN-S"].required_confirmation)
        self.assertTrue(result.independent_reconciliation.reconciled)

    def test_unconfirmed_individual_duties_cannot_use_the_register_title(self):
        (self.employer / "field-notes.md").write_text(
            NOTES + "The server's duties have not been confirmed.\n", encoding="utf-8")
        result = self.run_restaurant()
        self.assertEqual(result.decisions["DIN-S"].status, "OPEN")
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("42.02"))
        self.assertIsNone(result.proposals["DIN-S"].class_code)

    def test_missing_kitchen_observations_do_not_establish_restaurant_work(self):
        (self.employer / "field-notes.md").write_text("# Observations\nNo duties were observed.\n", encoding="utf-8")
        result = self.run_restaurant()
        self.assertEqual(result.by_code, {})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("93.06"))
        self.assertIn("DIN-S", result.proposals)
        self.assertIsNone(result.proposals["DIN-S"].class_code)
        self.assertTrue(result.proposals["DIN-S"].required_confirmation)


class LocalLarkspurIntegrationTest(unittest.TestCase):
    def test_actual_sources_allocate_only_evidenced_payroll_and_reconcile(self):
        self.assertTrue((COMPONENT / "employer_processing.py").is_file(), "Reusable employer workflow is not implemented")
        root = Path(os.environ.get("INSURANCE01_TEST_INPUTS", "/home/maxg/insurance01-inputs"))
        interview = COMPONENT.parents[1] / "interviews" / "ch03-premium-audit-20261105-0222(1).md"
        if not root.is_dir() or not interview.is_file():
            self.skipTest("Authoritative local development snapshots are unavailable")
        workflow = importlib.import_module("employer_processing")
        employer = root / "employer-files" / "larkspur-lane-bistro"
        result = workflow.process_employer(root / "classification-guide.md", employer, interview)
        self.assertEqual(result.receipts.dine_in, Decimal("1284615.20"))
        self.assertEqual(result.receipts.offsite, Decimal("362410.85"))
        self.assertEqual(result.receipts.total, Decimal("1647026.05"))
        self.assertTrue(Decimal("22.0039") < result.receipts.percentage < Decimal("22.0040"))
        self.assertEqual(result.by_code, {"F-710": Decimal("226431.55")})
        self.assertEqual(result.allocation.reconciliation.unresolved_total, Decimal("114293.80"))
        raw_rows = list(csv.DictReader(io.StringIO((employer / "payroll-register.csv").read_text())))
        raw_total = sum(Decimal(row["wages_paid"]) for row in raw_rows)
        self.assertEqual(raw_total, Decimal("340725.35"))
        self.assertEqual(sum(line.wages for line in result.allocation.lines), raw_total)
        self.assertEqual(result.independent_reconciliation.difference, Decimal("0.00"))
        self.assertTrue(result.independent_reconciliation.reconciled)
        self.assertEqual(sum(line.status == "ALLOCATED" for line in result.allocation.lines), 6)
        self.assertEqual(sum(line.status == "OPEN" for line in result.allocation.lines), 3)
        self.assertEqual(result.application.register_difference, Decimal("0.00"))
        self.assertTrue(all("complete relevant audit period" in result.decisions[key].reason for key in ("LL-E07", "LL-E08", "LL-E09")))
        self.assertFalse(any("guide's catering definitions differ" in item.reason for item in result.open_items))


if __name__ == "__main__":
    unittest.main()
