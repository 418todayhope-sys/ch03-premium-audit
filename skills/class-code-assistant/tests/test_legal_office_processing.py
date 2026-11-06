"""Integration of legal-office evidence without extending contractor practices."""

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
from test_employer_processing import GUIDE as RESTAURANT_GUIDE, INTERVIEW as RESTAURANT_INTERVIEW

GUIDE = RESTAURANT_GUIDE.replace("**CG-41.", "**CG-04. C-110 Clerical office employees.** Employees whose duties are confined to an office: correspondence,\nbookkeeping, dispatching by telephone or radio, drafting and estimating at a desk, and professional staff who work in\nthe office.\n\n**CG-41.")
INTERVIEW = RESTAURANT_INTERVIEW + """
**Nadia Brennan** · Voice · 06:03 PM

An office employee keeps the clerical code C-110 only if the site sign-in log shows them on a job site on four days or fewer in the audit period.

**Nadia Brennan** · Voice · 06:10 PM

If an office employee is on a job site for five or more days, their entire payroll moves to the employer's governing field code carrying the most payroll.

**Nadia Brennan** · Voice · 09:06 PM

Our sign-in day count rule was set up for contractors' office staff, and I have never applied it at an employer with no field code, so I have no practice for it.

**Nadia Brennan** · Voice · 09:11 PM

You should propose how you would treat it, write down why, and mark it as an open item for me or the employer to confirm. I don't settle these in this conversation.
"""
BUSINESS = """# Unrelated Counsel: business description
Audit period January 1, 2025 to December 31, 2025.
Unrelated Counsel is a law office handling closings, wills and business contracts.
"""
NOTES = """# Auditor's field notes
Office suite with five desks and a conference room. The attorneys appear in court
and meet clients at closings; neither is a job site. No one on staff does physical
work outside the office. No subcontractors, no travel pay.
"""
PAYROLL = """employee_id,name,position,wages_paid
Z1,Example First,Associate Attorney,101.01
Z2,Example Second,Associate Attorney,202.02
Z3,Example Visitor,Paralegal,30.03
Z4,Example Fourth,Legal Secretary,40.04
Z5,Example Fifth,Office Manager,50.05
"""
APPLICATION = """# Employer application
| Class code (employer's choice) | Employees | Payroll (USD) |
|---|---|---|
| C-110 | 5 | 423.15 |
"""
LOG_HEADER = "date,employee_id,name,site,signed_in_at\n"
DATES = ("2025-01-02", "2025-02-03", "2025-03-04", "2025-04-05", "2025-05-06", "2025-06-07")


class LegalOfficeIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.employer = self.root / "independent-input-location"
        self.employer.mkdir()
        self.guide = self.root / "classification.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview = self.root / "interview.md"
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        for filename, text in {"business-description.md": BUSINESS, "field-notes.md": NOTES,
                               "payroll-register.csv": PAYROLL, "application.md": APPLICATION}.items():
            (self.employer / filename).write_text(text, encoding="utf-8")
        self.set_log(DATES)

    def set_log(self, dates, employee="Z3", name="Example Visitor"):
        (self.employer / "site-signin-log.csv").write_text(LOG_HEADER + "".join(f"{day},{employee},{name},Synthetic Condominium,09:10\n" for day in dates), encoding="utf-8")

    def run_office(self, **kwargs):
        return process_employer(self.guide, self.employer, self.interview, **kwargs)

    def test_five_employees_reconcile_with_site_visitor_open_and_separate_proposal(self):
        result = self.run_office()
        self.assertEqual(result.by_code, {"C-110": Decimal("393.12")})
        self.assertEqual(result.decisions["Z3"].status, "OPEN")
        self.assertIsNone(result.decisions["Z3"].class_code)
        self.assertEqual(len(result.site_visits["Z3"]), 6)
        proposal = result.proposals["Z3"]
        self.assertEqual(proposal.class_code, "C-110")
        self.assertEqual(proposal.wages, Decimal("30.03"))
        self.assertTrue(proposal.required_confirmation)
        self.assertTrue(any(ref.locator == "CG-04" for ref in proposal.rule_sources))
        self.assertTrue(any("09:06 PM" in ref.locator for ref in result.decisions["Z3"].rule_sources))
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("423.15"))
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("30.03"))
        self.assertTrue(result.independent_reconciliation.reconciled)
        self.assertEqual(result.application.register_difference, Decimal("0.00"))
        self.assertEqual(result.application.verified_differences, {"C-110": Decimal("-30.03")})
        self.assertFalse(result.application.definitive)
        self.assertIsNone(result.receipts)
        self.assertFalse(any("receipt" in item.subject.lower() for item in result.open_items))
        self.assertTrue(any(item.proposed_treatment == proposal for item in result.open_items))

    def test_noncontractor_visits_do_not_acquire_a_threshold_exception(self):
        for count in (1, 4, 5, 6):
            with self.subTest(count=count):
                self.set_log(DATES[:count])
                result = self.run_office()
                self.assertEqual(result.decisions["Z3"].status, "OPEN")
                self.assertEqual(result.by_code, {"C-110": Decimal("393.12")})

    def test_equivalent_absence_statements_support_unvisited_office_staff(self):
        self.set_log(())
        for subject in ("No one on staff", "No employee", "No staff member"):
            for verb in ("does", "performs"):
                with self.subTest(subject=subject, verb=verb):
                    observation = f"{subject} {verb} physical work outside the office."
                    (self.employer / "field-notes.md").write_text(NOTES.replace(
                        "No one on staff does physical\nwork outside the office.", observation), encoding="utf-8")
                    result = self.run_office()
                    # Independent payroll control: 101.01+202.02+30.03+40.04+50.05.
                    self.assertEqual(result.by_code, {"C-110": Decimal("423.15")})
                    self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
                    self.assertEqual(result.independent_reconciliation.register_total, Decimal("423.15"))
                    self.assertTrue(result.independent_reconciliation.reconciled)
                    self.assertFalse(result.proposals)
                    for decision in result.decisions.values():
                        self.assertEqual((decision.status, decision.class_code, decision.rationale_ref),
                                         ("CLASSIFIED", "C-110", "CG-04"))
                        self.assertEqual({ref.locator for ref in decision.rule_sources}, {"CG-02", "CG-04"})
                        self.assertTrue(any(ref.source == str(self.employer / "field-notes.md")
                                            and observation in ref.excerpt for ref in decision.evidence_sources))

    def test_paraphrased_observations_preserve_legal_visit_boundaries(self):
        (self.employer / "field-notes.md").write_text(NOTES.replace(
            "No one on staff does physical\nwork outside the office.",
            "No employee performs physical work outside the office."), encoding="utf-8")
        for count in (0, 1, 4, 5, 6):
            with self.subTest(days=count):
                self.set_log(DATES[:count])
                result = self.run_office()
                decision = result.decisions["Z3"]
                # Any logged site exception requires review, independently of
                # the contractor's threshold; the remaining four wages = 393.12.
                self.assertEqual(result.by_code, {"C-110": Decimal("393.12" if count else "423.15")})
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("30.03" if count else "0.00"))
                self.assertEqual(len(result.site_visits["Z3"]), count)
                self.assertTrue(result.independent_reconciliation.reconciled)
                if count:
                    self.assertEqual((decision.status, decision.class_code), ("OPEN", None))
                    self.assertIn("no verified application", decision.reason)
                    self.assertTrue(any("09:06 PM" in ref.locator for ref in decision.rule_sources))
                    self.assertEqual((result.proposals["Z3"].class_code, result.proposals["Z3"].wages),
                                     ("C-110", Decimal("30.03")))
                    self.assertTrue(result.proposals["Z3"].required_confirmation)
                else:
                    self.assertEqual((decision.status, decision.class_code), ("CLASSIFIED", "C-110"))

    def test_qualified_absence_paraphrases_do_not_verify_office_duties(self):
        self.set_log(())
        for observation in (
            "It has not been confirmed that no employee performs physical work outside the office.",
            "No employee performs physical work outside the office, according to an unverified claim.",
            "No employee performs physical work outside the office except one assistant.",
            "No employee performs physical work outside the office?",
            "If no employee performs physical work outside the office, classification can be reviewed.",
            "Not every employee performs physical work outside the office.",
            "No employee may perform physical work outside the office.",
            "",  # Titles and an office suite do not supply missing duty evidence.
        ):
            with self.subTest(observation=observation):
                (self.employer / "field-notes.md").write_text(NOTES.replace(
                    "No one on staff does physical\nwork outside the office.", observation), encoding="utf-8")
                result = self.run_office()
                self.assertEqual(result.by_code, {})
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("423.15"))
                self.assertTrue(result.independent_reconciliation.reconciled)
                for key, decision in result.decisions.items():
                    self.assertEqual((decision.status, decision.class_code), ("OPEN", None))
                    self.assertTrue(decision.required_confirmation)
                    self.assertIsNone(result.proposals[key].class_code)

    def test_positive_absence_paraphrase_cannot_hide_conflicting_duty_evidence(self):
        self.set_log(())
        base = NOTES.replace("No one on staff does physical\nwork outside the office.",
                             "No employee performs physical work outside the office.")
        for conflict in (
            "Example First performs physical work outside the office.",
            "Some employees perform physical work outside the office.",
            "Example Fourth performs roofing work at construction sites.",
            "It has not been confirmed that no staff member does physical work outside the office.",
        ):
            with self.subTest(conflict=conflict):
                (self.employer / "field-notes.md").write_text(base + conflict + "\n", encoding="utf-8")
                result = self.run_office()
                self.assertEqual(result.by_code, {})
                self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("423.15"))
                self.assertTrue(result.independent_reconciliation.reconciled)
                for key, decision in result.decisions.items():
                    self.assertEqual((decision.status, decision.class_code), ("OPEN", None))
                    self.assertTrue(decision.required_confirmation)
                    self.assertIsNone(result.proposals[key].class_code)
                    self.assertTrue(any(conflict in ref.excerpt for ref in decision.evidence_sources))

    def test_adjacent_equivalent_absence_sentences_are_both_recognized(self):
        self.set_log(())
        observation = ("No employee performs physical work outside the office. "
                       "No one on staff does physical work outside the office.")
        (self.employer / "field-notes.md").write_text(NOTES.replace(
            "No one on staff does physical\nwork outside the office.", observation), encoding="utf-8")
        result = self.run_office()
        self.assertEqual(result.by_code, {"C-110": Decimal("423.15")})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("0.00"))
        self.assertTrue(result.independent_reconciliation.reconciled)

    def test_duplicate_signins_count_distinct_dates_and_preserve_both_source_rows(self):
        self.set_log((*DATES, DATES[0]))
        result = self.run_office()
        self.assertEqual(result.by_code, {"C-110": Decimal("393.12")})
        self.assertEqual(len(result.site_visits["Z3"]), 6)
        refs = [ref for ref in result.decisions["Z3"].evidence_sources if ref.source.endswith("site-signin-log.csv")]
        self.assertEqual(len(refs), 7)

    def test_new_logged_employee_changes_decision_on_fresh_run(self):
        self.assertEqual(self.run_office().decisions["Z2"].class_code, "C-110")
        path = self.employer / "site-signin-log.csv"
        path.write_text(path.read_text() + "2025-07-08,Z2,Example Second,Synthetic Condominium,10:00\n", encoding="utf-8")
        result = self.run_office()
        self.assertEqual(result.decisions["Z2"].status, "OPEN")
        self.assertEqual(result.by_code, {"C-110": Decimal("191.10")})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("232.05"))

    def test_missing_log_is_unknown_rather_than_zero_visits(self):
        (self.employer / "site-signin-log.csv").unlink()
        result = self.run_office()
        self.assertEqual(result.by_code, {})
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("423.15"))
        self.assertNotIn("Z3", result.site_visits)

    def test_unknown_log_identity_blocks_inference_and_requires_confirmation(self):
        self.set_log(DATES, employee="MISSING")
        result = self.run_office()
        self.assertEqual(result.by_code, {})
        self.assertTrue(any("identity" in item.reason.lower() for item in result.open_items))

    def test_conflicting_log_id_cannot_classify_the_named_worker_as_unvisited(self):
        self.set_log(DATES, employee="Z1", name="Example Visitor")
        result = self.run_office()
        self.assertEqual(result.decisions["Z1"].status, "OPEN")
        self.assertEqual(result.decisions["Z3"].status, "OPEN")
        self.assertTrue(any("identity" in item.reason.lower() for item in result.open_items))

    def test_name_mismatch_or_invalid_visit_date_remains_open_with_original_row(self):
        for dates, name in [(DATES, "Wrong Person"), (("2026-01-01",), "Example Visitor"), (("not-a-date",), "Example Visitor")]:
            with self.subTest(dates=dates, name=name):
                self.set_log(dates, name=name)
                result = self.run_office()
                self.assertEqual(result.decisions["Z3"].status, "OPEN")
                self.assertTrue(any(ref.source.endswith("site-signin-log.csv") for ref in result.decisions["Z3"].evidence_sources))
                self.assertTrue(result.independent_reconciliation.reconciled)

    def test_unknown_role_or_contradictory_duties_cannot_be_classified_by_title(self):
        path = self.employer / "payroll-register.csv"
        path.write_text(PAYROLL.replace("Legal Secretary", "Carpenter"), encoding="utf-8")
        result = self.run_office()
        self.assertEqual(result.decisions["Z4"].status, "OPEN")
        path.write_text(PAYROLL, encoding="utf-8")
        (self.employer / "field-notes.md").write_text(NOTES + "Z1 performs roofing work at construction sites.\n", encoding="utf-8")
        self.assertEqual(self.run_office().by_code, {})

    def test_negated_or_unconfirmed_observations_do_not_verify_office_duties(self):
        for text in [NOTES.replace("Office suite", "Not an office suite"),
                     NOTES.replace("No one on staff does physical\nwork outside the office.", "It has not been confirmed that no one on staff does physical work outside the office."),
                     NOTES + "It has not been confirmed that no one on staff does physical work outside the office.\n"]:
            with self.subTest(text=text):
                (self.employer / "field-notes.md").write_text(text, encoding="utf-8")
                self.assertEqual(self.run_office().by_code, {})

    def test_missing_or_changed_guide_does_not_create_office_classification(self):
        self.guide.write_text(GUIDE.replace("and professional staff who work in", "THIS CLASS IS RETIRED;"), encoding="utf-8")
        result = self.run_office()
        self.assertEqual(result.by_code, {})
        self.assertEqual(result.decisions["Z3"].status, "OPEN")

    def test_policy_after_a_heading_cannot_be_discarded_by_source_guard(self):
        revised = GUIDE.replace("**CG-41.", "### C-110 revised restriction\n\nC-110 excludes professional legal staff.\n\n**CG-41.")
        self.guide.write_text(revised, encoding="utf-8")
        self.assertEqual(self.run_office().by_code, {})

    def test_missing_scope_clarification_keeps_visits_open_and_requests_source_review(self):
        self.interview.write_text(INTERVIEW.replace("so I have no practice for it.", "UNVERIFIED CHANGED PRACTICE"), encoding="utf-8")
        result = self.run_office()
        self.assertEqual(result.by_code, {"C-110": Decimal("393.12")})
        self.assertEqual(result.decisions["Z3"].status, "OPEN")
        self.assertIn("source", result.decisions["Z3"].reason.lower())

    def test_configurable_signin_path_and_low_precision_preserve_cents(self):
        (self.employer / "site-signin-log.csv").rename(self.employer / "visits.csv")
        files = replace(EmployerFiles(), site_signins="visits.csv")
        with localcontext() as context:
            context.prec = 3
            result = self.run_office(files=files)
        self.assertEqual(result.by_code, {"C-110": Decimal("393.12")})
        self.assertEqual(result.independent_reconciliation.difference, Decimal("0.00"))
        self.assertTrue(any(ref.source.endswith("visits.csv") for ref in result.decisions["Z3"].evidence_sources))

    def test_application_discrepancy_does_not_change_register_or_open_wages(self):
        (self.employer / "application.md").write_text(APPLICATION.replace("423.15", "400.00"), encoding="utf-8")
        result = self.run_office()
        self.assertEqual(result.application.register_difference, Decimal("23.15"))
        self.assertEqual(result.independent_reconciliation.register_total, Decimal("423.15"))

    def test_unmapped_source_and_missing_field_notes_prevent_unreviewed_classification(self):
        (self.employer / "individual-duties.md").write_text("A separate duty record needs review.", encoding="utf-8")
        self.assertEqual(self.run_office().by_code, {})
        (self.employer / "individual-duties.md").unlink()
        (self.employer / "field-notes.md").unlink()
        self.assertEqual(self.run_office().by_code, {})


