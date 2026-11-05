"""Synthetic source-bound adjustments; proposals must never affect verified totals."""

from dataclasses import replace
from datetime import date
from decimal import Decimal, localcontext
import hashlib
import importlib
from pathlib import Path
import sys
import tempfile
import unittest


COMPONENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPONENT))
from rule_evaluator import Decision, SourceReference

GUIDE = """# Synthetic guide
**CG-03. Payroll.** Payroll is the gross remuneration paid to employees for the period: wages, salaries, commissions
and bonuses. Expense reimbursements that the employer can document, such as travel and lodging costs, are not payroll.

**CG-06. Subcontractors.** Payments to a subcontractor who does not carry workers' compensation insurance for its own
workers may be treated as payroll of the employer, under the code for the work the subcontractor performed.

**CG-11. R-310 Roofing.** Roofing work.

**CG-21. E-510 Electrical wiring.** Electrical work.
"""
INTERVIEW = """# Synthetic interview
**Nadia Brennan** · Voice · 06:12 PM

A certificate of insurance covering the whole audit period. If a subcontractor can't show one, payments to them are added to the payroll at 60 percent.

**Nadia Brennan** · Voice · 06:12 PM

A certificate that lapses partway through counts as no certificate at all, so we add the subcontractor's payments to payroll at 60 percent.

**Nadia Brennan** · Voice · 09:08 PM

I have not had a certificate come back in a name that differs from the name on the payments, so I have no practice for deciding if it is the same subcontractor.

**Nadia Brennan** · Voice · 09:09 PM

Yes, if the documentation is missing, it counts as no certificate and the payments are added to the payroll at 60 percent.

**Nadia Brennan** · Voice · 06:05 PM

A daily allowance paid to crews working out-of-town is left out of payroll up to forty-seven dollars per worker per day. Anything paid above that amount counts as payroll.

**Nadia Brennan** · Voice · 09:09 PM

I have no clear practice for someone receiving a daily allowance with no out-of-town days. Propose how you would handle it and why, and mark it as an open item.
"""


class PayrollAdjustmentTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue((COMPONENT / "payroll_adjustments.py").is_file(), "Payroll adjustments are not implemented")
        self.adjustments = importlib.import_module("payroll_adjustments")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.guide = self.root / "guide.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview = self.root / "interview.md"
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        self.engine = self.adjustments.PayrollAdjuster.from_paths(self.guide, self.interview)
        self.period = self.adjustments.AuditPeriod(date(2025, 1, 1), date(2025, 12, 31))
        self.search_source = SourceReference("synthetic/certificate-register.csv", "complete register and auditor search")

    def classification(self, code="R-310", paragraph="CG-11"):
        excerpt = "**CG-11. R-310 Roofing.** Roofing work." if code == "R-310" else "**CG-21. E-510 Electrical wiring.** Electrical work."
        ref = SourceReference(str(self.guide), paragraph, excerpt=excerpt, sha256=hashlib.sha256(GUIDE.encode()).hexdigest())
        return Decision("documented_work", "CLASSIFIED", code, paragraph, "Documented synthetic work.", (), (ref,), (SourceReference("synthetic/duties.md", "paragraph 1"),), ("actual documented work",), "whole_audit_period")

    def subcontractor(self, amount="100.00", **changes):
        payment = self.adjustments.SubcontractorPayment("P1", "Synthetic Roofing LLC", date(2025, 6, 1), "roofing", Decimal(amount), SourceReference("synthetic/payments.csv", "line 2", 2, 2, f"P1,{amount}"), self.classification())
        values = dict(period=self.period, payment=payment, certificates=(), search_complete=True, search_source=self.search_source)
        values.update(changes)
        return self.adjustments.SubcontractorCase(**values)

    def certificate(self, start=None, end=None, name="Synthetic Roofing LLC", number="CERT-1"):
        return self.adjustments.Certificate(number, name, start or date(2025, 1, 1), end or date(2025, 12, 31), SourceReference("synthetic/certificates.csv", number))

    def travel(self, amount="100.00", days=2, **changes):
        allowance = self.adjustments.TravelAllowance("A1", "E1", "Synthetic worker", Decimal(amount), days, SourceReference("synthetic/payroll.csv", "line 2", 2, 2, f"E1,{amount},{days}"), SourceReference("synthetic/travel-log.csv", "documented audited-period days"), True, True, self.classification("E-510", "CG-21"))
        if type(days) is int and 0 < days <= 365 and Decimal(amount) >= 0:
            numerator, denominator = Decimal(amount).as_integer_ratio()
            cents = numerator * 100 // denominator
            quotient, remainder = divmod(cents, days)
            daily = []
            for index in range(days):
                paid = quotient + (index < remainder)
                daily.append(self.adjustments.DailyAllowance(date.fromordinal(self.period.start.toordinal() + index), Decimal(f"{paid // 100}.{paid % 100:02d}"), SourceReference("synthetic/daily-allowances.csv", f"day {index + 1}")))
            allowance = replace(allowance, daily_payments=tuple(daily))
        allowance = replace(allowance, **changes)
        return self.adjustments.TravelCase(self.period, allowance)

    def assert_verified(self, line, payroll, nonpayroll):
        self.assertEqual(line.status, "VERIFIED")
        self.assertEqual(line.payroll_added, Decimal(payroll))
        self.assertEqual(line.nonpayroll, Decimal(nonpayroll))
        self.assertEqual(line.unresolved_basis, Decimal("0.00"))
        self.assertTrue(line.rule_sources)
        self.assertTrue(line.evidence_sources)
        self.assertIsNone(line.proposal)

    def assert_open(self, line):
        self.assertEqual(line.status, "OPEN")
        self.assertEqual(line.payroll_added, Decimal("0.00"))
        self.assertEqual(line.nonpayroll, Decimal("0.00"))
        self.assertEqual(line.unresolved_basis, line.input_record.amount)
        self.assertIsNone(line.class_code)
        self.assertIsNone(line.rationale_ref)
        self.assertTrue(line.reason)
        self.assertTrue(line.required_confirmation)

    def test_full_period_certificate_inclusive_endpoints_excludes_payment(self):
        for cert in [self.certificate(), self.certificate(date(2024, 1, 1), date(2026, 1, 1))]:
            with self.subTest(cert=cert):
                line = self.engine.subcontractor(self.subcontractor(certificates=(cert,)))
                self.assert_verified(line, "0.00", "100.00")
                self.assertIsNone(line.class_code)

    def test_missing_expired_late_start_and_early_end_certificates_add_sixty_percent(self):
        for certs in [(), (self.certificate(date(2024, 1, 1), date(2024, 12, 31)),), (self.certificate(start=date(2025, 1, 2)),), (self.certificate(end=date(2025, 12, 30)),)]:
            with self.subTest(certs=certs):
                line = self.engine.subcontractor(self.subcontractor(certificates=certs))
                self.assert_verified(line, "60.00", "40.00")
                self.assertEqual((line.class_code, line.rationale_ref), ("R-310", "CG-11"))

    def test_certificate_name_mismatch_never_assumes_identity(self):
        for name in ["Synthetic Roofing", "SYNTHETIC ROOFING LLC", "Other contractor"]:
            with self.subTest(name=name):
                line = self.engine.subcontractor(self.subcontractor(certificates=(self.certificate(name=name),)))
                self.assert_open(line)
                self.assertIn("name", line.reason.lower())

    def test_unknown_certificate_inventory_or_missing_dates_stay_open(self):
        for changes in [{"certificates": None}, {"search_complete": False}, {"search_source": None}, {"certificates": (replace(self.certificate(), coverage_to=None),)}, {"certificates": (replace(self.certificate(), coverage_from=date(2026, 1, 1)),)}]:
            with self.subTest(changes=changes):
                self.assert_open(self.engine.subcontractor(self.subcontractor(**changes)))

    def test_full_certificate_proof_does_not_require_exhaustive_missing_document_search(self):
        case = self.subcontractor(certificates=(self.certificate(),), search_complete=False, search_source=None)
        self.assert_verified(self.engine.subcontractor(case), "0.00", "100.00")

    def test_multiple_partial_certificates_are_not_silently_stitched_into_full_coverage(self):
        certs = (self.certificate(end=date(2025, 6, 30)), self.certificate(start=date(2025, 7, 1), number="CERT-2"))
        self.assert_open(self.engine.subcontractor(self.subcontractor(certificates=certs)))

    def test_unknown_work_code_and_out_of_period_payments_stay_open(self):
        case = self.subcontractor()
        for payment in [replace(case.payment, decision=None), replace(case.payment, work=""), replace(case.payment, payment_date=date(2026, 1, 1))]:
            with self.subTest(payment=payment):
                self.assert_open(self.engine.subcontractor(replace(case, payment=payment)))

    def test_subcent_sixty_percent_is_unrounded_proposal_not_verified_money(self):
        line = self.engine.subcontractor(self.subcontractor("0.01"))
        self.assert_open(line)
        self.assertEqual(line.proposal.payroll_added, Decimal("0.006"))
        self.assertEqual(line.proposal.nonpayroll, Decimal("0.004"))
        self.assertIn("round", line.reason.lower())

    def test_allowance_below_at_and_above_cap(self):
        for amount, included, excluded in [("90.00", "0.00", "90.00"), ("94.00", "0.00", "94.00"), ("94.01", "0.01", "94.00"), ("100.00", "6.00", "94.00")]:
            with self.subTest(amount=amount):
                line = self.engine.travel(self.travel(amount))
                self.assert_verified(line, included, excluded)
                self.assertEqual(line.class_code, "E-510" if Decimal(included) else None)

    def test_zero_documented_days_requires_open_unapproved_full_inclusion_proposal(self):
        line = self.engine.travel(self.travel("390.00", 0))
        self.assert_open(line)
        self.assertEqual(line.proposal.payroll_added, Decimal("390.00"))
        self.assertEqual(line.proposal.nonpayroll, Decimal("0.00"))
        self.assertIn("propos", line.proposal.reason.lower())

    def test_daily_caps_do_not_pool_unused_exclusions_between_days(self):
        case = self.travel()
        daily = tuple(replace(item, amount=Decimal(amount)) for item, amount in zip(case.allowance.daily_payments, ("90.00", "10.00")))
        line = self.engine.travel(replace(case, allowance=replace(case.allowance, daily_payments=daily)))
        self.assert_verified(line, "43.00", "57.00")
        self.assertTrue(all(item.source in line.evidence_sources for item in daily))

    def test_day_count_and_total_without_daily_payment_basis_remain_open(self):
        self.assert_open(self.engine.travel(self.travel(daily_payments=None)))

    def test_uniform_daily_rate_requires_source_and_reconciliation_to_total(self):
        rate_source = SourceReference("synthetic/allowance-policy.md", "documented worker daily rate")
        self.assert_verified(self.engine.travel(self.travel(daily_payments=None, uniform_daily_amount=Decimal("50.00"), rate_source=rate_source)), "6.00", "94.00")
        for changes in [{"rate_source": None}, {"uniform_daily_amount": Decimal("49.00")}, {"uniform_daily_amount": Decimal("-1.00")}]:
            values = dict(daily_payments=None, uniform_daily_amount=Decimal("50.00"), rate_source=rate_source)
            values.update(changes)
            self.assert_open(self.engine.travel(self.travel(**values)))

    def test_invalid_or_incomplete_daily_payment_evidence_remains_open(self):
        case = self.travel()
        one, two = case.allowance.daily_payments
        for daily in [(one,), (one, replace(two, day=one.day)), (one, replace(two, day=date(2026, 1, 1))), (one, replace(two, amount=Decimal("49.00"))), (one, replace(two, source=None)), (one, replace(two, amount=Decimal("-50.00")))]:
            with self.subTest(daily=daily):
                self.assert_open(self.engine.travel(replace(case, allowance=replace(case.allowance, daily_payments=daily))))

    def test_malformed_worker_ids_cannot_bypass_worker_period_duplicate_guard(self):
        for employee in ["", "   ", "E1 ", " E1"]:
            with self.subTest(employee=employee):
                with self.assertRaisesRegex(self.adjustments.AdjustmentError, "identifier"):
                    self.engine.travel(self.travel(employee_id=employee))

    def test_stale_classification_definition_requires_rereading_current_guide(self):
        case = self.travel()
        self.guide.write_text(GUIDE.replace("Electrical work.", "This code is retired; obtain auditor confirmation."), encoding="utf-8")
        engine = self.adjustments.PayrollAdjuster.from_paths(self.guide, self.interview)
        self.assert_open(engine.travel(case))

    def test_missing_undocumented_or_invalid_days_do_not_become_zero(self):
        for changes in [{"travel_days": None}, {"travel_days": -1}, {"travel_days": True}, {"travel_days": 1.5}, {"days_complete": False}, {"days_source": None}]:
            with self.subTest(changes=changes):
                line = self.engine.travel(self.travel(**changes))
                self.assert_open(line)

    def test_documented_day_count_cannot_exceed_days_in_the_audit_period(self):
        one_day = self.adjustments.AuditPeriod(date(2025, 1, 1), date(2025, 1, 1))
        self.assert_open(self.engine.travel(replace(self.travel(days=2), period=one_day)))

    def test_allowance_must_be_separate_from_base_wages_before_addition(self):
        for value in [False, None]:
            with self.subTest(value=value):
                self.assert_open(self.engine.travel(self.travel(separate_from_base=value)))

    def test_positive_excess_needs_verified_classification_but_full_exclusion_does_not(self):
        self.assert_open(self.engine.travel(self.travel(decision=None)))
        self.assert_verified(self.engine.travel(self.travel("94.00", decision=None)), "0.00", "94.00")

    def test_zero_allowance_has_no_money_movement_or_false_open_exposure(self):
        self.assert_verified(self.engine.travel(self.travel("0.00", 0, decision=None)), "0.00", "0.00")

    def test_large_calculations_are_exact_under_low_decimal_precision(self):
        with localcontext() as context:
            context.prec = 3
            self.assert_verified(self.engine.subcontractor(self.subcontractor("1000000000000000000000.05")), "600000000000000000000.03", "400000000000000000000.02")
            self.assert_verified(self.engine.travel(self.travel("1000000000000000000000.01", 1)), "999999999999999999953.01", "47.00")

    def test_invalid_currency_is_rejected_and_negative_inputs_remain_open(self):
        for amount in [0.1, Decimal("NaN"), Decimal("Infinity"), Decimal("1.001")]:
            with self.subTest(amount=amount):
                case = self.travel()
                case = replace(case, allowance=replace(case.allowance, amount=amount))
                with self.assertRaises(self.adjustments.AdjustmentError):
                    self.engine.travel(case)
        self.assert_open(self.engine.travel(self.travel("-1.00")))
        self.assert_open(self.engine.subcontractor(self.subcontractor("-1.00")))

    def test_batch_reconciles_verified_nonpayroll_and_unresolved_basis_separately(self):
        result = self.engine.evaluate_batch((self.subcontractor(),), (self.travel(), self.travel("390.00", 0, allowance_id="A2", employee_id="E2", source=SourceReference("synthetic/payroll.csv", "line 3", 3, 3))))
        self.assertEqual(result.by_code, {"R-310": Decimal("60.00"), "E-510": Decimal("6.00")})
        self.assertEqual(result.reconciliation.basis_total, Decimal("590.00"))
        self.assertEqual(result.reconciliation.payroll_added, Decimal("66.00"))
        self.assertEqual(result.reconciliation.nonpayroll, Decimal("134.00"))
        self.assertEqual(result.reconciliation.unresolved_basis, Decimal("390.00"))
        self.assertEqual(result.reconciliation.difference, Decimal("0.00"))
        self.assertTrue(result.reconciliation.reconciled)

    def test_proposals_never_enter_verified_totals(self):
        result = self.engine.evaluate_batch((self.subcontractor("0.01"),), (self.travel("390.00", 0),))
        self.assertEqual(result.by_code, {})
        self.assertEqual(result.reconciliation.payroll_added, Decimal("0.00"))
        self.assertEqual(result.reconciliation.nonpayroll, Decimal("0.00"))
        self.assertEqual(result.reconciliation.unresolved_basis, Decimal("390.01"))
        self.assertTrue(result.reconciliation.reconciled)

    def test_duplicate_payment_ids_and_relabelled_rows_are_rejected(self):
        case = self.subcontractor()
        for second in [case, replace(case, payment=replace(case.payment, payment_id="P2"))]:
            with self.subTest(second=second):
                with self.assertRaisesRegex(self.adjustments.AdjustmentError, "duplicate"):
                    self.engine.evaluate_batch((case, second), ())

    def test_worker_period_allowance_cannot_receive_daily_cap_twice(self):
        one = self.travel()
        two = self.travel(allowance_id="A2", source=SourceReference("synthetic/payroll.csv", "line 3", 3, 3))
        with self.assertRaisesRegex(self.adjustments.AdjustmentError, "worker"):
            self.engine.evaluate_batch((), (one, two))

    def test_daily_monetary_evidence_cannot_be_reused_by_another_case(self):
        one = self.travel()
        two = self.travel(allowance_id="A2", employee_id="E2", source=SourceReference("synthetic/payroll.csv", "line 3", 3, 3))
        with self.assertRaisesRegex(self.adjustments.AdjustmentError, "duplicate"):
            self.engine.evaluate_batch((), (one, two))
        two = replace(two, allowance=replace(two.allowance, daily_payments=None, uniform_daily_amount=Decimal("50.00"), rate_source=self.search_source, source=one.allowance.daily_payments[0].source))
        with self.assertRaisesRegex(self.adjustments.AdjustmentError, "duplicate"):
            self.engine.evaluate_batch((), (one, two))

    def test_common_rate_source_can_support_distinct_workers_without_double_counting(self):
        values = dict(daily_payments=None, uniform_daily_amount=Decimal("50.00"), rate_source=SourceReference("synthetic/allowance-policy.md", "worker daily rate"))
        one = self.travel(**values)
        two = self.travel(allowance_id="A2", employee_id="E2", source=SourceReference("synthetic/payroll.csv", "line 3", 3, 3), **values)
        result = self.engine.evaluate_batch(travel=(one, two))
        self.assertTrue(result.reconciliation.reconciled)
        self.assertEqual(result.reconciliation.payroll_added, Decimal("12.00"))

    def test_one_day_summary_may_reference_its_own_daily_monetary_row(self):
        case = self.travel("50.00", 1)
        case = replace(case, allowance=replace(case.allowance, source=case.allowance.daily_payments[0].source))
        result = self.engine.evaluate_batch(travel=(case,))
        self.assertTrue(result.reconciliation.reconciled)
        self.assertEqual(result.reconciliation.payroll_added, Decimal("3.00"))

    def test_original_input_objects_certificates_and_rule_sources_are_preserved(self):
        case = self.subcontractor(certificates=(self.certificate(end=date(2025, 6, 30)),))
        line = self.engine.subcontractor(case)
        self.assertIs(line.input_record, case.payment)
        self.assertEqual(line.certificates, case.certificates)
        self.assertIn(case.payment.source, line.evidence_sources)
        self.assertIn(case.certificates[0].source, line.evidence_sources)
        self.assertTrue(any(ref.locator == "CG-06" for ref in line.rule_sources))
        self.assertTrue(any("06:12 PM" in ref.locator for ref in line.rule_sources))
        for ref in line.rule_sources:
            if ref.source == str(self.interview):
                self.assertEqual(len(ref.sha256), 64)
                self.assertIn(ref.excerpt, "\n".join(INTERVIEW.splitlines()[ref.line_start - 1:ref.line_end]))

    def test_changed_or_missing_authoritative_rules_stay_open(self):
        for old in ["at 60 percent", "forty-seven dollars"]:
            with self.subTest(old=old):
                self.interview.write_text(INTERVIEW.replace(old, "unverified policy"), encoding="utf-8")
                engine = self.adjustments.PayrollAdjuster.from_paths(self.guide, self.interview)
                line = engine.subcontractor(self.subcontractor()) if old == "at 60 percent" else engine.travel(self.travel())
                self.assert_open(line)
        engine = self.adjustments.PayrollAdjuster.from_paths(self.root / "missing-guide.md", self.interview)
        self.assert_open(engine.travel(self.travel()))

    def test_changed_written_rule_is_not_accepted_only_because_identifier_matches(self):
        for old, rule in [("workers may be treated as payroll", "subcontractor"), ("are not payroll.", "travel")]:
            with self.subTest(rule=rule):
                self.guide.write_text(GUIDE.replace(old, "UNVERIFIED CHANGED WRITTEN POLICY"), encoding="utf-8")
                engine = self.adjustments.PayrollAdjuster.from_paths(self.guide, self.interview)
                line = engine.subcontractor(self.subcontractor()) if rule == "subcontractor" else engine.travel(self.travel())
                self.assert_open(line)

    def test_reconciliation_against_input_cases_detects_an_entire_missing_output(self):
        cases = (self.subcontractor(), self.travel())
        lines = (self.engine.subcontractor(cases[0]),)
        check = self.adjustments.reconcile_adjustments(lines, expected_cases=cases)
        self.assertFalse(check.reconciled)
        self.assertEqual(check.basis_total, Decimal("200.00"))
        self.assertEqual(check.difference, Decimal("100.00"))
        self.assertEqual(check.record_differences[("travel", "A1")], Decimal("100.00"))

    def test_missing_zero_amount_record_still_fails_source_completeness(self):
        case = self.travel("0.00", 0)
        check = self.adjustments.reconcile_adjustments((), expected_cases=(case,))
        self.assertFalse(check.reconciled)
        self.assertEqual(check.difference, Decimal("0.00"))
        self.assertEqual(check.missing_records, (("travel", "A1"),))

    def test_independent_reconciliation_catches_compensating_per_record_errors(self):
        one = self.engine.subcontractor(self.subcontractor())
        two = self.engine.travel(self.travel())
        tampered = (replace(one, nonpayroll=Decimal("30.00")), replace(two, nonpayroll=Decimal("104.00")))
        check = self.adjustments.reconcile_adjustments(tampered)
        self.assertEqual(check.difference, Decimal("0.00"))
        self.assertFalse(check.reconciled)
        self.assertTrue(any(value != 0 for value in check.record_differences.values()))


if __name__ == "__main__":
    unittest.main()
