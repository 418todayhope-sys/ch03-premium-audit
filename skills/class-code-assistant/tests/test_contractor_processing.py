"""Real-component contractor integration; evidence drives both rule stages."""

from dataclasses import replace
from datetime import date, timedelta
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
from test_legal_office_processing import GUIDE as OFFICE_GUIDE, INTERVIEW as OFFICE_INTERVIEW

GUIDE = OFFICE_GUIDE + """
**CG-11. R-310 Roofing.** Installation, repair and removal of roofs and roof coverings on any building, including
work on scaffolds and ladders at the roof line.

**CG-12. R-320 Siding and gutters.** Installation and repair of exterior siding, gutters, downspouts and exterior trim
below the roof line. Roofing work is described by CG-11.
"""
INTERVIEW = OFFICE_INTERVIEW + """
**Nadia Brennan** · Voice · 09:04 PM

Contractors doing both roofing and siding classify field workers with 15 or more days on a roof entirely under R-310, and those with fewer days entirely under R-320.

**Nadia Brennan** · Voice · 09:16 PM

The 15-day roofing rule applies specifically to contractors who perform both roofing and siding work within the audit period.
"""
BUSINESS = """# Independent Exteriors: business description
Audit period January 1, 2025 to December 31, 2025.
Independent Exteriors replaces roofs and installs siding and gutters. The company does its own installation.
"""
NOTES = """# Auditor field notes
Two field workers were out on jobs, one roof and one siding job, and the estimator
was measuring a house for a quote. The bookkeeper works in the office.
Crew time is recorded on the crew timesheets by job and type of work. Office staff
sign the site sign-in sheet when they visit a job.
"""
PAYROLL = """employee_id,name,position,wages_paid
F1,Example First,Coordinator,100.01
F2,Example Second,Siding Installer,50.02
E1,Example Estimator,Estimator,30.03
B1,Example Books,Bookkeeper,20.04
"""
APPLICATION = """# Employer application
| Class code (employer's choice) | Employees | Payroll (USD) |
|---|---|---|
| R-310 | 1 | 100.01 |
| C-110 | 3 | 100.09 |
"""
TIME_HEADER = "date,employee_id,name,job_id,work_type,hours\n"
SITE_HEADER = "date,employee_id,name,site,signed_in_at\n"


class ContractorIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.employer = self.root / "another-input-location"
        self.employer.mkdir()
        self.guide = self.root / "guide.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview = self.root / "interview.md"
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        for filename, text in {"business-description.md": BUSINESS, "field-notes.md": NOTES,
                               "payroll-register.csv": PAYROLL, "application.md": APPLICATION}.items():
            (self.employer / filename).write_text(text, encoding="utf-8")
        self.set_times()
        self.set_visits()

    def set_times(self, first=15, second=14):
        rows = []
        for employee, name, count in [("F1", "Example First", first), ("F2", "Example Second", second)]:
            for offset in range(count):
                rows.append(f"{date(2025,1,1)+timedelta(days=offset)},{employee},{name},JOB-1,roofing,8.0\n")
            rows.append(f"2025-02-01,{employee},{name},JOB-2,siding,8.0\n")
        (self.employer / "crew-timesheets.csv").write_text(TIME_HEADER + "".join(rows), encoding="utf-8")

    def set_visits(self, estimator=5, bookkeeper=0, unassigned=0):
        rows = []
        for employee, name, count in [("E1", "Example Estimator", estimator), ("B1", "Example Books", bookkeeper)]:
            for offset in range(count):
                rows.append(f"{date(2025,3,1)+timedelta(days=offset)},{employee},{name},Site A,09:00\n")
        for offset in range(unassigned):
            rows.append(f"{date(2025,4,1)+timedelta(days=offset)},,Unattributed Visitor,Site A,10:00\n")
        (self.employer / "site-signin-log.csv").write_text(SITE_HEADER + "".join(rows), encoding="utf-8")

    def run_contractor(self, **kwargs):
        return process_employer(self.guide, self.employer, self.interview, **kwargs)

    def test_two_stage_rules_and_unique_inferred_employee_changes(self):
        result = self.run_contractor()
        self.assertEqual(result.by_code, {"C-110": Decimal("20.04"), "R-310": Decimal("130.04"), "R-320": Decimal("50.02")})
        self.assertEqual(len(result.roofing_days["F1"]), 15)
        self.assertEqual(len(result.roofing_days["F2"]), 14)
        self.assertEqual(result.governing_field.class_code, "R-310")
        self.assertEqual(result.governing_field.by_code, {"R-310": Decimal("100.01"), "R-320": Decimal("50.02")})
        self.assertEqual(result.decisions["E1"].class_code, "R-310")
        self.assertEqual(result.employee_comparisons["F2"].reported_code, "C-110")
        self.assertEqual(result.employee_comparisons["F2"].calculated_code, "R-320")
        self.assertEqual(result.employee_comparisons["F2"].status, "CHANGE")
        self.assertTrue(result.employee_comparisons["F2"].reported_inferred)
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("200.10"))
        self.assertTrue(result.independent_reconciliation.reconciled)
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))

    def test_same_day_multiple_jobs_do_not_cross_fifteen_day_threshold(self):
        path = self.employer / "crew-timesheets.csv"
        path.write_text(path.read_text() + "2025-01-01,F2,Example Second,JOB-3,roofing,2.0\n", encoding="utf-8")
        result = self.run_contractor()
        self.assertEqual(len(result.roofing_days["F2"]), 14)
        self.assertEqual(result.decisions["F2"].class_code, "R-320")
        self.assertEqual(len([r for r in result.decisions["F2"].evidence_sources if r.source.endswith("crew-timesheets.csv")]), 16)

    def test_zero_roofing_days_with_documented_siding_is_not_a_missing_timesheet(self):
        self.set_times(second=0)
        result = self.run_contractor()
        self.assertEqual(result.roofing_days["F2"], ())
        self.assertEqual(result.decisions["F2"].class_code, "R-320")

    def test_governing_code_changes_with_field_payroll_and_not_job_titles(self):
        (self.employer / "payroll-register.csv").write_text(PAYROLL.replace("50.02", "150.02"), encoding="utf-8")
        result = self.run_contractor()
        self.assertEqual(result.governing_field.class_code, "R-320")
        self.assertEqual(result.decisions["E1"].class_code, "R-320")
        self.assertEqual(result.decisions["F1"].class_code, "R-310")

    def test_governing_code_tie_keeps_high_visit_office_worker_open(self):
        (self.employer / "payroll-register.csv").write_text(PAYROLL.replace("50.02", "100.01"), encoding="utf-8")
        result = self.run_contractor()
        self.assertIsNone(result.governing_field.class_code)
        self.assertEqual(result.decisions["E1"].status, "OPEN")
        self.assertEqual(result.decisions["B1"].class_code, "C-110")
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("30.03"))

    def test_four_and_five_office_days_and_bookkeeper_evidence(self):
        self.set_visits(estimator=4, bookkeeper=5)
        result = self.run_contractor()
        self.assertEqual(result.decisions["E1"].class_code, "C-110")
        self.assertEqual(result.decisions["B1"].class_code, "R-310")

    def test_unassigned_visit_is_preserved_without_inventing_an_employee(self):
        self.set_visits(unassigned=1)
        result = self.run_contractor()
        self.assertEqual(result.decisions["E1"].class_code, "R-310")
        self.assertEqual(result.decisions["B1"].class_code, "C-110")
        self.assertEqual(len(result.site_visits["B1"]), 0)
        self.assertEqual(len(result.unassigned_site_records), 1)
        self.assertTrue(any("unattributed" in item.subject.lower() for item in result.open_items))
        self.set_visits(estimator=4, unassigned=1)
        self.assertEqual(self.run_contractor().decisions["E1"].status, "OPEN")

    def test_missing_timesheets_do_not_establish_zero_roofing_or_a_governing_code(self):
        (self.employer / "crew-timesheets.csv").unlink()
        result = self.run_contractor()
        self.assertNotIn("F1", result.roofing_days)
        self.assertIsNone(result.governing_field.class_code)
        self.assertEqual(result.decisions["F1"].status, "OPEN")
        self.assertEqual(result.decisions["E1"].status, "OPEN")
        self.assertEqual(result.decisions["B1"].class_code, "C-110")

    def test_missing_one_field_workers_rows_cannot_make_them_siding_by_default(self):
        path = self.employer / "crew-timesheets.csv"
        path.write_text("\n".join(line for line in path.read_text().splitlines() if ",F2," not in line) + "\n", encoding="utf-8")
        result = self.run_contractor()
        self.assertEqual(result.decisions["F2"].status, "OPEN")
        self.assertIsNone(result.governing_field.class_code)
        self.assertEqual(result.decisions["E1"].status, "OPEN")

    def test_unknown_work_bad_hours_and_outside_period_dates_are_open(self):
        path = self.employer / "crew-timesheets.csv"
        original = path.read_text()
        for text in [original.replace(",roofing,8.0", ",electrical,8.0", 1), original.replace(",roofing,8.0", ",roofing,NaN", 1), original.replace("2025-01-01", "2026-01-01", 1)]:
            with self.subTest(text=text[:100]):
                path.write_text(text, encoding="utf-8")
                result = self.run_contractor()
                self.assertEqual(result.decisions["F1"].status, "OPEN")
                self.assertIsNone(result.governing_field.class_code)

    def test_conflicting_employee_identity_is_not_resolved_by_guessing_a_name(self):
        path = self.employer / "crew-timesheets.csv"
        path.write_text(path.read_text().replace("F1,Example First", "F1,Example Second", 1), encoding="utf-8")
        result = self.run_contractor()
        self.assertEqual(result.decisions["F1"].status, "OPEN")
        self.assertEqual(result.decisions["F2"].status, "OPEN")
        self.assertIsNone(result.governing_field.class_code)

    def test_rule_scope_and_changed_source_wording_prevent_classification(self):
        (self.employer / "business-description.md").write_text(BUSINESS.replace("and installs siding and gutters", "and does not install siding"), encoding="utf-8")
        self.assertEqual(self.run_contractor().decisions["F1"].status, "OPEN")
        (self.employer / "business-description.md").write_text(BUSINESS, encoding="utf-8")
        self.guide.write_text(GUIDE.replace("work on scaffolds and ladders at the roof line.", "### Restriction\nThis code excludes roofing."), encoding="utf-8")
        self.assertEqual(self.run_contractor().decisions["F1"].status, "OPEN")

    def test_unmapped_duties_and_unsupported_bookkeeper_observations_are_open(self):
        (self.employer / "individual-duties.md").write_text("Unmapped duty evidence.", encoding="utf-8")
        self.assertEqual(self.run_contractor().by_code, {})
        (self.employer / "individual-duties.md").unlink()
        (self.employer / "field-notes.md").write_text(NOTES.replace("The bookkeeper works in the office.", "The bookkeeper's work location is unconfirmed."), encoding="utf-8")
        self.assertEqual(self.run_contractor().decisions["B1"].status, "OPEN")

    def test_qualified_or_conflicting_office_observations_do_not_establish_office_roles(self):
        path = self.employer / "field-notes.md"
        for text, employee in [(NOTES.replace("The bookkeeper works in the office.", "It is not confirmed that the bookkeeper works in the office."), "B1"),
                               (NOTES.replace("was measuring a house for a quote", "was not measuring a house for a quote"), "E1")]:
            with self.subTest(employee=employee):
                path.write_text(text, encoding="utf-8")
                self.assertEqual(self.run_contractor().decisions[employee].status, "OPEN")

    def test_conflicting_timesheet_row_is_cited_in_open_decisions(self):
        path = self.employer / "crew-timesheets.csv"
        path.write_text(path.read_text().replace("F1,Example First", "F1,Example Second", 1), encoding="utf-8")
        result = self.run_contractor()
        self.assertTrue(any(ref.line_start == 2 and "F1,Example Second" in ref.excerpt for ref in result.decisions["F1"].evidence_sources))

    def test_time_records_conflicting_with_an_observed_office_role_need_scope_review(self):
        path = self.employer / "crew-timesheets.csv"
        path.write_text(path.read_text() + "2025-02-01,B1,Example Books,JOB-4,roofing,8.0\n", encoding="utf-8")
        self.assertEqual(self.run_contractor().decisions["B1"].status, "OPEN")

    def test_explicit_missing_records_prevent_complete_evidence_assertion(self):
        (self.employer / "field-notes.md").write_text(NOTES + "Some crew timesheets and office sign-in pages for this period are missing.\n", encoding="utf-8")
        result = self.run_contractor()
        self.assertEqual(result.by_code, {})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("200.10"))

    def test_additional_bookkeeper_installation_duties_require_review(self):
        (self.employer / "field-notes.md").write_text(NOTES + "The bookkeeper also installs roofs on jobs every week.\n", encoding="utf-8")
        self.assertEqual(self.run_contractor().decisions["B1"].status, "OPEN")

    def test_singular_role_observation_cannot_be_reused_for_two_employees(self):
        (self.employer / "payroll-register.csv").write_text(PAYROLL + "B2,Unobserved Employee,Bookkeeper,40.05\n", encoding="utf-8")
        result = self.run_contractor()
        self.assertEqual(result.decisions["B2"].status, "OPEN")
        self.assertEqual(result.decisions["B1"].status, "OPEN")
        self.assertIsNone(result.governing_field.class_code)

    def test_impossible_application_headcount_is_open_instead_of_overflowing(self):
        (self.employer / "application.md").write_text(APPLICATION.replace("| R-310 | 1 |", "| R-310 | 99999999999999999999999999999 |"), encoding="utf-8")
        result = self.run_contractor()
        self.assertEqual(result.by_code["R-310"], Decimal("130.04"))
        self.assertIsNone(result.employee_comparisons["F1"].reported_code)
        self.assertEqual(result.employee_comparisons["F1"].status, "OPEN")

    def test_governing_and_dependent_office_decision_retain_crew_dependencies(self):
        result = self.run_contractor()
        for references in (result.governing_field.evidence_sources, result.decisions["E1"].evidence_sources):
            self.assertTrue(any(ref.source.endswith("crew-timesheets.csv") and ref.line_start == 2 for ref in references))

    def test_ambiguous_application_mapping_is_never_filled_from_titles(self):
        (self.employer / "payroll-register.csv").write_text(PAYROLL.replace("50.02", "100.01"), encoding="utf-8")
        (self.employer / "application.md").write_text(APPLICATION.replace("100.09", "150.08"), encoding="utf-8")
        result = self.run_contractor()
        self.assertIsNone(result.employee_comparisons["F1"].reported_code)
        self.assertEqual(result.employee_comparisons["F1"].status, "OPEN")

    def test_configurable_paths_and_low_decimal_precision_keep_exact_cents(self):
        (self.employer / "crew-timesheets.csv").rename(self.employer / "activity.csv")
        files = replace(EmployerFiles(), crew_timesheets="activity.csv")
        with localcontext() as context:
            context.prec = 3
            result = self.run_contractor(files=files)
        self.assertEqual(result.by_code["R-310"], Decimal("130.04"))
        self.assertEqual(result.independent_reconciliation.difference, Decimal("0.00"))
        self.assertTrue(any(ref.source.endswith("activity.csv") for ref in result.decisions["F1"].evidence_sources))


