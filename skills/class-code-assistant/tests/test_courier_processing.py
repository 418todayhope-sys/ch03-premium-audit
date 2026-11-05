"""Weekly courier integration with independent small monetary fixtures."""

import csv
from dataclasses import replace
from datetime import date, timedelta
from decimal import Decimal, localcontext
import hashlib
import io
import os
from pathlib import Path
import sys
import tempfile
import unittest

COMPONENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPONENT))
from employer_processing import EmployerFiles, process_employer
from test_legal_office_processing import GUIDE as OFFICE_GUIDE
from test_rule_evaluator import INTERVIEW

GUIDE = OFFICE_GUIDE + """
**CG-31. T-610 Courier and delivery drivers.** Drivers of vans and light trucks delivering parcels and documents,
and helpers who ride on the delivery vehicles.
"""
BUSINESS = """# Independent delivery business
Audit period January 5, 2026 to January 18, 2026.
Independent Delivery runs same-day document and parcel delivery for local businesses, two van routes two days a week.
Four employees, paid weekly.
"""
NOTES = """# Auditor field notes
Dispatch office with two desks and a radio; two vans. The dispatcher, Inside Person, was on the radio.
The route log lists every route day with its driver and anyone riding along. Pay weeks run Monday to Sunday.
"""
REGISTER = """employee_id,name,position,wages_paid
D1,Driver One,Driver,200.02
D2,Driver Two,Driver,180.04
I1,Inside Person,Dispatcher,60.02
B1,Books Person,Bookkeeper,40.10
"""
APPLICATION = """# Application
| Class code (employer's choice) | Employees | Payroll (USD) |
|---|---|---|
| T-610 | 2 | 380.06 |
| C-110 | 2 | 100.12 |
"""
ROUTE_HEADER = "date,route_id,driver_id,ride_along_id,stops\n"
WEEK_HEADER = "week_start,week_end,employee_id,gross_pay\n"


class CourierIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.employer = self.root / "independent-delivery-inputs"
        self.employer.mkdir()
        self.guide = self.root / "guide.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview = self.root / "interview.md"
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        for filename, text in {"business-description.md": BUSINESS, "field-notes.md": NOTES,
            "payroll-register.csv": REGISTER, "application.md": APPLICATION}.items():
            (self.employer / filename).write_text(text, encoding="utf-8")
        rows = []
        for start in (date(2026, 1, 5), date(2026, 1, 12)):
            for employee, pay in (("D1", "100.01"), ("D2", "90.02"), ("I1", "30.01"), ("B1", "20.05")):
                rows.append(f"{start},{start + timedelta(days=6)},{employee},{pay}\n")
        self.weekly = WEEK_HEADER + "".join(rows)
        (self.employer / "weekly-payroll.csv").write_text(self.weekly, encoding="utf-8")
        self.routes()

    def routes(self, counts=(1, 2)):
        rows = []
        for week, start in enumerate((date(2026, 1, 5), date(2026, 1, 12))):
            for index, offset in enumerate((0, 6)):
                for route, driver in (("X", "D1"), ("Y", "D2")):
                    rider = "I1" if route == "X" and index < counts[week] else ""
                    rows.append(f"{start + timedelta(days=offset)},{route},{driver},{rider},10\n")
        (self.employer / "route-log.csv").write_text(ROUTE_HEADER + "".join(rows), encoding="utf-8")

    def run_courier(self, **kwargs):
        return process_employer(self.guide, self.employer, self.interview, **kwargs)

    def week(self, result, employee="I1", start=date(2026, 1, 5)):
        return next(row for row in result.weekly_results if row.employee_id == employee and row.week_start == start)

    def test_whole_week_threshold_and_independent_reconciliation(self):
        result = self.run_courier()
        self.assertEqual(result.by_code, {"T-610": Decimal("410.07"), "C-110": Decimal("70.11")})
        self.assertEqual(result.employee_totals["I1"], {"T-610": Decimal("30.01"), "C-110": Decimal("30.01")})
        self.assertEqual(len(result.weekly_results), 8)
        self.assertTrue(result.weekly_reconciliation.reconciled)
        self.assertEqual(result.weekly_reconciliation.weekly_total, Decimal("480.18"))
        self.assertTrue(result.independent_reconciliation.reconciled)
        self.assertEqual(result.application.verified_differences, {"T-610": Decimal("30.01"), "C-110": Decimal("-30.01")})

    def test_zero_one_two_day_boundaries_and_bookkeeper_rides(self):
        for count, code in ((0, "C-110"), (1, "C-110"), (2, "T-610")):
            with self.subTest(days=count):
                self.routes((count, count))
                self.assertEqual(self.week(self.run_courier()).decision.class_code, code)
        path = self.employer / "route-log.csv"
        path.write_text(path.read_text().replace(",I1,", ",B1,"), encoding="utf-8")
        self.assertEqual(self.week(self.run_courier(), "B1").decision.class_code, "T-610")

    def test_distinct_dates_ignore_two_rides_on_the_same_day(self):
        self.routes((1, 1))
        path = self.employer / "route-log.csv"
        path.write_text(path.read_text().replace("2026-01-05,Y,D2,,", "2026-01-05,Y,D2,I1,"), encoding="utf-8")
        row = self.week(self.run_courier())
        self.assertEqual(row.ride_days, (date(2026, 1, 5),))
        self.assertEqual(row.decision.class_code, "C-110")

    def test_sunday_and_following_monday_belong_to_separate_pay_weeks(self):
        self.routes((0, 1))
        path = self.employer / "route-log.csv"
        path.write_text(path.read_text().replace("2026-01-11,X,D1,,", "2026-01-11,X,D1,I1,"), encoding="utf-8")
        result = self.run_courier()
        self.assertEqual(self.week(result).decision.class_code, "C-110")
        self.assertEqual(self.week(result, start=date(2026, 1, 12)).decision.class_code, "C-110")

    def test_weekly_parts_preserve_dates_ids_raw_money_and_rule_sources(self):
        result = self.run_courier()
        row = self.week(result)
        self.assertEqual(row.week_end, date(2026, 1, 11))
        self.assertEqual(row.wages, Decimal("30.01"))
        self.assertEqual(row.raw_record.values["employee_id"], "I1")
        self.assertEqual(row.decision.scope, "whole_pay_week")
        self.assertTrue(any(ref.locator == "Nadia Brennan · 09:05 PM" for ref in row.decision.rule_sources))
        self.assertTrue(any(ref.locator == "CG-31" for ref in row.decision.rule_sources))
        self.assertTrue(any(ref.source.endswith("route-log.csv") and ref.line_start == 1 for ref in row.decision.evidence_sources))
        self.assertTrue(any(line.part.part_id == row.part_id for line in result.allocation.lines))
        for ref in (*row.decision.rule_sources, *row.decision.evidence_sources):
            self.assertEqual(ref.sha256, hashlib.sha256(Path(ref.source).read_bytes()).hexdigest())

    def test_missing_week_keeps_full_employee_register_wages_open(self):
        path = self.employer / "weekly-payroll.csv"
        path.write_text(self.weekly.replace("2026-01-05,2026-01-11,I1,30.01\n", ""), encoding="utf-8")
        result = self.run_courier()
        self.assertFalse(result.weekly_reconciliation.reconciled)
        self.assertEqual(result.weekly_reconciliation.missing_weeks["I1"], (date(2026, 1, 5),))
        self.assertEqual(result.employee_totals["I1"], {"OPEN": Decimal("60.02")})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("60.02"))

    def test_offsetting_employee_wage_errors_do_not_pass_annual_controls(self):
        path = self.employer / "weekly-payroll.csv"
        path.write_text(self.weekly.replace("D1,100.01", "D1,100.02", 1).replace("I1,30.01", "I1,30.00", 1), encoding="utf-8")
        result = self.run_courier()
        control = result.weekly_reconciliation
        self.assertEqual(control.weekly_total, Decimal("480.18"))
        self.assertEqual(control.employee_differences["D1"], Decimal("-0.01"))
        self.assertEqual(control.employee_differences["I1"], Decimal("0.01"))
        self.assertFalse(control.reconciled)
        self.assertEqual(result.employee_totals["D1"], {"OPEN": Decimal("200.02")})

    def test_duplicate_zero_pay_week_is_detected_even_when_money_still_balances(self):
        path = self.employer / "weekly-payroll.csv"
        path.write_text(self.weekly + "2026-01-05,2026-01-11,I1,0.00\n", encoding="utf-8")
        result = self.run_courier()
        self.assertFalse(result.weekly_reconciliation.reconciled)
        self.assertEqual(result.weekly_reconciliation.duplicate_weeks["I1"], (date(2026, 1, 5),))
        self.assertEqual(result.employee_totals["I1"], {"OPEN": Decimal("60.02")})

    def test_unknown_weekly_employee_money_is_preserved_as_orphan_basis(self):
        (self.employer / "weekly-payroll.csv").write_text(self.weekly + "2026-01-05,2026-01-11,UNKNOWN,5.00\n", encoding="utf-8")
        result = self.run_courier()
        self.assertEqual(result.weekly_reconciliation.orphan_total, Decimal("5.00"))
        self.assertFalse(result.weekly_reconciliation.reconciled)
        self.assertNotIn("UNKNOWN", result.employee_totals)
        self.assertFalse(result.application.definitive)

    def test_duplicate_or_conflicting_route_rows_stay_open_with_proposals(self):
        path = self.employer / "route-log.csv"
        original = path.read_text()
        for row in ("2026-01-05,X,D1,I1,10\n", "2026-01-05,X,D1,B1,10\n"):
            with self.subTest(row=row):
                path.write_text(original + row, encoding="utf-8")
                result = self.run_courier()
                weekly = self.week(result)
                self.assertEqual(weekly.decision.status, "OPEN")
                self.assertIsNotNone(weekly.proposal)
                self.assertTrue(any("duplicate" in item.reason.lower() or "conflict" in item.reason.lower() for item in result.open_items))

    def test_unattributed_rider_is_bounded_without_assigning_an_identity(self):
        path = self.employer / "route-log.csv"
        path.write_text(path.read_text().replace("2026-01-11,Y,D2,,", "2026-01-11,Y,D2,UNKNOWN,"), encoding="utf-8")
        result = self.run_courier()
        weekly = self.week(result)
        self.assertEqual(weekly.decision.status, "OPEN")
        self.assertEqual(weekly.ride_days, (date(2026, 1, 5),))
        self.assertEqual(weekly.proposal.class_code, "C-110")
        self.assertEqual(self.week(result, "B1").decision.class_code, "C-110")
        self.assertNotIn("UNKNOWN", result.employee_totals)

    def test_missing_route_rows_and_unknown_drivers_cannot_verify_zero_rides(self):
        path = self.employer / "route-log.csv"
        original = path.read_text()
        for changed in (original.replace("2026-01-11,Y,D2,,10\n", ""), original.replace("2026-01-11,Y,D2,,", "2026-01-11,Y,UNKNOWN,,")):
            with self.subTest(changed=changed):
                path.write_text(changed, encoding="utf-8")
                self.assertEqual(self.week(self.run_courier()).decision.status, "OPEN")

    def test_invalid_pay_week_boundaries_and_zero_pay_missing_weeks_require_review(self):
        path = self.employer / "weekly-payroll.csv"
        path.write_text(self.weekly.replace("2026-01-05,2026-01-11,I1", "2026-01-06,2026-01-12,I1"), encoding="utf-8")
        result = self.run_courier()
        self.assertFalse(result.weekly_reconciliation.reconciled)
        self.assertEqual(result.employee_totals["I1"], {"OPEN": Decimal("60.02")})
        path.write_text(self.weekly.replace("2026-01-05,2026-01-11,I1,30.01\n", ""), encoding="utf-8")
        (self.employer / "payroll-register.csv").write_text(REGISTER.replace("I1,Inside Person,Dispatcher,60.02", "I1,Inside Person,Dispatcher,30.01"), encoding="utf-8")
        self.assertFalse(self.run_courier().weekly_reconciliation.reconciled)

    def test_missing_files_and_empty_sources_do_not_become_complete_zero_evidence(self):
        for filename in ("route-log.csv", "weekly-payroll.csv"):
            path = self.employer / filename
            original = path.read_text()
            for contents in (None, original.splitlines()[0] + "\n"):
                with self.subTest(filename=filename, contents=contents):
                    if contents is None:
                        path.unlink()
                    else:
                        path.write_text(contents, encoding="utf-8")
                    result = self.run_courier()
                    self.assertTrue(result.open_items)
                    self.assertGreater(result.independent_reconciliation.unresolved_total, 0)
                    self.assertFalse(result.application.definitive)
                    path.write_text(original, encoding="utf-8")

    def test_negated_completeness_duty_exceptions_and_changed_rule_sources_are_open(self):
        path = self.employer / "field-notes.md"
        for text in (NOTES.replace("lists every route day", "does not list every route day"), NOTES + "Inside Person performs physical roof installation.\n", NOTES + "Some route pages are missing.\n"):
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                self.assertEqual(self.week(self.run_courier()).decision.status, "OPEN")
        path.write_text(NOTES, encoding="utf-8")
        self.interview.write_text(INTERVIEW.replace("two or more days", "three or more days"), encoding="utf-8")
        self.assertEqual(self.week(self.run_courier()).decision.status, "OPEN")
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        self.guide.write_text(GUIDE.replace("Drivers of vans", "Operators of vans"), encoding="utf-8")
        self.assertEqual(self.week(self.run_courier()).decision.status, "OPEN")

    def test_configurable_sources_reread_exact_cents_under_low_precision(self):
        (self.employer / "route-log.csv").rename(self.employer / "journeys.csv")
        (self.employer / "weekly-payroll.csv").rename(self.employer / "weeks.csv")
        files = replace(EmployerFiles(), routes="journeys.csv", weekly_payroll="weeks.csv")
        with localcontext() as context:
            context.prec = 3
            result = self.run_courier(files=files)
        self.assertEqual(result.by_code, {"T-610": Decimal("410.07"), "C-110": Decimal("70.11")})
        path = self.employer / "journeys.csv"
        path.write_text(path.read_text().replace(",I1,", ",,"), encoding="utf-8")
        self.assertEqual(self.run_courier(files=files).by_code, {"T-610": Decimal("380.06"), "C-110": Decimal("100.12")})

    def test_individual_duty_conflicts_and_negated_office_observations_require_review(self):
        path = self.employer / "field-notes.md"
        cases = (
            (NOTES + "Inside Person does not perform dispatch or bookkeeping work.\n", "I1"),
            (NOTES + "Driver One never drives a van; the Driver title is retained for payroll.\n", "D1"),
            (NOTES + "Books Person works in the warehouse, unloading parcels all week.\n", "B1"),
            (NOTES.replace("Dispatch office with", "There is no dispatch office. There are"), "I1"),
        )
        for text, employee in cases:
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                result = self.run_courier()
                self.assertEqual(self.week(result, employee).decision.status, "OPEN")
                self.assertIsNotNone(self.week(result, employee).proposal)
                self.assertGreater(result.independent_reconciliation.unresolved_total, 0)

    def test_empty_annual_register_does_not_fabricate_a_reconciled_zero_basis(self):
        (self.employer / "payroll-register.csv").write_text(REGISTER.splitlines()[0] + "\n", encoding="utf-8")
        result = self.run_courier()
        self.assertIsNone(result.allocation)
        self.assertIsNone(result.independent_reconciliation)
        self.assertTrue(result.open_items)


