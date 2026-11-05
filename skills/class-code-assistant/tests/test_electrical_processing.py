"""Electrical duties, included owners and independently reconciled travel pay."""

from dataclasses import replace
from decimal import Decimal, localcontext
import csv
import hashlib
import os
from pathlib import Path
import sys
import tempfile
import unittest

COMPONENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPONENT))
from employer_processing import EmployerFiles, process_employer
from test_homebuilding_processing import GUIDE as HOME_GUIDE
from test_payroll_adjustments import INTERVIEW

GUIDE = HOME_GUIDE + """
**CG-21. E-510 Electrical wiring.** Installation and repair of electrical wiring and fixtures inside buildings,
including service connections.
"""
BUSINESS = """# Independent Electric
Audit period January 1, 2025 to December 31, 2025.
Independent Electric does residential and light commercial wiring in Example County, plus a few out-of-town jobs a year.
Four people on the payroll register, including the owner, Owner Person, who has not filed an election of exclusion.
No subcontractors in the period.
"""
NOTES = """# Auditor field notes
Shop and office in Example Town. The owner, Owner Person, leads a crew on site most days
and pulls wire himself; the office administrator, Office Person, runs the office and never goes to jobs.
Some of the electricians spent weeks on an out-of-town job in Elsewhere; they were paid a flat amount per day away on top of
wages, shown in its own column of the payroll register.
"""
PAYROLL = """employee_id,name,position,wages_paid,travel_days,travel_allowance_paid
O1,Owner Person,"Owner, Master Electrician",100.00,0,0.00
F1,Field Person,Journeyman Electrician,50.05,2,100.00
A1,Apprentice Person,Apprentice Electrician,30.03,0,3.90
C1,Office Person,Office Administrator,20.02,0,0.00
"""
APPLICATION = """# Application
| Class code (employer's choice) | Employees | Payroll (USD) |
|---|---|---|
| E-510 | 2 | 80.08 |
| C-110 | 2 | 120.02 |
"""
SIGNINS = """date,employee_id,name,site,signed_in_at
2025-02-03,O1,Owner Person,Example Site,08:30
"""


class ElectricalIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.employer = self.root / "unrelated-electrical-inputs"
        self.employer.mkdir()
        self.guide = self.root / "guide.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview = self.root / "interview.md"
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        for name, text in {"business-description.md": BUSINESS, "field-notes.md": NOTES,
            "payroll-register.csv": PAYROLL, "application.md": APPLICATION, "site-signin-log.csv": SIGNINS}.items():
            (self.employer / name).write_text(text, encoding="utf-8")

    def run_electric(self, **kwargs):
        return process_employer(self.guide, self.employer, self.interview, **kwargs)

    def allowance(self, result, employee="F1"):
        return next(line for line in result.adjustments.lines if line.input_record.employee_id == employee)

    def test_owner_duties_verified_travel_and_separate_reconciliations(self):
        result = self.run_electric()
        self.assertEqual(result.allocation.by_code, {"E-510": Decimal("180.08"), "C-110": Decimal("20.02")})
        self.assertEqual(result.by_code, {"E-510": Decimal("186.08"), "C-110": Decimal("20.02")})
        self.assertEqual(result.owner_assessment.status, "INCLUDED")
        self.assertEqual(result.owner_assessment.removed_wages, Decimal("0.00"))
        self.assertTrue(any(ref.locator == "CG-05" for ref in result.decisions["O1"].rule_sources))
        self.assertTrue(result.independent_reconciliation.reconciled)
        self.assertTrue(result.adjustments.reconciliation.reconciled)
        self.assertTrue(result.travel_reconciliation.reconciled)
        self.assertEqual(result.travel_reconciliation.known_payroll, Decimal("206.10"))
        self.assertEqual(result.travel_reconciliation.cash_total, Decimal("304.00"))
        self.assertEqual(result.travel_reconciliation.cash_difference, Decimal("0.00"))
        self.assertEqual(result.employee_comparisons["O1"].status, "CHANGE")
        self.assertEqual(result.application.verified_differences, {"E-510": Decimal("106.00"), "C-110": Decimal("-100.00")})

    def test_zero_day_payment_stays_open_with_separate_proposal_and_questions(self):
        result = self.run_electric()
        line = self.allowance(result, "A1")
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.payroll_added, Decimal("0.00"))
        self.assertEqual(line.unresolved_basis, Decimal("3.90"))
        self.assertEqual(line.proposal.payroll_added, Decimal("3.90"))
        self.assertEqual(line.input_record.decision.class_code, "E-510")
        questions = " ".join(line.required_confirmation).lower()
        self.assertTrue(all(word in questions for word in ("days", "purpose", "wages")))
        self.assertFalse(result.application.definitive)
        self.assertEqual(result.adjustments.reconciliation.unresolved_basis, Decimal("3.90"))

    def test_daily_cap_below_at_and_above_boundary_is_exact(self):
        path = self.employer / "payroll-register.csv"
        for amount, added, excluded in (("93.98", "0.00", "93.98"), ("94.00", "0.00", "94.00"), ("94.02", "0.02", "94.00")):
            with self.subTest(amount=amount):
                path.write_text(PAYROLL.replace("50.05,2,100.00", f"50.05,2,{amount}"), encoding="utf-8")
                line = self.allowance(self.run_electric())
                self.assertEqual(line.status, "VERIFIED")
                self.assertEqual(line.payroll_added, Decimal(added))
                self.assertEqual(line.nonpayroll, Decimal(excluded))

    def test_fractional_cent_daily_rate_is_open_without_rounding_or_averaging(self):
        (self.employer / "payroll-register.csv").write_text(PAYROLL.replace("50.05,2,100.00", "50.05,2,94.01"), encoding="utf-8")
        self.assertEqual(self.allowance(self.run_electric()).status, "OPEN")

    def test_variable_or_negated_flat_rate_cannot_authorize_daily_exclusions(self):
        path = self.employer / "field-notes.md"
        for text in (NOTES.replace("a flat amount", "variable amounts"), NOTES.replace("were paid a flat", "were not paid a flat"), NOTES + "The daily amounts varied from day to day.\n", NOTES + "Travel payments were not a flat amount per day.\n"):
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                line = self.allowance(self.run_electric())
                self.assertEqual(line.status, "OPEN")
                self.assertEqual(line.nonpayroll, Decimal("0.00"))

    def test_missing_or_conflicting_wage_separation_prevents_double_counting(self):
        path = self.employer / "field-notes.md"
        for text in (NOTES.replace("on top of\nwages", "with inclusion in wages unconfirmed"), NOTES + "Travel_allowance_paid is already included in wages_paid.\n", NOTES.replace("on top of\nwages", "not on top of wages")):
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                result = self.run_electric()
                self.assertEqual(result.adjustments.reconciliation.payroll_added, Decimal("0.00"))
                self.assertEqual(self.allowance(result).status, "OPEN")
                self.assertIsNone(result.travel_reconciliation.cash_total)

    def test_missing_allowance_columns_prevent_a_fabricated_complete_zero_adjustment(self):
        (self.employer / "payroll-register.csv").write_text("employee_id,name,position,wages_paid\nO1,Owner Person,Master Electrician,100.00\n", encoding="utf-8")
        result = self.run_electric()
        self.assertIsNone(result.travel_reconciliation)
        self.assertTrue(result.open_items)
        self.assertFalse(result.application.definitive)

    def test_invalid_or_missing_day_counts_keep_original_money_open(self):
        path = self.employer / "payroll-register.csv"
        for days in ("", "-1", "1.5", "999"):
            with self.subTest(days=days):
                path.write_text(PAYROLL.replace("50.05,2,100.00", f"50.05,{days},100.00"), encoding="utf-8")
                line = self.allowance(self.run_electric())
                self.assertEqual(line.status, "OPEN")
                self.assertEqual(line.unresolved_basis, Decimal("100.00"))

    def test_owner_requires_no_exclusion_matching_identity_and_wiring_observation(self):
        path = self.employer / "business-description.md"
        for text in (BUSINESS.replace("has not filed", "has filed"), BUSINESS.replace("owner, Owner Person", "owner, Different Person")):
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                result = self.run_electric()
                self.assertEqual(result.decisions["O1"].status, "OPEN")
                self.assertEqual(result.owner_assessment.status, "OPEN")
                self.assertEqual(result.independent_reconciliation.register_total, Decimal("200.10"))
        path.write_text(BUSINESS, encoding="utf-8")
        (self.employer / "field-notes.md").write_text(NOTES.replace("and pulls wire himself", "and never does electrical work himself"), encoding="utf-8")
        self.assertEqual(self.run_electric().decisions["O1"].status, "OPEN")

    def test_office_class_requires_named_affirmative_notes_and_no_site_conflict(self):
        path = self.employer / "field-notes.md"
        path.write_text(NOTES.replace("never goes to jobs", "sometimes goes to jobs"), encoding="utf-8")
        self.assertEqual(self.run_electric().decisions["C1"].status, "OPEN")
        path.write_text(NOTES, encoding="utf-8")
        (self.employer / "site-signin-log.csv").write_text(SIGNINS + "2025-02-04,C1,Office Person,Example Site,09:00\n", encoding="utf-8")
        self.assertEqual(self.run_electric().decisions["C1"].status, "OPEN")

    def test_unknown_or_conflicting_employee_duties_cannot_supply_an_allowance_code(self):
        path = self.employer / "payroll-register.csv"
        path.write_text(PAYROLL.replace("Field Person,Journeyman Electrician", "Field Person,Accountant"), encoding="utf-8")
        result = self.run_electric()
        self.assertEqual(result.decisions["F1"].status, "OPEN")
        self.assertEqual(self.allowance(result).status, "OPEN")
        self.assertEqual(self.allowance(result).payroll_added, Decimal("0.00"))
        path.write_text(PAYROLL, encoding="utf-8")
        (self.employer / "field-notes.md").write_text(NOTES + "Field Person performs only clerical bookkeeping.\n", encoding="utf-8")
        self.assertEqual(self.run_electric().decisions["F1"].status, "OPEN")

    def test_changed_guide_and_travel_interview_rules_require_fresh_review(self):
        self.guide.write_text(GUIDE.replace("Installation and repair of electrical wiring", "UNVERIFIED NEW ELECTRICAL POLICY"), encoding="utf-8")
        self.assertEqual(self.run_electric().decisions["F1"].status, "OPEN")
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview.write_text(INTERVIEW.replace("forty-seven dollars", "fifty dollars"), encoding="utf-8")
        self.assertEqual(self.allowance(self.run_electric()).status, "OPEN")

    def test_missing_empty_or_conflicting_site_records_never_invent_identities(self):
        path = self.employer / "site-signin-log.csv"
        for text in (SIGNINS.splitlines()[0] + "\n", SIGNINS.replace("O1,Owner Person", "O1,Another Person"), SIGNINS + "2025-02-04,,Visitor,Example Site,09:00\n"):
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                result = self.run_electric()
                self.assertTrue(result.open_items)
                self.assertNotIn("Visitor", result.decisions)
                if "Another Person" in text:
                    self.assertEqual(result.decisions["O1"].status, "OPEN")

    def test_original_rows_and_exact_rule_citations_are_preserved(self):
        result = self.run_electric()
        self.assertEqual(len(result.adjustments.lines), 4)
        line = self.allowance(result)
        self.assertEqual(line.input_record.raw_record.values["travel_allowance_paid"], Decimal("100.00"))
        self.assertEqual(line.input_record.uniform_daily_amount, Decimal("50.00"))
        self.assertTrue(line.input_record.separate_from_base)
        self.assertTrue(any(ref.locator == "CG-03" for ref in line.rule_sources))
        self.assertTrue(any(ref.locator == "CG-21" for ref in line.rule_sources))
        self.assertTrue(any(ref.locator == "Nadia Brennan · 06:05 PM" for ref in line.rule_sources))
        for ref in (*line.evidence_sources, *line.rule_sources):
            self.assertEqual(ref.sha256, hashlib.sha256(Path(ref.source).read_bytes()).hexdigest())

    def test_configurable_sources_reread_and_low_decimal_precision_preserve_cents(self):
        (self.employer / "payroll-register.csv").rename(self.employer / "wages.csv")
        (self.employer / "site-signin-log.csv").rename(self.employer / "visits.csv")
        files = replace(EmployerFiles(), payroll="wages.csv", site_signins="visits.csv")
        with localcontext() as context:
            context.prec = 3
            result = self.run_electric(files=files)
        self.assertEqual(result.travel_reconciliation.known_payroll, Decimal("206.10"))
        path = self.employer / "wages.csv"
        path.write_text(path.read_text().replace("50.05,2,100.00", "50.05,2,94.00"), encoding="utf-8")
        self.assertEqual(self.run_electric(files=files).adjustments.reconciliation.payroll_added, Decimal("0.00"))

    def test_missing_notes_empty_register_and_duplicate_employee_sources_are_open(self):
        path = self.employer / "field-notes.md"
        path.unlink()
        result = self.run_electric()
        self.assertTrue(result.open_items)
        self.assertEqual(result.adjustments.reconciliation.payroll_added, Decimal("0.00"))
        path.write_text(NOTES, encoding="utf-8")
        path = self.employer / "payroll-register.csv"
        for text in (PAYROLL.splitlines()[0] + "\n", PAYROLL + PAYROLL.splitlines()[2] + "\n"):
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                result = self.run_electric()
                self.assertIsNone(result.allocation)
                self.assertTrue(result.open_items)

    def test_business_description_conflicts_cannot_be_overridden_by_field_notes(self):
        path = self.employer / "business-description.md"
        for statement, duty_conflict in (("Travel_allowance_paid is already included in wages_paid.", False), ("Field Person performs only clerical bookkeeping.", True)):
            with self.subTest(statement=statement):
                path.write_text(BUSINESS + statement + "\n", encoding="utf-8")
                result = self.run_electric()
                self.assertEqual(self.allowance(result).status, "OPEN")
                self.assertEqual(self.allowance(result).payroll_added, Decimal("0.00"))
                if duty_conflict:
                    self.assertEqual(result.decisions["F1"].status, "OPEN")
                else:
                    self.assertIsNone(result.travel_reconciliation.cash_total)

    def test_conflicting_positive_election_statement_keeps_owner_and_wages_open(self):
        (self.employer / "business-description.md").write_text(BUSINESS + "The owner has since filed an election of exclusion.\n", encoding="utf-8")
        result = self.run_electric()
        self.assertEqual(result.owner_assessment.status, "OPEN")
        self.assertEqual(result.decisions["O1"].status, "OPEN")
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("200.10"))

    def test_disclosed_incomplete_travel_counts_prevent_even_below_cap_exclusions(self):
        (self.employer / "payroll-register.csv").write_text(PAYROLL.replace("50.05,2,100.00", "50.05,2,94.00"), encoding="utf-8")
        path = self.employer / "field-notes.md"
        for statement in ("The travel-day counts omit several trips.", "The travel-day count is incomplete."):
            with self.subTest(statement=statement):
                path.write_text(NOTES + statement + "\n", encoding="utf-8")
                line = self.allowance(self.run_electric())
                self.assertFalse(line.input_record.days_complete)
                self.assertEqual(line.status, "OPEN")
                self.assertEqual(line.nonpayroll, Decimal("0.00"))

    def test_missing_site_pages_prevent_office_zero_visit_confirmation(self):
        (self.employer / "field-notes.md").write_text(NOTES + "Several site sign-in pages are missing.\n", encoding="utf-8")
        result = self.run_electric()
        self.assertEqual(result.decisions["C1"].status, "OPEN")
        self.assertTrue(result.decisions["C1"].required_confirmation)

    def test_collective_office_duty_exception_prevents_field_title_classification(self):
        (self.employer / "field-notes.md").write_text(NOTES + "The electricians work only in the office.\n", encoding="utf-8")
        self.assertEqual(self.run_electric().decisions["F1"].status, "OPEN")


