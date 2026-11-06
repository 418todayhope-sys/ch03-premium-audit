"""End-to-end homebuilding and subcontractor evidence, without identity guesses."""

from dataclasses import replace
from decimal import Decimal, ROUND_DOWN, ROUND_UP, localcontext
import csv
import io
import os
from pathlib import Path
import sys
import tempfile
import unittest

COMPONENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPONENT))
from employer_processing import EmployerFiles, process_employer
from test_contractor_processing import GUIDE as CONTRACTOR_GUIDE, INTERVIEW, SITE_HEADER

GUIDE = CONTRACTOR_GUIDE.replace("**CG-06.", "**CG-05. Owners and executive officers.** An owner or executive officer who has filed an election of exclusion is not\ncounted. An owner who is included is counted under the code for the work the owner does.\n\n**CG-06.") + """
**CG-15. H-420 Residential homebuilding.** Construction and remodeling of dwellings: framing, drywall, interior
finish, carpentry and general labor at the building site. Roofing work is described by CG-11 and electrical wiring
by CG-21.
"""
BUSINESS = """# Independent Homes: business description
Audit period January 1, 2025 to December 31, 2025.
Independent Homes builds single-family houses: framing, drywall, finish carpentry and site labor with its own crew, and subcontractors for some trades.
Four employees. The owner, Excluded Person, has filed an election of exclusion and is not on the payroll register.
"""
NOTES = """# Auditor field notes
Office in a converted house; three houses under construction. The office manager, Manager One,
drives material and paperwork out to the sites and meets inspectors there; the owner calls it "running errands".
The estimator visits a site now and then to measure. The bookkeeper stays in the office.
Three subcontractors were paid in the period (framing, drywall and roofing). The owner says they are all insured; we
collected the certificates of insurance the owner could find.
"""
PAYROLL = """employee_id,name,position,wages_paid
H1,Field One,Carpenter,100.00
E1,Estimator One,Estimator,50.00
M1,Manager One,Office Manager,60.00
B1,Books One,Bookkeeper,40.00
"""
APPLICATION = """# Application
| Class code (employer's choice) | Employees | Payroll (USD) |
|---|---|---|
| H-420 | 1 | 100.00 |
| C-110 | 3 | 150.00 |
"""
PAYMENTS = """date,subcontractor,work,invoice,amount_paid
2025-03-01,FrameBuild Co.,framing,FRAME-1,50.00
2025-04-01,DryBuild,drywall,DRY-1,20.05
2025-05-01,RoofBuild,roofing,ROOF-1,30.00
"""
CERTIFICATES = """subcontractor,certificate_no,coverage_from,coverage_to
FrameBuild Co.,CERT-F,2025-01-01,2025-12-31
RoofBuild & Siding LLC,CERT-R,2025-01-01,2025-06-30
"""


class HomebuildingIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.employer = self.root / "independent-homebuilding-inputs"
        self.employer.mkdir()
        self.guide = self.root / "guide.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview = self.root / "interview.md"
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        for filename, text in {"business-description.md": BUSINESS, "field-notes.md": NOTES,
                               "payroll-register.csv": PAYROLL, "application.md": APPLICATION,
                               "subcontractor-payments.csv": PAYMENTS, "insurance-certificates.csv": CERTIFICATES}.items():
            (self.employer / filename).write_text(text, encoding="utf-8")
        self.set_visits()

    def set_visits(self, estimator=3):
        rows = [f"2025-02-{index+1:02d},E1,Estimator One,Site A,09:00\n" for index in range(estimator)]
        rows += [f"2025-03-{index+1:02d},M1,Manager One,Site A,10:00\n" for index in range(5)]
        rows.append("2025-04-15,,County inspector,Site A,11:00\n")
        (self.employer / "site-signin-log.csv").write_text(SITE_HEADER + "".join(rows), encoding="utf-8")

    def run_homes(self, **kwargs):
        return process_employer(self.guide, self.employer, self.interview, **kwargs)

    def test_employee_rules_subcontractor_additions_and_combined_reconciliation(self):
        result = self.run_homes()
        self.assertEqual(result.allocation.by_code, {"H-420": Decimal("160.00"), "C-110": Decimal("90.00")})
        self.assertEqual(result.by_code, {"H-420": Decimal("172.03"), "C-110": Decimal("90.00")})
        self.assertEqual(result.governing_field.class_code, "H-420")
        self.assertEqual(result.adjustments.reconciliation.basis_total, Decimal("100.05"))
        self.assertEqual(result.adjustments.reconciliation.payroll_added, Decimal("12.03"))
        self.assertEqual(result.adjustments.reconciliation.nonpayroll, Decimal("58.02"))
        self.assertEqual(result.adjustments.reconciliation.unresolved_basis, Decimal("30.00"))
        self.assertTrue(result.combined_reconciliation.reconciled)
        self.assertEqual(result.combined_reconciliation.confirmed_payroll, Decimal("262.03"))
        self.assertEqual(result.owner_assessment.status, "EXCLUDED")
        self.assertEqual(result.owner_assessment.removed_wages, Decimal("0.00"))
        self.assertEqual(result.employee_comparisons["M1"].status, "CHANGE")

    def test_affirmative_residential_construction_paraphrases_preserve_allocations(self):
        for activity in (
            "constructs detached family homes",
            "builds detached houses",
            "constructs single-family dwellings",
            "builds single family homes",
            "constructs detached dwellings",
            "CONSTRUCTS  DETACHED\nFAMILY HOMES",
        ):
            with self.subTest(activity=activity):
                text = BUSINESS.replace("Independent Homes", "Juniper Timber Co.").replace("builds single-family houses", activity)
                (self.employer / "business-description.md").write_text(text, encoding="utf-8")
                result = self.run_homes()
                # Fixture wages: field 100 + five-day manager 60; clerical 50+40.
                # Missing drywall proof adds 20.05 * 60% = 12.03; roofing stays OPEN.
                self.assertEqual(result.allocation.by_code, {"H-420": Decimal("160.00"), "C-110": Decimal("90.00")})
                self.assertEqual(result.by_code, {"H-420": Decimal("172.03"), "C-110": Decimal("90.00")})
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
                self.assertEqual(result.governing_field.class_code, "H-420")
                self.assertEqual(result.decisions["H1"].rationale_ref, "CG-15")
                self.assertTrue(result.combined_reconciliation.reconciled)

    def test_uncertain_or_planned_construction_activity_remains_open(self):
        for activity in (
            "may construct detached family homes",
            "plans to construct single-family houses",
            "possibly constructs single-family dwellings",
            "is unsure whether it constructs detached homes",
            "constructs detached homes, but that activity is unconfirmed",
        ):
            with self.subTest(activity=activity):
                (self.employer / "business-description.md").write_text(
                    BUSINESS.replace("builds single-family houses", activity), encoding="utf-8")
                result = self.run_homes()
                self.assertTrue(all(d.status == "OPEN" for d in result.decisions.values()))
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("250.00"))
                self.assertTrue(result.independent_reconciliation.reconciled)

    def test_negated_construction_paraphrases_cannot_establish_homebuilding(self):
        for activity in ("does not construct single-family dwellings", "never constructs detached family homes",
                         "no longer builds detached homes"):
            with self.subTest(activity=activity):
                (self.employer / "business-description.md").write_text(
                    BUSINESS.replace("builds single-family houses", activity), encoding="utf-8")
                result = self.run_homes()
                self.assertTrue(all(d.status == "OPEN" for d in result.decisions.values()))
                self.assertEqual(result.allocation.by_code, {})
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("250.00"))

    def test_unrelated_building_or_sales_activity_is_not_residential_construction(self):
        for activity in ("constructs commercial office buildings", "sells detached houses", "builds industrial equipment"):
            with self.subTest(activity=activity):
                (self.employer / "business-description.md").write_text(
                    BUSINESS.replace("builds single-family houses", activity), encoding="utf-8")
                result = self.run_homes()
                self.assertEqual(result.allocation.by_code, {})
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("250.00"))

    def test_customer_or_supplier_construction_does_not_establish_employer_activity(self):
        for activity in (
            "supplies a client who constructs detached homes",
            "serves customers whose company constructs single-family houses",
            "sells components to a supplier that builds detached dwellings",
        ):
            with self.subTest(activity=activity):
                (self.employer / "business-description.md").write_text(
                    BUSINESS.replace("builds single-family houses", activity), encoding="utf-8")
                result = self.run_homes()
                self.assertTrue(all(d.status == "OPEN" for d in result.decisions.values()))
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("250.00"))

    def test_construction_description_alone_does_not_replace_own_crew_evidence(self):
        text = BUSINESS.replace("builds single-family houses", "constructs detached homes").replace(
            "framing, drywall, finish carpentry and site labor with its own crew", "work performed entirely by other businesses")
        (self.employer / "business-description.md").write_text(text, encoding="utf-8")
        result = self.run_homes()
        self.assertTrue(all(d.status == "OPEN" for d in result.decisions.values()))
        self.assertEqual(result.allocation.by_code, {})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("250.00"))

    def test_mismatched_certificate_remains_open_with_original_identity_and_proposal(self):
        result = self.run_homes()
        line = next(line for line in result.adjustments.lines if line.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.input_record.subcontractor, "RoofBuild")
        self.assertEqual(line.certificates[0].subcontractor, "RoofBuild & Siding LLC")
        self.assertEqual(line.payroll_added, Decimal("0.00"))
        self.assertEqual(line.proposal.payroll_added, Decimal("18.00"))
        self.assertEqual(line.input_record.decision.class_code, "R-310")

    def test_capitalization_only_full_period_certificate_is_retrieved_but_stays_open(self):
        payment_path = self.employer / "subcontractor-payments.csv"
        certificate_path = self.employer / "insurance-certificates.csv"
        payment_text = PAYMENTS.replace("RoofBuild", "Copper Roofing LLC")
        certificate_text = CERTIFICATES.replace("RoofBuild & Siding LLC", "COPPER ROOFING LLC").replace("2025-06-30", "2025-12-31")
        payment_path.write_text(payment_text, encoding="utf-8")
        certificate_path.write_text(certificate_text, encoding="utf-8")
        result = self.run_homes()
        line = next(item for item in result.adjustments.lines if item.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.input_record.subcontractor, "Copper Roofing LLC")
        self.assertEqual(line.input_record.raw_record.values["subcontractor"], "Copper Roofing LLC")
        self.assertEqual(line.certificates[0].subcontractor, "COPPER ROOFING LLC")
        self.assertEqual(line.certificates[0].raw_record.values["subcontractor"], "COPPER ROOFING LLC")
        self.assertEqual((line.payroll_added, line.nonpayroll, line.unresolved_basis),
                         (Decimal("0.00"), Decimal("0.00"), Decimal("30.00")))
        self.assertEqual((line.proposal.payroll_added, line.proposal.nonpayroll),
                         (Decimal("18.00"), Decimal("12.00")))
        self.assertEqual((line.input_record.source.source, line.input_record.source.line_start), (str(payment_path), 4))
        self.assertEqual((line.certificates[0].source.source, line.certificates[0].source.line_start), (str(certificate_path), 3))
        self.assertIn(line.certificates[0].source, line.evidence_sources)
        self.assertTrue(line.required_confirmation)
        self.assertNotIn("R-310", result.adjustments.by_code)
        self.assertTrue(result.combined_reconciliation.reconciled)
        self.assertEqual(payment_path.read_text(), payment_text)
        self.assertEqual(certificate_path.read_text(), certificate_text)

    def test_capitalization_only_expired_certificate_keeps_identity_review_open(self):
        (self.employer / "insurance-certificates.csv").write_text(
            CERTIFICATES.replace("RoofBuild & Siding LLC", "ROOFBUILD"), encoding="utf-8")
        result = self.run_homes()
        line = next(item for item in result.adjustments.lines if item.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.input_record.subcontractor, "RoofBuild")
        self.assertEqual(line.certificates[0].subcontractor, "ROOFBUILD")
        self.assertEqual(line.certificates[0].coverage_to.isoformat(), "2025-06-30")
        self.assertEqual(line.payroll_added, Decimal("0.00"))
        self.assertEqual(line.unresolved_basis, Decimal("30.00"))
        self.assertEqual(line.proposal.payroll_added, Decimal("18.00"))
        self.assertTrue(line.required_confirmation)

    def test_exact_name_full_period_certificate_excludes_the_payment(self):
        (self.employer / "insurance-certificates.csv").write_text(
            CERTIFICATES.replace("RoofBuild & Siding LLC", "RoofBuild").replace("2025-06-30", "2025-12-31"), encoding="utf-8")
        result = self.run_homes()
        line = next(item for item in result.adjustments.lines if item.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "VERIFIED")
        self.assertEqual(line.input_record.subcontractor, line.certificates[0].subcontractor)
        self.assertEqual((line.payroll_added, line.nonpayroll, line.unresolved_basis),
                         (Decimal("0.00"), Decimal("30.00"), Decimal("0.00")))
        self.assertIsNone(line.proposal)
        self.assertNotIn("R-310", result.adjustments.by_code)

    def test_exact_name_expired_certificate_includes_all_invoice_sixty_percent(self):
        (self.employer / "insurance-certificates.csv").write_text(
            CERTIFICATES.replace("RoofBuild & Siding LLC", "RoofBuild"), encoding="utf-8")
        line = next(item for item in self.run_homes().adjustments.lines if item.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "VERIFIED")
        self.assertLess(line.input_record.payment_date, line.certificates[0].coverage_to)
        self.assertEqual((line.payroll_added, line.nonpayroll, line.unresolved_basis),
                         (Decimal("18.00"), Decimal("12.00"), Decimal("0.00")))
        self.assertEqual((line.class_code, line.rationale_ref), ("R-310", "CG-11"))
        self.assertIsNone(line.proposal)

    def test_missing_certificate_after_documented_search_adds_sixty_percent(self):
        (self.employer / "insurance-certificates.csv").write_text(
            "\n".join(CERTIFICATES.splitlines()[:2]) + "\n", encoding="utf-8")
        line = next(item for item in self.run_homes().adjustments.lines if item.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "VERIFIED")
        self.assertEqual(line.certificates, ())
        self.assertEqual((line.payroll_added, line.nonpayroll), (Decimal("18.00"), Decimal("12.00")))
        self.assertEqual((line.class_code, line.rationale_ref), ("R-310", "CG-11"))

    def test_distinct_business_name_candidate_is_not_accepted_as_identity(self):
        (self.employer / "subcontractor-payments.csv").write_text(
            PAYMENTS.replace("RoofBuild", "Copper Roofing LLC"), encoding="utf-8")
        (self.employer / "insurance-certificates.csv").write_text(
            CERTIFICATES.replace("RoofBuild & Siding LLC", "Copper Roofing Partners").replace("2025-06-30", "2025-12-31"), encoding="utf-8")
        line = next(item for item in self.run_homes().adjustments.lines if item.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.certificates[0].subcontractor, "Copper Roofing Partners")
        self.assertEqual(line.payroll_added, Decimal("0.00"))
        self.assertEqual(line.unresolved_basis, Decimal("30.00"))
        self.assertEqual(line.proposal.payroll_added, Decimal("18.00"))

    def test_unrelated_certificate_does_not_become_a_payee_identity_match(self):
        (self.employer / "insurance-certificates.csv").write_text(
            CERTIFICATES.replace("RoofBuild & Siding LLC", "Unrelated Plumbing LLC").replace("2025-06-30", "2025-12-31"), encoding="utf-8")
        line = next(item for item in self.run_homes().adjustments.lines if item.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "VERIFIED")
        self.assertEqual(line.certificates, ())
        self.assertEqual((line.payroll_added, line.nonpayroll), (Decimal("18.00"), Decimal("12.00")))

    def test_fractional_cent_sixty_percent_stays_exact_open_under_decimal_rounding_modes(self):
        # No confirmed rounding policy authorizes rounding 0.006 or 0.024 into
        # verified cents. Either rounding direction must preserve the proposal.
        for amount, proposed, nonpayroll in [("0.01", "0.006", "0.004"), ("0.04", "0.024", "0.016")]:
            for rounding in (ROUND_DOWN, ROUND_UP):
                with self.subTest(amount=amount, rounding=rounding):
                    (self.employer / "subcontractor-payments.csv").write_text(
                        "date,subcontractor,work,invoice,amount_paid\n"
                        f"2025-05-01,Fractional Roofing,roofing,CENT-1,{amount}\n", encoding="utf-8")
                    (self.employer / "insurance-certificates.csv").write_text(
                        "subcontractor,certificate_no,coverage_from,coverage_to\n", encoding="utf-8")
                    with localcontext() as context:
                        context.prec = 3
                        context.rounding = rounding
                        result = self.run_homes()
                    line, = result.adjustments.lines
                    self.assertEqual(line.status, "OPEN")
                    self.assertEqual((line.payroll_added, line.nonpayroll, line.unresolved_basis),
                                     (Decimal("0.00"), Decimal("0.00"), Decimal(amount)))
                    self.assertEqual((line.proposal.payroll_added, line.proposal.nonpayroll),
                                     (Decimal(proposed), Decimal(nonpayroll)))
                    self.assertEqual(line.proposal.payroll_added + line.proposal.nonpayroll, Decimal(amount))
                    self.assertTrue(any("round" in question.lower() for question in line.required_confirmation))
                    self.assertEqual(result.adjustments.by_code, {})
                    self.assertEqual(result.combined_reconciliation.confirmed_payroll, Decimal("250.00"))
                    self.assertTrue(result.adjustments.reconciliation.reconciled)
                    self.assertTrue(result.combined_reconciliation.reconciled)

    def test_exact_name_expired_certificate_adds_sixty_percent_even_before_lapse(self):
        path = self.employer / "insurance-certificates.csv"
        path.write_text(CERTIFICATES.replace("RoofBuild & Siding LLC", "RoofBuild"), encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(result.adjustments.by_code, {"H-420": Decimal("12.03"), "R-310": Decimal("18.00")})
        self.assertEqual(result.combined_reconciliation.confirmed_payroll, Decimal("280.03"))
        path.write_text(CERTIFICATES.replace("RoofBuild & Siding LLC", "RoofBuild").replace("2025-06-30", "2025-12-31"), encoding="utf-8")
        self.assertNotIn("R-310", self.run_homes().adjustments.by_code)

    def test_unrelated_missing_certificate_is_not_hidden_by_a_different_vendor_certificate(self):
        line = next(line for line in self.run_homes().adjustments.lines if line.adjustment_id == "DRY-1")
        self.assertEqual(line.status, "VERIFIED")
        self.assertEqual(line.class_code, "H-420")
        self.assertEqual(line.payroll_added, Decimal("12.03"))
        self.assertTrue(line.input_record.raw_record)
        self.assertTrue(any(ref.locator == "CG-06" for ref in line.rule_sources))

    def test_missing_inventory_is_unknown_not_a_documented_missing_certificate(self):
        (self.employer / "insurance-certificates.csv").unlink()
        result = self.run_homes()
        self.assertEqual(result.adjustments.reconciliation.payroll_added, Decimal("0.00"))
        self.assertEqual(result.adjustments.reconciliation.unresolved_basis, Decimal("100.05"))
        self.assertTrue(all(line.status == "OPEN" for line in result.adjustments.lines))

    def test_missing_payments_do_not_fabricate_a_confirmed_combined_total(self):
        (self.employer / "subcontractor-payments.csv").unlink()
        result = self.run_homes()
        self.assertIsNone(result.combined_reconciliation)
        self.assertTrue(result.open_items)

    def test_duplicate_invoice_is_a_source_error_without_a_partial_combined_total(self):
        path = self.employer / "subcontractor-payments.csv"
        path.write_text(PAYMENTS + PAYMENTS.splitlines()[1] + "\n", encoding="utf-8")
        result = self.run_homes()
        self.assertIsNone(result.combined_reconciliation)
        self.assertTrue(any("duplicate" in item.reason.lower() for item in result.open_items))

    def test_unknown_subcontractor_work_and_missing_certificate_dates_stay_open(self):
        path = self.employer / "subcontractor-payments.csv"
        path.write_text(PAYMENTS.replace("DryBuild,drywall", "DryBuild,unknown work"), encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(next(line for line in result.adjustments.lines if line.adjustment_id == "DRY-1").status, "OPEN")
        (self.employer / "insurance-certificates.csv").write_text(CERTIFICATES.replace("2025-12-31", ""), encoding="utf-8")
        self.assertEqual(next(line for line in self.run_homes().adjustments.lines if line.adjustment_id == "FRAME-1").status, "OPEN")

    def test_four_confirmed_visits_plus_an_unattributed_date_preserves_open_classification(self):
        self.set_visits(estimator=4)
        path = self.employer / "site-signin-log.csv"
        path.write_text(path.read_text().replace("County inspector", "Unidentified employee"), encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(result.decisions["E1"].status, "OPEN")
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("50.00"))
        self.assertEqual(result.combined_reconciliation.confirmed_payroll, Decimal("262.03"))
        self.assertEqual(result.combined_reconciliation.classified_payroll, Decimal("212.03"))
        self.assertEqual(result.proposals["E1"].class_code, "C-110")

    def test_four_employee_days_stay_clerical_and_five_assign_entire_wages_to_field(self):
        for days, code, paragraph in ((4, "C-110", "CG-04"), (5, "H-420", "CG-15")):
            with self.subTest(days=days):
                self.set_visits(estimator=days)
                path = self.employer / "site-signin-log.csv"
                path.write_text("".join(line for line in path.read_text().splitlines(keepends=True)
                                        if "County inspector" not in line), encoding="utf-8")
                result = self.run_homes()
                decision = result.decisions["E1"]
                self.assertEqual((decision.status, decision.class_code, decision.rationale_ref),
                                 ("CLASSIFIED", code, paragraph))
                self.assertEqual(len(result.site_visits["E1"]), days)
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
                self.assertEqual(result.allocation.by_code[code], Decimal("90.00") if days == 4 else Decimal("210.00"))
                self.assertTrue(result.independent_reconciliation.reconciled)

    def test_equivalent_estimator_measurement_visits_preserve_four_five_day_rule(self):
        for observation in (
            "For measurements, the estimator occasionally travels to a building site.",
            "The estimator sometimes visits construction sites to take measurements.",
            "To measure, the estimator periodically goes to job sites.",
            "The estimator travels to the site for measurements.",
            "THE ESTIMATOR\nVISITS A SITE NOW AND THEN TO MEASURE.",
        ):
            for days, code, paragraph, expected in (
                (4, "C-110", "CG-04", {"C-110": Decimal("90.00"), "H-420": Decimal("160.00")}),
                (5, "H-420", "CG-15", {"C-110": Decimal("40.00"), "H-420": Decimal("210.00")}),
            ):
                with self.subTest(observation=observation, days=days):
                    self.set_visits(estimator=days)
                    (self.employer / "field-notes.md").write_text(NOTES.replace(
                        "The estimator visits a site now and then to measure.", observation), encoding="utf-8")
                    result = self.run_homes()
                    # Independent control: carpenter 100, manager (five days) 60,
                    # bookkeeper 40, estimator 50 under the four/five-day rule.
                    decision = result.decisions["E1"]
                    self.assertEqual((decision.status, decision.class_code, decision.rationale_ref),
                                     ("CLASSIFIED", code, paragraph))
                    self.assertEqual(result.allocation.by_code, expected)
                    self.assertEqual(result.independent_reconciliation.register_total, Decimal("250.00"))
                    self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
                    self.assertTrue(result.independent_reconciliation.reconciled)
                    self.assertEqual(len(result.site_visits["E1"]), days)
                    self.assertTrue(any(ref.source == str(self.employer / "field-notes.md")
                                        and observation in ref.excerpt for ref in decision.evidence_sources))
                    self.assertTrue(any(ref.source == str(self.employer / "site-signin-log.csv")
                                        for ref in decision.evidence_sources))
                    self.assertTrue(any(ref.source == str(self.interview) for ref in decision.rule_sources))

    def test_estimator_title_or_measurement_words_do_not_establish_supported_duties(self):
        for observation in (
            "The estimator visits a building site.",
            "The estimator takes measurements.",
            "The estimator may travel to a building site for measurements.",
            "The estimator never travels to a building site for measurements.",
            "A customer says the estimator travels to a building site for measurements.",
            "The estimator travels to a site to measure and lay bricks.",
            "The estimator travels to building sites for measurements or other duties.",
            "",  # A payroll title and sign-ins cannot replace actual-duty evidence.
        ):
            with self.subTest(observation=observation):
                self.set_visits(estimator=4)
                (self.employer / "field-notes.md").write_text(NOTES.replace(
                    "The estimator visits a site now and then to measure.", observation), encoding="utf-8")
                result = self.run_homes()
                self.assertEqual((result.decisions["E1"].status, result.decisions["E1"].class_code), ("OPEN", None))
                self.assertTrue(result.decisions["E1"].required_confirmation)
                self.assertTrue(any("[E1]" in item.subject and item.required_confirmation for item in result.open_items))
                self.assertTrue(result.independent_reconciliation.reconciled)

    def test_additional_conflicting_estimator_duties_override_supported_visit_sentence(self):
        for observation in (
            "The estimator lays bricks at the sites.",
            "The estimator also performs landscaping.",
            "The estimator may perform other duties outside the office.",
        ):
            with self.subTest(observation=observation):
                self.set_visits(estimator=4)
                (self.employer / "field-notes.md").write_text(NOTES + observation + "\n", encoding="utf-8")
                result = self.run_homes()
                self.assertEqual((result.decisions["E1"].status, result.decisions["E1"].class_code), ("OPEN", None))
                self.assertTrue(result.decisions["E1"].required_confirmation)
                self.assertTrue(result.independent_reconciliation.reconciled)

    def test_paraphrased_estimator_duties_do_not_resolve_missing_or_ambiguous_visits(self):
        (self.employer / "field-notes.md").write_text(NOTES.replace(
            "The estimator visits a site now and then to measure.",
            "For measurements, the estimator occasionally travels to a building site."), encoding="utf-8")
        for issue in ("unidentified", "conflicting identity", "incomplete", "missing"):
            with self.subTest(issue=issue):
                self.set_visits(estimator=4)
                path = self.employer / "site-signin-log.csv"
                text = path.read_text()
                if issue == "unidentified":
                    path.write_text(text.replace("County inspector", "Unidentified employee"), encoding="utf-8")
                elif issue == "conflicting identity":
                    path.write_text(text.replace("E1,Estimator One", "E1,Unknown Person", 1), encoding="utf-8")
                elif issue == "incomplete":
                    path.write_text(text + "2025-04-16,E1,Estimator One,Site A,\n", encoding="utf-8")
                else:
                    path.unlink()
                result = self.run_homes()
                self.assertEqual((result.decisions["E1"].status, result.decisions["E1"].class_code), ("OPEN", None))
                self.assertTrue(result.decisions["E1"].required_confirmation)
                self.assertTrue(result.independent_reconciliation.reconciled)
                if issue == "unidentified":
                    self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("50.00"))
                    self.assertEqual(result.proposals["E1"].class_code, "C-110")
                    self.assertEqual(result.proposals["E1"].wages, Decimal("50.00"))

    def test_estimator_measurement_observation_cannot_identify_multiple_estimators(self):
        (self.employer / "field-notes.md").write_text(NOTES.replace(
            "The estimator visits a site now and then to measure.",
            "The estimator visits construction sites for measurements."), encoding="utf-8")
        (self.employer / "payroll-register.csv").write_text(
            PAYROLL + "E2,Another Person,Estimator,8.01\n", encoding="utf-8")
        result = self.run_homes()
        for key in ("E1", "E2"):
            self.assertEqual((result.decisions[key].status, result.decisions[key].class_code), ("OPEN", None))
            self.assertTrue(result.decisions[key].required_confirmation)
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("258.01"))
        self.assertTrue(result.independent_reconciliation.reconciled)

    def test_documented_external_inspectors_do_not_add_an_employee_day_and_remain_reviewable(self):
        for label in ("County inspector", "City inspector", "Municipal building inspector"):
            with self.subTest(visitor=label):
                self.set_visits(estimator=4)
                path = self.employer / "site-signin-log.csv"
                path.write_text(path.read_text().replace("County inspector", label), encoding="utf-8")
                result = self.run_homes()
                self.assertEqual(result.decisions["E1"].class_code, "C-110")
                self.assertEqual(result.allocation.by_code["C-110"], Decimal("90.00"))
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
                self.assertNotIn("E1", result.proposals)
                ref, = result.unassigned_site_records
                self.assertEqual(ref.source, str(path))
                self.assertIn(f"2025-04-15,,{label},Site A,11:00", ref.excerpt)
                self.assertIn(ref, result.decisions["E1"].evidence_sources)
                visitor_questions = [item for item in result.open_items
                                     if ref in item.sources and "external" in item.reason.lower()]
                self.assertTrue(visitor_questions, "The external record still requires employer confirmation")
                self.assertTrue(all(item.required_confirmation for item in visitor_questions))

    def test_repeated_employee_entries_and_external_inspection_do_not_create_a_fifth_day(self):
        self.set_visits(estimator=4)
        path = self.employer / "site-signin-log.csv"
        path.write_text(path.read_text() + "2025-02-04,E1,Estimator One,Site B,14:00\n", encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(len(result.site_visits["E1"]), 4)
        self.assertEqual(result.decisions["E1"].class_code, "C-110")

    def test_unknown_person_or_unspecified_inspector_cannot_be_assumed_external(self):
        for label in ("", "Unidentified employee", "Visitor Person", "Inspector"):
            with self.subTest(visitor=label):
                self.set_visits(estimator=4)
                path = self.employer / "site-signin-log.csv"
                path.write_text(path.read_text().replace("County inspector", label), encoding="utf-8")
                result = self.run_homes()
                self.assertEqual(result.decisions["E1"].status, "OPEN")
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("50.00"))
                self.assertEqual(result.proposals["E1"].class_code, "C-110")
                self.assertEqual(result.combined_reconciliation.classified_payroll, Decimal("212.03"))

    def test_external_role_with_employee_id_name_conflict_keeps_office_payroll_open(self):
        self.set_visits(estimator=4)
        path = self.employer / "site-signin-log.csv"
        path.write_text(path.read_text().replace(",,County inspector,", ",E1,County inspector,"), encoding="utf-8")
        result = self.run_homes()
        self.assertTrue(all(result.decisions[key].status == "OPEN" for key in ("E1", "M1", "B1")))
        self.assertTrue(any("conflict" in result.decisions[key].reason for key in ("E1", "M1", "B1")))

    def test_unknown_nonblank_employee_id_does_not_authorize_external_visitor_exclusion(self):
        self.set_visits(estimator=4)
        path = self.employer / "site-signin-log.csv"
        path.write_text(path.read_text().replace(",,County inspector,", ",UNKNOWN-ID,County inspector,"), encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(result.decisions["E1"].status, "OPEN")
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("50.00"))

    def test_external_role_matching_a_registered_name_remains_an_ambiguous_identity(self):
        self.set_visits(estimator=4)
        path = self.employer / "payroll-register.csv"
        path.write_text(PAYROLL.replace("Books One", "County inspector"), encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(result.decisions["E1"].status, "OPEN")
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("50.00"))

    def test_external_visitors_do_not_resolve_missing_employee_signin_pages(self):
        self.set_visits(estimator=4)
        (self.employer / "field-notes.md").write_text(NOTES + "Some sign-in pages are missing.\n", encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(result.decisions["E1"].status, "OPEN")
        self.assertTrue(result.decisions["E1"].required_confirmation)

    def test_external_label_cannot_override_conflicting_employer_identity_evidence(self):
        self.set_visits(estimator=4)
        for statement in ("The County inspector entry was signed by Estimator One.",
                          "The 2025-04-15 sign-in with no employee ID belongs to Estimator One.",
                          "The inspector who signed in on 2025-04-15 was Estimator One."):
            with self.subTest(identity_evidence=statement):
                (self.employer / "field-notes.md").write_text(NOTES + statement + "\n", encoding="utf-8")
                result = self.run_homes()
                self.assertEqual(result.decisions["E1"].status, "OPEN")
                self.assertTrue(result.decisions["E1"].required_confirmation)

    def test_owner_exclusion_requires_the_documented_election_and_consistent_register(self):
        path = self.employer / "business-description.md"
        path.write_text(BUSINESS.replace("has filed an election of exclusion", "has not filed an election of exclusion"), encoding="utf-8")
        self.assertEqual(self.run_homes().owner_assessment.status, "OPEN")
        path.write_text(BUSINESS, encoding="utf-8")
        (self.employer / "payroll-register.csv").write_text(PAYROLL + "OWN,Excluded Person,Owner,10.00\n", encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(result.owner_assessment.status, "OPEN")
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("260.00"))
        self.assertEqual(result.decisions["OWN"].status, "OPEN")

    def test_competing_unresolved_subcontractor_exposure_cannot_silently_choose_governing_code(self):
        (self.employer / "subcontractor-payments.csv").write_text(PAYMENTS.replace("ROOF-1,30.00", "ROOF-1,1000.00"), encoding="utf-8")
        result = self.run_homes()
        self.assertIsNone(result.governing_field.class_code)
        self.assertEqual(result.decisions["M1"].status, "OPEN")

    def test_configurable_sources_reread_and_keep_low_precision_cents_exact(self):
        (self.employer / "subcontractor-payments.csv").rename(self.employer / "invoices.csv")
        files = replace(EmployerFiles(), subcontractor_payments="invoices.csv")
        with localcontext() as context:
            context.prec = 3
            result = self.run_homes(files=files)
        self.assertEqual(result.adjustments.reconciliation.payroll_added, Decimal("12.03"))
        self.assertEqual(result.combined_reconciliation.confirmed_payroll, Decimal("262.03"))
        self.assertTrue(all(line.input_record.source.source.endswith("invoices.csv") for line in result.adjustments.lines))

    def test_negated_homebuilding_business_cannot_authorize_duty_classifications(self):
        (self.employer / "business-description.md").write_text(BUSINESS.replace("builds single-family houses", "no longer builds single-family houses"), encoding="utf-8")
        self.assertTrue(all(decision.status == "OPEN" for decision in self.run_homes().decisions.values()))

    def test_physical_office_duty_exception_requires_human_review(self):
        (self.employer / "field-notes.md").write_text(NOTES + "The bookkeeper also installs roofs.\n", encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(result.decisions["B1"].status, "OPEN")
        self.assertTrue(result.decisions["B1"].required_confirmation)

    def test_explicit_missing_signin_pages_cannot_verify_office_day_bounds(self):
        (self.employer / "field-notes.md").write_text(NOTES + "Some sign-in pages are missing.\n", encoding="utf-8")
        result = self.run_homes()
        self.assertTrue(all(result.decisions[key].status == "OPEN" for key in ("E1", "M1", "B1")))

    def test_missing_payments_prevent_definitive_comparison_even_with_all_employee_codes(self):
        (self.employer / "subcontractor-payments.csv").unlink()
        path = self.employer / "site-signin-log.csv"
        path.write_text("".join(line for line in path.read_text().splitlines(keepends=True) if not any(value in line for value in ("2025-03-04", "2025-03-05", "County inspector"))), encoding="utf-8")
        result = self.run_homes()
        self.assertTrue(all(decision.status == "CLASSIFIED" for decision in result.decisions.values()))
        self.assertIsNone(result.combined_reconciliation)
        self.assertFalse(result.application.definitive)

    def test_empty_critical_monetary_tables_cannot_confirm_zero_original_basis(self):
        for filename, original in (("payroll-register.csv", PAYROLL), ("subcontractor-payments.csv", PAYMENTS)):
            with self.subTest(filename=filename):
                path = self.employer / filename
                path.write_text(original.splitlines()[0] + "\n", encoding="utf-8")
                try:
                    result = self.run_homes()
                    self.assertIsNone(result.combined_reconciliation)
                    self.assertTrue(result.open_items)
                finally:
                    path.write_text(original, encoding="utf-8")

    def test_empty_signin_log_conflicts_with_observed_visits(self):
        (self.employer / "site-signin-log.csv").write_text(SITE_HEADER, encoding="utf-8")
        result = self.run_homes()
        self.assertTrue(all(result.decisions[key].status == "OPEN" for key in ("E1", "M1", "B1")))

    def test_negated_certificate_search_does_not_verify_missing_coverage(self):
        (self.employer / "field-notes.md").write_text(NOTES.replace("collected the certificates", "have not collected the certificates"), encoding="utf-8")
        line = next(line for line in self.run_homes().adjustments.lines if line.adjustment_id == "DRY-1")
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.payroll_added, Decimal("0.00"))

    def test_named_work_conflicts_cannot_be_overridden_by_titles_or_invoice_work(self):
        path = self.employer / "field-notes.md"
        path.write_text(NOTES + "Field One performs roofing throughout the audit period.\nDryBuild performed only roofing work during this audit period.\n", encoding="utf-8")
        result = self.run_homes()
        self.assertEqual(result.decisions["H1"].status, "OPEN")
        line = next(line for line in result.adjustments.lines if line.adjustment_id == "DRY-1")
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.payroll_added, Decimal("0.00"))

    def test_revoked_election_cannot_authorize_owner_exclusion(self):
        (self.employer / "business-description.md").write_text(BUSINESS + "The election of exclusion was revoked before the audit period began.\n", encoding="utf-8")
        self.assertEqual(self.run_homes().owner_assessment.status, "OPEN")

    def test_similar_leading_certificate_name_stays_open_without_identity_assumption(self):
        (self.employer / "subcontractor-payments.csv").write_text(PAYMENTS.replace("RoofBuild", "Harbor Island Roofing"), encoding="utf-8")
        (self.employer / "insurance-certificates.csv").write_text(CERTIFICATES.replace("RoofBuild & Siding LLC", "Harbor Island Roof & Siding LLC"), encoding="utf-8")
        line = next(line for line in self.run_homes().adjustments.lines if line.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.certificates[0].subcontractor, "Harbor Island Roof & Siding LLC")
        self.assertEqual(line.payroll_added, Decimal("0.00"))

    def test_negated_construction_observation_prevents_field_duty_confirmation(self):
        (self.employer / "field-notes.md").write_text(NOTES.replace("three houses under construction", "no houses under construction"), encoding="utf-8")
        self.assertEqual(self.run_homes().decisions["H1"].status, "OPEN")

    def test_zero_observed_visits_cite_the_examined_complete_log(self):
        path = self.employer / "site-signin-log.csv"
        path.write_text("".join(line for line in path.read_text().splitlines(keepends=True) if "County inspector" not in line), encoding="utf-8")
        refs = self.run_homes().decisions["B1"].evidence_sources
        self.assertTrue(any(ref.source == str(path) and ref.line_start == 1 and "Manager One" in ref.excerpt for ref in refs))