class LocalHarborIntegrationTest(unittest.TestCase):
    def test_actual_five_employees_and_six_site_visits(self):
        root = Path(os.environ.get("INSURANCE01_TEST_INPUTS", "/home/maxg/insurance01-inputs"))
        interview = COMPONENT.parents[1] / "interviews" / "ch03-premium-audit-20261105-0222(1).md"
        if not root.is_dir() or not interview.is_file():
            self.skipTest("Authoritative local development snapshots are unavailable")
        employer = root / "employer-files" / "harbor-point-legal"
        result = process_employer(root / "classification-guide.md", employer, interview)
        self.assertEqual(result.by_code, {"C-110": Decimal("360935.68")})
        self.assertEqual(result.decisions["HP-E03"].status, "OPEN")
        self.assertEqual(len(result.site_visits["HP-E03"]), 6)
        self.assertEqual(result.proposals["HP-E03"].class_code, "C-110")
        self.assertEqual(result.proposals["HP-E03"].wages, Decimal("64212.48"))
        self.assertEqual(result.independent_reconciliation.unresolved_total, Decimal("64212.48"))
        raw = list(csv.DictReader(io.StringIO((employer / "payroll-register.csv").read_text())))
        self.assertEqual(sum(Decimal(row["wages_paid"]) for row in raw), Decimal("425148.16"))
        self.assertEqual(sum(line.wages for line in result.allocation.lines), Decimal("425148.16"))
        self.assertTrue(result.independent_reconciliation.reconciled)
        self.assertEqual(result.independent_reconciliation.difference, Decimal("0.00"))
        self.assertEqual(result.application.register_difference, Decimal("0.00"))
        self.assertEqual(result.application.verified_differences, {"C-110": Decimal("-64212.48")})
        self.assertEqual({line.class_code for line in result.allocation.lines if line.class_code}, {"C-110"})


if __name__ == "__main__":
    unittest.main()