class LocalBayCrestIntegrationTest(unittest.TestCase):
    def test_actual_ten_employees_and_independent_raw_csv_reconciliation(self):
        root = Path(os.environ.get("INSURANCE01_TEST_INPUTS", "/home/maxg/insurance01-inputs"))
        interview = COMPONENT.parents[1] / "interviews" / "ch03-premium-audit-20261105-0222(1).md"
        if not root.is_dir() or not interview.is_file():
            self.skipTest("Authoritative local development snapshots are unavailable")
        employer = root / "employer-files" / "bay-crest-exteriors"
        result = process_employer(root / "classification-guide.md", employer, interview)
        self.assertEqual(result.by_code, {"C-110": Decimal("44812.35"), "R-310": Decimal("450480.60"), "R-320": Decimal("46205.10")})
        self.assertEqual([len(result.roofing_days[f"BC-E0{i}"]) for i in range(1,9)], [188,176,201,164,152,97,15,9])
        self.assertEqual(result.governing_field.by_code, {"R-310": Decimal("382049.70"), "R-320": Decimal("46205.10")})
        self.assertEqual(result.decisions["BC-E09"].class_code, "R-310")
        self.assertEqual(len(result.site_visits["BC-E09"]), 9)
        self.assertEqual(result.decisions["BC-E10"].class_code, "C-110")
        self.assertEqual(len(result.unassigned_site_records), 1)
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
        self.assertEqual(result.independent_reconciliation.difference, Decimal("0.00"))
        raw = list(csv.DictReader(io.StringIO((employer / "payroll-register.csv").read_text())))
        self.assertEqual(sum(Decimal(row["wages_paid"]) for row in raw), Decimal("541498.05"))
        self.assertEqual(sum(line.wages for line in result.allocation.lines), Decimal("541498.05"))
        self.assertEqual(result.application.verified_differences, {"C-110": Decimal("-319158.10"), "R-310": Decimal("272953.00"), "R-320": Decimal("46205.10")})
        changed = {key for key, item in result.employee_comparisons.items() if item.status == "CHANGE"}
        self.assertEqual(changed, {"BC-E04", "BC-E05", "BC-E06", "BC-E07", "BC-E08", "BC-E09"})


if __name__ == "__main__":
    unittest.main()
