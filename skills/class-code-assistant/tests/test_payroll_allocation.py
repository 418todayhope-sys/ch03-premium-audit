"""Synthetic base wages only: exact accounting, provenance and unresolved decisions."""

from dataclasses import replace
from decimal import Decimal, localcontext
import importlib
from pathlib import Path
import sys
import tempfile
import unittest


COMPONENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPONENT))
from input_reader import read_csv
from rule_evaluator import Decision, SourceReference


class PayrollAllocationTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue((COMPONENT / "payroll_allocation.py").is_file(), "Base payroll allocator is not implemented")
        self.payroll = importlib.import_module("payroll_allocation")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def record(self, employee, wages, line=2):
        source = SourceReference("synthetic/register.csv", f"line {line}", line, line, f"{employee},{wages}")
        return self.payroll.PayrollRecord(employee, f"Worker {employee}", Decimal(wages), source)

    def classified(self, code="C-110", paragraph="CG-04", scope="whole_audit_period"):
        guide = SourceReference("synthetic/guide.md", paragraph, 1, 1, f"**{paragraph}. {code} Synthetic definition.**")
        rule = SourceReference("synthetic/interview.md", "verified auditor statement", 2, 2, "Synthetic verified statement.")
        evidence = SourceReference("synthetic/activities.csv", "rows 2-4")
        return Decision("verified_synthetic_rule", "CLASSIFIED", code, paragraph, "Verified synthetic duties.", (), (guide, rule), (evidence,), ("verified synthetic applicability",), scope)

    def open_decision(self):
        return Decision("uncovered_case", "OPEN", None, None, "Conflicting duty evidence.", ("Auditor must confirm Worker E2's duties.",), (SourceReference("synthetic/interview.md", "open-item practice"),), (SourceReference("synthetic/notes.md", "paragraph 2"),), ("case requires review",), "whole_audit_period")

    def part(self, part_id, employee, wages, line, scope="whole_pay_week"):
        return self.payroll.PayrollPart(part_id, employee, Decimal(wages), SourceReference("synthetic/weekly.csv", f"line {line}", line, line, f"{employee},{wages}"), scope)

    def test_aggregate_multiple_codes_and_reconcile_exact_cents(self):
        records = [self.record("E1", "0.10"), self.record("E2", "0.20", 3), self.record("E3", "10.05", 4)]
        result = self.payroll.allocate_payroll(records, {"E1": self.classified(), "E2": self.classified(), "E3": self.classified("R-310", "CG-11")})
        self.assertEqual(result.by_code, {"C-110": Decimal("0.30"), "R-310": Decimal("10.05")})
        self.assertEqual(result.reconciliation.register_total, Decimal("10.35"))
        self.assertEqual(result.reconciliation.allocated_total, Decimal("10.35"))
        self.assertEqual(result.reconciliation.unresolved_total, Decimal("0.00"))
        self.assertEqual(result.reconciliation.difference, Decimal("0.00"))
        self.assertTrue(result.reconciliation.reconciled)

    def test_missing_and_open_decisions_keep_wages_unassigned(self):
        records = [self.record("E1", "100.00"), self.record("E2", "20.01", 3), self.record("E3", "30.02", 4)]
        open_case = self.open_decision()
        result = self.payroll.allocate_payroll(records, {"E1": self.classified(), "E2": open_case})
        self.assertEqual(result.by_code, {"C-110": Decimal("100.00")})
        self.assertEqual(result.reconciliation.unresolved_total, Decimal("50.03"))
        self.assertTrue(result.reconciliation.reconciled)
        pending = {line.employee.employee_id: line for line in result.lines if line.status == "OPEN"}
        self.assertEqual(set(pending), {"E2", "E3"})
        self.assertIs(pending["E2"].decision, open_case)
        self.assertEqual(pending["E2"].required_confirmation, open_case.required_confirmation)
        for line in pending.values():
            self.assertIsNone(line.class_code)
            self.assertIsNone(line.rationale_ref)
            self.assertTrue(line.reason)
            self.assertTrue(line.required_confirmation)

    def test_employee_row_and_full_rule_provenance_are_retained(self):
        record = self.record("E1", "12.30")
        decision = self.classified()
        result = self.payroll.allocate_payroll([record], {"E1": decision})
        line = result.lines[0]
        self.assertIs(line.employee, record)
        self.assertEqual(line.part.source, record.source)
        self.assertIs(line.decision, decision)
        self.assertEqual(line.rationale_ref, "CG-04")
        self.assertEqual(line.decision.rule_sources, decision.rule_sources)
        self.assertEqual(line.wages, Decimal("12.30"))

    def test_reader_adapter_preserves_raw_row_and_excludes_travel_columns(self):
        path = self.root / "payroll.csv"
        path.write_bytes(b'employee_id,name,wages_paid,travel_allowance_paid\r\nE1,"Ada, A",100.25,999.00\r\n')
        table = read_csv(path)
        records = self.payroll.records_from_csv(table)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].wages, Decimal("100.25"))
        self.assertEqual(records[0].name, "Ada, A")
        self.assertIs(records[0].raw_record, table.rows[0])
        self.assertEqual(records[0].source.source, str(path))
        self.assertEqual(records[0].source.line_start, 2)
        self.assertIn('E1,"Ada, A",100.25,999.00', records[0].source.excerpt)
        self.assertEqual(len(records[0].source.sha256), 64)
        result = self.payroll.allocate_payroll(records, {"E1": self.classified()})
        self.assertEqual(result.reconciliation.allocated_total, Decimal("100.25"))

    def test_reader_adapter_supports_configurable_wage_and_employee_columns(self):
        path = self.root / "custom.csv"
        path.write_text("worker,label,base_pay\n007,Ada,12.34\n", encoding="utf-8")
        table = read_csv(path, money_columns={"base_pay"})
        records = self.payroll.records_from_csv(table, employee_column="worker", wages_column="base_pay", name_column="label")
        self.assertEqual((records[0].employee_id, records[0].name, records[0].wages), ("007", "Ada", Decimal("12.34")))

    def test_adapter_line_provenance_treats_unicode_separators_as_field_content(self):
        path = self.root / "unicode.csv"
        path.write_text("employee_id,name,wages_paid\nE1,Ada\u2028Analyst,10.00\nE2,Bob,20.00\n", encoding="utf-8")
        records = self.payroll.records_from_csv(read_csv(path))
        self.assertEqual(records[0].source.excerpt, "E1,Ada\u2028Analyst,10.00")
        self.assertEqual((records[0].source.line_start, records[0].source.line_end), (2, 2))
        self.assertEqual(records[1].source.excerpt, "E2,Bob,20.00")
        self.assertEqual((records[1].source.line_start, records[1].source.line_end), (3, 3))

    def test_adapter_rejects_missing_employee_or_wage_columns(self):
        for text in ["name,wages_paid\nAda,1.00\n", "employee_id,name\nE1,Ada\n", "date,subcontractor,amount_paid\n2025-01-01,Firm,100.00\n"]:
            with self.subTest(text=text):
                path = self.root / "invalid.csv"
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(self.payroll.AllocationError):
                    self.payroll.records_from_csv(read_csv(path))

    def test_duplicate_register_employee_or_source_rows_are_rejected(self):
        one = self.record("E1", "10.00")
        for records in [[one, one], [one, self.record("E1", "5.00", 3)], [one, replace(one, employee_id="E2")]]:
            with self.subTest(records=records):
                with self.assertRaisesRegex(self.payroll.AllocationError, "duplicate"):
                    self.payroll.allocate_payroll(records, {})

    def test_one_employee_can_have_multiple_verified_weekly_classifications(self):
        register = [self.record("E1", "100.00")]
        parts = [self.part("week-a", "E1", "40.00", 2), self.part("week-b", "E1", "60.00", 3)]
        result = self.payroll.allocate_parts(register, parts, {"week-a": self.classified(scope="whole_pay_week"), "week-b": self.classified("T-610", "CG-31", "whole_pay_week")})
        self.assertEqual(result.by_code, {"C-110": Decimal("40.00"), "T-610": Decimal("60.00")})
        self.assertTrue(result.reconciliation.reconciled)
        self.assertEqual(result.reconciliation.employee_differences, {"E1": Decimal("0.00")})

    def test_open_week_and_missing_employee_parts_remain_separate(self):
        register = [self.record("E1", "100.00"), self.record("E2", "25.00", 3)]
        parts = [self.part("week-a", "E1", "40.00", 2), self.part("week-b", "E1", "60.00", 3)]
        result = self.payroll.allocate_parts(register, parts, {"week-a": self.classified(scope="whole_pay_week")})
        self.assertEqual(result.by_code, {"C-110": Decimal("40.00")})
        self.assertEqual(result.reconciliation.unresolved_total, Decimal("85.00"))
        self.assertTrue(result.reconciliation.reconciled)
        self.assertEqual(len([line for line in result.lines if line.status == "OPEN"]), 2)

    def test_weekly_decision_cannot_allocate_entire_annual_register_wages(self):
        result = self.payroll.allocate_payroll([self.record("E1", "100.00")], {"E1": self.classified("T-610", "CG-31", "whole_pay_week")})
        self.assertEqual(result.by_code, {})
        self.assertEqual(result.reconciliation.unresolved_total, Decimal("100.00"))
        self.assertIn("scope", result.lines[0].reason.lower())

    def test_duplicate_part_ids_and_relabelled_duplicate_source_rows_are_rejected(self):
        register = [self.record("E1", "100.00")]
        part = self.part("week-a", "E1", "50.00", 2)
        for parts in [[part, part], [part, replace(part, part_id="relabelled")]]:
            with self.subTest(parts=parts):
                with self.assertRaisesRegex(self.payroll.AllocationError, "duplicate"):
                    self.payroll.allocate_parts(register, parts, {})

    def test_under_over_and_offsetting_employee_part_totals_are_rejected(self):
        for amount in ["99.99", "100.01"]:
            with self.subTest(amount=amount):
                with self.assertRaisesRegex(self.payroll.AllocationError, "reconcile"):
                    self.payroll.allocate_parts([self.record("E1", "100.00")], [self.part("p", "E1", amount, 2)], {})
        with self.assertRaisesRegex(self.payroll.AllocationError, "reconcile"):
            self.payroll.allocate_parts([self.record("E1", "100.00"), self.record("E2", "50.00", 3)], [self.part("p1", "E1", "90.00", 2), self.part("p2", "E2", "60.00", 3)], {})

    def test_unknown_employee_and_orphan_decision_keys_are_rejected(self):
        register = [self.record("E1", "100.00")]
        with self.assertRaises(self.payroll.AllocationError):
            self.payroll.allocate_parts(register, [self.part("p", "UNKNOWN", "100.00", 2)], {})
        with self.assertRaises(self.payroll.AllocationError):
            self.payroll.allocate_payroll(register, {"UNKNOWN": self.classified()})

    def test_incomplete_or_pending_classified_decisions_stay_open(self):
        good = self.classified()
        for bad in [replace(good, class_code=None), replace(good, rationale_ref=None), replace(good, rule_sources=()), replace(good, evidence_sources=()), replace(good, applicability=()), replace(good, required_confirmation=("Still needs confirmation",)), replace(good, status="UNKNOWN"), replace(good, rationale_ref="CG-NOT-IN-SOURCES")]:
            with self.subTest(bad=bad):
                result = self.payroll.allocate_payroll([self.record("E1", "100.00")], {"E1": bad})
                self.assertEqual(result.by_code, {})
                self.assertEqual(result.lines[0].status, "OPEN")
                self.assertIsNone(result.lines[0].class_code)
                self.assertTrue(result.lines[0].required_confirmation)
                self.assertTrue(result.reconciliation.reconciled)

    def test_code_contradicting_the_cited_guide_definition_stays_open(self):
        contradictory = replace(self.classified(), class_code="R-310")
        result = self.payroll.allocate_payroll([self.record("E1", "100.00")], {"E1": contradictory})
        self.assertEqual(result.by_code, {})
        self.assertEqual(result.lines[0].status, "OPEN")
        self.assertEqual(result.reconciliation.unresolved_total, Decimal("100.00"))

    def test_subcent_float_and_nonfinite_amounts_are_rejected_without_rounding(self):
        for amount in [Decimal("1.234"), Decimal("1.235"), Decimal("NaN"), Decimal("Infinity"), 0.1]:
            with self.subTest(amount=amount):
                record = replace(self.record("E1", "1.00"), wages=amount)
                with self.assertRaisesRegex(self.payroll.AllocationError, "E1"):
                    self.payroll.allocate_payroll([record], {})

    def test_exact_cent_trailing_zero_normalization_does_not_change_value(self):
        result = self.payroll.allocate_payroll([self.record("E1", "1.2300")], {"E1": self.classified()})
        self.assertEqual(str(result.by_code["C-110"]), "1.23")
        self.assertEqual(str(result.reconciliation.register_total), "1.23")
        self.assertEqual(str(result.lines[0].wages), "1.23")

    def test_aggregation_does_not_round_under_low_decimal_context_precision(self):
        with localcontext() as context:
            context.prec = 3
            result = self.payroll.allocate_payroll([self.record("E1", "9007199254740993.01"), self.record("E2", "0.02", 3)], {"E1": self.classified(), "E2": self.classified()})
            self.assertEqual(result.by_code, {"C-110": Decimal("9007199254740993.03")})
            self.assertEqual(result.reconciliation.register_total, Decimal("9007199254740993.03"))
            self.assertTrue(result.reconciliation.reconciled)

    def test_zero_wages_and_signed_corrections_remain_auditable(self):
        result = self.payroll.allocate_payroll([self.record("E1", "0.00"), self.record("E2", "-1.25", 3)], {"E1": self.classified(), "E2": self.classified("R-310", "CG-11")})
        self.assertEqual(result.by_code, {"R-310": Decimal("-1.25")})
        self.assertEqual(len(result.lines), 2)
        self.assertEqual(result.reconciliation.register_total, Decimal("-1.25"))
        self.assertTrue(result.reconciliation.reconciled)

    def test_independent_reconciliation_catches_missing_or_duplicate_lines(self):
        records = [self.record("E1", "100.00"), self.record("E2", "20.00", 3)]
        result = self.payroll.allocate_payroll(records, {"E1": self.classified(), "E2": self.classified()})
        check = self.payroll.reconcile_payroll(records, result.lines[:1])
        self.assertFalse(check.reconciled)
        self.assertEqual(check.difference, Decimal("20.00"))
        self.assertEqual(check.employee_differences, {"E1": Decimal("0.00"), "E2": Decimal("20.00")})
        with self.assertRaisesRegex(self.payroll.AllocationError, "duplicate"):
            self.payroll.reconcile_payroll(records, (result.lines[0], result.lines[0]))

    def test_independent_reconciliation_catches_offsetting_employee_errors(self):
        records = [self.record("E1", "100.00"), self.record("E2", "20.00", 3)]
        result = self.payroll.allocate_payroll(records, {"E1": self.classified(), "E2": self.classified()})
        lines = [replace(result.lines[0], wages=Decimal("90.00")), replace(result.lines[1], wages=Decimal("30.00"))]
        check = self.payroll.reconcile_payroll(records, lines)
        self.assertEqual(check.difference, Decimal("0.00"))
        self.assertFalse(check.reconciled)
        self.assertEqual(check.employee_differences, {"E1": Decimal("10.00"), "E2": Decimal("-10.00")})

    def test_reconciliation_catches_changed_parts_even_when_employee_total_matches(self):
        register = [self.record("E1", "100.00")]
        parts = [self.part("p1", "E1", "40.00", 2), self.part("p2", "E1", "60.00", 3)]
        decisions = {"p1": self.classified(scope="whole_pay_week"), "p2": self.classified("T-610", "CG-31", "whole_pay_week")}
        result = self.payroll.allocate_parts(register, parts, decisions)
        changed = [replace(result.lines[0], wages=Decimal("100.00")), replace(result.lines[1], wages=Decimal("0.00"))]
        check = self.payroll.reconcile_payroll(register, changed)
        self.assertFalse(check.reconciled)
        self.assertEqual(check.difference, Decimal("0.00"))
        self.assertEqual(check.employee_differences, {"E1": Decimal("0.00")})
        self.assertEqual(check.part_differences, {"p1": Decimal("-60.00"), "p2": Decimal("60.00")})

    def test_empty_register_reconciles_to_zero_without_outputs(self):
        result = self.payroll.allocate_payroll([], {})
        self.assertEqual(result.by_code, {})
        self.assertEqual(result.lines, ())
        self.assertTrue(result.reconciliation.reconciled)
        self.assertEqual(result.reconciliation.register_total, Decimal("0.00"))


if __name__ == "__main__":
    unittest.main()