class LocalSevernIntegrationTest(unittest.TestCase):
    def test_actual_employees_all_eight_payments_and_separate_reconciliations(self):
        root = Path(os.environ.get("INSURANCE01_TEST_INPUTS", "/home/maxg/insurance01-inputs"))
        interview = COMPONENT.parents[1] / "interviews" / "ch03-premium-audit-20261105-0222(1).md"
        if not root.is_dir() or not interview.is_file():
            self.skipTest("Authoritative local development snapshots are unavailable")
        employer = root / "employer-files" / "severn-homebuilders"
        result = process_employer(root / "classification-guide.md", employer, interview)
        self.assertEqual(result.allocation.by_code, {"H-420": Decimal("344511.00"), "C-110": Decimal("117368.70")})
        self.assertEqual((result.decisions["SH-E06"].status, result.decisions["SH-E06"].class_code,
                          result.decisions["SH-E06"].rationale_ref), ("CLASSIFIED", "C-110", "CG-04"))
        self.assertEqual(result.decisions["SH-E07"].class_code, "H-420")
        self.assertEqual(len(result.site_visits["SH-E06"]), 4)
        self.assertEqual(len(result.site_visits["SH-E07"]), 11)
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("461879.70"))
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
        self.assertEqual(len(result.adjustments.lines), 8)
        self.assertEqual(result.adjustments.by_code, {"H-420": Decimal("24693.39")})
        self.assertEqual(result.adjustments.reconciliation.basis_total, Decimal("152117.05"))
        self.assertEqual(result.adjustments.reconciliation.nonpayroll, Decimal("81478.01"))
        self.assertEqual(result.adjustments.reconciliation.unresolved_basis, Decimal("45945.65"))
        self.assertEqual(result.by_code, {"H-420": Decimal("369204.39"), "C-110": Decimal("117368.70")})
        self.assertEqual(result.combined_reconciliation.confirmed_payroll, Decimal("486573.09"))
        self.assertEqual(result.combined_reconciliation.classified_payroll, Decimal("486573.09"))
        self.assertTrue(result.combined_reconciliation.reconciled)
        self.assertTrue(result.independent_reconciliation.reconciled)
        self.assertTrue(result.adjustments.reconciliation.reconciled)
        proposed = sum(line.proposal.payroll_added for line in result.adjustments.lines if line.proposal)
        self.assertEqual(proposed, Decimal("27567.39"))
        self.assertEqual(result.owner_assessment.status, "EXCLUDED")
        wages = list(csv.DictReader(io.StringIO((employer / "payroll-register.csv").read_text())))
        payments = list(csv.DictReader(io.StringIO((employer / "subcontractor-payments.csv").read_text())))
        self.assertEqual(sum(Decimal(row["wages_paid"]) for row in wages), Decimal("461879.70"))
        self.assertEqual(sum(Decimal(row["amount_paid"]) for row in payments), Decimal("152117.05"))


if __name__ == "__main__":
    unittest.main()
