"""End-to-end homebuilding and subcontractor evidence, without identity guesses."""

from dataclasses import replace
from decimal import Decimal, localcontext
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

    def test_mismatched_certificate_remains_open_with_original_identity_and_proposal(self):
        result = self.run_homes()
        line = next(line for line in result.adjustments.lines if line.adjustment_id == "ROOF-1")
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.input_record.subcontractor, "RoofBuild")
        self.assertEqual(line.certificates[0].subcontractor, "RoofBuild & Siding LLC")
        self.assertEqual(line.payroll_added, Decimal("0.00"))
        self.assertEqual(line.proposal.payroll_added, Decimal("18.00"))
        self.assertEqual(line.input_record.decision.class_code, "R-310")

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
        result = self.run_homes()
        self.assertEqual(result.decisions["E1"].status, "OPEN")
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("50.00"))
        self.assertEqual(result.combined_reconciliation.confirmed_payroll, Decimal("262.03"))
        self.assertEqual(result.combined_reconciliation.classified_payroll, Decimal("212.03"))
        self.assertEqual(result.proposals["E1"].class_code, "C-110")

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
        self.assertEqual(result.allocation.by_code, {"H-420": Decimal("344511.00"), "C-110": Decimal("46118.25")})
        self.assertEqual(result.decisions["SH-E06"].status, "OPEN")
        self.assertEqual(result.decisions["SH-E07"].class_code, "H-420")
        self.assertEqual(len(result.site_visits["SH-E06"]), 4)
        self.assertEqual(len(result.site_visits["SH-E07"]), 11)
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("461879.70"))
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("71250.45"))
        self.assertEqual(len(result.adjustments.lines), 8)
        self.assertEqual(result.adjustments.by_code, {"H-420": Decimal("24693.39")})
        self.assertEqual(result.adjustments.reconciliation.basis_total, Decimal("152117.05"))
        self.assertEqual(result.adjustments.reconciliation.nonpayroll, Decimal("81478.01"))
        self.assertEqual(result.adjustments.reconciliation.unresolved_basis, Decimal("45945.65"))
        self.assertEqual(result.by_code, {"H-420": Decimal("369204.39"), "C-110": Decimal("46118.25")})
        self.assertEqual(result.combined_reconciliation.confirmed_payroll, Decimal("486573.09"))
        self.assertEqual(result.combined_reconciliation.classified_payroll, Decimal("415322.64"))
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