class LocalElectricalAndRegressionTests(unittest.TestCase):
    def sources(self):
        root = Path(os.environ.get("INSURANCE01_TEST_INPUTS", "/home/maxg/insurance01-inputs"))
        interview = COMPONENT.parents[1] / "interviews/ch03-premium-audit-20261105-0222(1).md"
        if not root.is_dir() or not interview.is_file():
            self.skipTest("Local development snapshots are unavailable")
        return root, interview

    def test_actual_patuxent_wages_allowances_open_case_and_application(self):
        root, interview = self.sources()
        folder = root / "employer-files/patuxent-electric"
        result = process_employer(root / "classification-guide.md", folder, interview)
        self.assertEqual(len(result.register), 7)
        self.assertEqual(result.owner_assessment.status, "INCLUDED")
        self.assertEqual(result.decisions["PE-E01"].class_code, "E-510")
        self.assertEqual(result.decisions["PE-E07"].class_code, "C-110")
        self.assertEqual(result.allocation.by_code, {"E-510": Decimal("424024.85"), "C-110": Decimal("43905.60")})
        self.assertEqual(result.by_code, {"E-510": Decimal("426184.85"), "C-110": Decimal("43905.60")})
        self.assertEqual(result.adjustments.reconciliation.basis_total, Decimal("9224.00"))
        self.assertEqual(result.adjustments.reconciliation.payroll_added, Decimal("2160.00"))
        self.assertEqual(result.adjustments.reconciliation.nonpayroll, Decimal("6674.00"))
        self.assertEqual(result.adjustments.reconciliation.unresolved_basis, Decimal("390.00"))
        self.assertEqual(result.travel_reconciliation.known_payroll, Decimal("470090.45"))
        self.assertEqual(result.travel_reconciliation.cash_total, Decimal("477154.45"))
        self.assertTrue(result.travel_reconciliation.reconciled)
        self.assertTrue(result.independent_reconciliation.reconciled)
        kyle = next(line for line in result.adjustments.lines if line.input_record.employee_id == "PE-E06")
        self.assertEqual(kyle.status, "OPEN")
        self.assertEqual(kyle.proposal.payroll_added, Decimal("390.00"))
        self.assertEqual(result.application.verified_differences, {"E-510": Decimal("120160.00"), "C-110": Decimal("-118000.00")})
        with (folder / "payroll-register.csv").open() as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(sum(Decimal(row["wages_paid"]) for row in rows), Decimal("467930.45"))
        self.assertEqual(sum(Decimal(row["travel_allowance_paid"]) for row in rows), Decimal("9224.00"))

    def test_all_five_previous_employer_class_totals_and_reconciliations(self):
        root, interview = self.sources()
        expected = {
            "larkspur-lane-bistro": {"F-710": Decimal("226431.55")},
            "harbor-point-legal": {"C-110": Decimal("360935.68")},
            "bay-crest-exteriors": {"C-110": Decimal("44812.35"), "R-310": Decimal("450480.60"), "R-320": Decimal("46205.10")},
            "severn-homebuilders": {"C-110": Decimal("46118.25"), "H-420": Decimal("369204.39")},
            "annapolis-courier": {"C-110": Decimal("107820.45"), "T-610": Decimal("176694.95")},
        }
        for employer, codes in expected.items():
            with self.subTest(employer=employer):
                result = process_employer(root / "classification-guide.md", root / "employer-files" / employer, interview)
                self.assertEqual(result.by_code, codes)
                self.assertTrue(result.independent_reconciliation.reconciled)


if __name__ == "__main__":
    unittest.main()