class LocalCourierIntegrationTest(unittest.TestCase):
    def test_actual_weekly_split_all_rows_and_annual_reconciliation(self):
        root = Path(os.environ.get("INSURANCE01_TEST_INPUTS", "/home/maxg/insurance01-inputs"))
        interview = COMPONENT.parents[1] / "interviews/ch03-premium-audit-20261105-0222(1).md"
        if not root.is_dir() or not interview.is_file():
            self.skipTest("Local development snapshots are unavailable")
        employer = root / "employer-files/annapolis-courier"
        result = process_employer(root / "classification-guide.md", employer, interview)
        self.assertEqual(result.by_code, {"T-610": Decimal("176694.95"), "C-110": Decimal("107820.45")})
        self.assertEqual(len(result.weekly_results), 312)
        self.assertTrue(result.weekly_reconciliation.reconciled)
        self.assertTrue(result.independent_reconciliation.reconciled)
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("284515.40"))
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
        self.assertEqual(result.employee_totals["AC-E04"], {"T-610": Decimal("22808.75"), "C-110": Decimal("24633.45")})
        self.assertEqual(result.employee_totals["AC-E05"], {"C-110": Decimal("46675.20")})
        self.assertEqual(sum(row.employee_id == "AC-E04" and row.decision.class_code == "T-610" for row in result.weekly_results), 25)
        self.assertEqual(result.application.verified_differences, {"T-610": Decimal("22808.75"), "C-110": Decimal("-22808.75")})
        with (employer / "weekly-payroll.csv").open() as stream:
            raw = list(csv.DictReader(stream))
        self.assertEqual(sum(Decimal(row["gross_pay"]) for row in raw), Decimal("284515.40"))


if __name__ == "__main__":
    unittest.main()
