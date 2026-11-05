"""Audit report contracts against synthetic inputs and the six preserved results."""

from copy import deepcopy
import csv
from decimal import localcontext
import hashlib
import importlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from test_electrical_processing import APPLICATION, BUSINESS, GUIDE, INTERVIEW, NOTES, PAYROLL, SIGNINS
from audit_questions import generate_questions
from generate_codes import generate_csvs

COMPONENT = Path(__file__).resolve().parents[1]
REPO = COMPONENT.parents[1]
CLI = COMPONENT / "audit_report.py"


class AuditReportTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(CLI.is_file(), "Reusable audit-report generator is missing")
        self.module = importlib.import_module("audit_report")
        temporary = tempfile.TemporaryDirectory(prefix="report current inputs ")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.employer = self.root / "new-electrical-business"
        self.employer.mkdir()
        self.guide, self.interview = self.root / "guide.md", self.root / "interview.md"
        self.guide.write_text(GUIDE)
        self.interview.write_text(INTERVIEW)
        for filename, content in {"business-description.md": BUSINESS, "field-notes.md": NOTES,
                "payroll-register.csv": PAYROLL, "application.md": APPLICATION, "site-signin-log.csv": SIGNINS}.items():
            (self.employer / filename).write_text(content)
        self.codes, self.review = self.root / "codes", self.root / "review.json"
        self.questions, self.output = self.root / "questions.md", self.root / "report.md"
        self.prepare()

    def prepare(self):
        self.state = generate_csvs(self.guide, self.interview, employer=self.employer,
                                  output_dir=self.codes, review_state=self.review)
        generate_questions(self.review, codes_dir=self.codes, output=self.questions)

    def generate(self, **kwargs):
        return self.module.generate_report(self.review, codes_dir=self.codes,
                    questions=self.questions, output=kwargs.pop("output", self.output), **kwargs)

    def test_new_employer_report_keeps_exact_csv_codes_differences_and_reconciliation(self):
        report = self.generate()
        text = self.output.read_text()
        self.assertEqual(report["uncovered"], {})
        self.assertEqual(report["employers"][0]["disposition"], "PARTIALLY UNRESOLVED")
        self.assertIn("| C-110 | 120.02 | 20.02 | -100.00 | CG-04 |", text)
        self.assertIn("| E-510 | 80.08 | 186.08 | 106.00 | CG-21 |", text)
        self.assertIn("200.10 + 6.00 = 206.10 + 0.00", text)
        self.assertIn("304.00 = 206.10 + 0.00 + 94.00 + 3.90", text)
        self.assertIn("Independent Electric", text)

    def test_every_employee_and_payment_is_identified_with_amount_and_reason(self):
        self.generate()
        text = self.output.read_text()
        for employee in self.state["processing"]["employers"][0]["employee_payroll"]:
            self.assertIn(employee["employee_id"], text)
            self.assertIn(employee["name"], text)
            self.assertIn(employee["register_wages"], text)
        for line in self.state["processing"]["employers"][0]["adjustments"]["lines"]:
            self.assertIn(line["adjustment_id"], text)
            self.assertIn(line["reason"], text)
            self.assertIn(line["input_record"]["amount"], text)

    def test_open_proposal_is_unapproved_and_human_roles_are_explicit(self):
        self.generate()
        text = self.output.read_text()
        self.assertIn("UNAPPROVED PROPOSED treatments", text)
        self.assertIn("travel:A1", text)
        self.assertIn("3.90", text)
        self.assertIn("Employer payroll/records contact", text)
        self.assertIn("Responsible policy reviewer: auditor", text)
        self.assertIn("already included", text)
        self.assertIn("CG-03", text)

    def test_repeat_invocation_preserves_all_inputs_and_output_mtime(self):
        paths = [self.guide, self.interview, self.review, self.questions,
                 *self.employer.iterdir(), *self.codes.iterdir()]
        before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths}
        first = self.generate()
        time = self.output.stat().st_mtime_ns
        self.assertEqual(first, self.generate())
        self.assertEqual(time, self.output.stat().st_mtime_ns)
        self.assertEqual(before, {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths})

    def test_tampered_questions_are_not_rewritten_or_accepted(self):
        self.questions.write_text(self.questions.read_text().replace("All questions are unanswered.", "Approved."))
        before = self.questions.read_bytes()
        with self.assertRaisesRegex(self.module.ReportGenerationError, "question"):
            self.generate()
        self.assertEqual(before, self.questions.read_bytes())
        self.assertFalse(self.output.exists())

    def test_missing_questions_raise_clear_error_without_generating_them(self):
        self.questions.unlink()
        with self.assertRaisesRegex(self.module.ReportGenerationError, "question|questions.md"):
            self.generate()
        self.assertFalse(self.questions.exists())
        self.assertFalse(self.output.exists())

    def test_stale_source_blocks_report(self):
        self.guide.write_text(GUIDE + "\nChanged current edition.\n")
        with self.assertRaisesRegex(self.module.ReportGenerationError, "source|state"):
            self.generate()
        self.assertFalse(self.output.exists())

    def test_tampered_csv_and_review_state_block_report(self):
        path = next(self.codes.iterdir())
        original = path.read_bytes()
        path.write_bytes(original.replace(b"186.08", b"186.09"))
        with self.assertRaises(self.module.ReportGenerationError):
            self.generate()
        path.write_bytes(original)
        state = deepcopy(self.state)
        state["processing"]["employers"][0]["open_adjustment_basis"] = "0.00"
        self.review.write_text(json.dumps(state))
        with self.assertRaises(self.module.ReportGenerationError):
            self.generate()
        self.assertFalse(self.output.exists())

    def test_output_cannot_overwrite_sources_dependencies_or_operator_work(self):
        self.output.write_text("Operator report\n")
        for output in (self.guide, self.review, self.questions, next(self.codes.iterdir()),
                       self.employer / "new.md", self.output):
            with self.subTest(output=output), self.assertRaises(self.module.ReportGenerationError):
                self.generate(output=output)
        self.assertEqual(self.output.read_text(), "Operator report\n")

    def test_symlink_output_is_rejected(self):
        self.output.symlink_to(self.questions)
        with self.assertRaises(self.module.ReportGenerationError):
            self.generate()

    def test_low_decimal_precision_does_not_change_cent_amounts(self):
        expected = self.generate()
        with localcontext() as context:
            context.prec = 2
            actual = self.generate()
        self.assertEqual(expected, actual)

    def test_fully_resolved_matching_and_corrected_splits_have_distinct_conclusions(self):
        for index, (application, disposition) in enumerate(((APPLICATION, "CORRECTED"),
                (APPLICATION.replace("| E-510 | 2 | 80.08 |", "| E-510 | 3 | 186.08 |")
                    .replace("| C-110 | 2 | 120.02 |", "| C-110 | 1 | 20.02 |"), "ACCEPTED"))):
            with self.subTest(disposition=disposition):
                (self.employer / "payroll-register.csv").write_text(PAYROLL.replace("30.03,0,3.90", "30.03,0,0.00"))
                (self.employer / "application.md").write_text(application)
                self.codes, self.review, self.questions = self.root / f"codes {index}", self.root / f"review {index}.json", self.root / f"questions {index}.md"
                self.prepare()
                result = self.generate(output=self.root / f"report {index}.md")
                self.assertEqual(result["employers"][0]["disposition"], disposition)

    def test_verified_zero_and_nonpayroll_payments_do_not_display_an_open_code(self):
        self.generate()
        self.assertNotRegex(self.output.read_text(), r"\| 0\.00 \| OPEN \| VERIFIED \|")
        self.assertIn("— no payroll allocation", self.output.read_text())

    def test_matching_dollars_with_conflicting_reported_headcount_are_not_accepted(self):
        (self.employer / "payroll-register.csv").write_text(PAYROLL.replace("30.03,0,3.90", "30.03,0,0.00"))
        (self.employer / "application.md").write_text(APPLICATION.replace("80.08", "186.08")
            .replace("120.02", "20.02").replace("| E-510 | 2 |", "| E-510 | 9 |"))
        self.codes, self.review, self.questions = self.root / "wrong count codes", self.root / "wrong count.json", self.root / "wrong count questions.md"
        self.prepare()
        result = self.generate()
        self.assertEqual(result["employers"][0]["disposition"], "PARTIALLY UNRESOLVED")
        self.assertIn("reported employee count", self.output.read_text())

    def test_unknown_employee_application_assignment_is_not_labeled_documented(self):
        (self.employer / "application.md").write_text(APPLICATION.replace("80.08", "186.08").replace("120.02", "20.02"))
        self.codes, self.review, self.questions = self.root / "unconfirmed codes", self.root / "unconfirmed.json", self.root / "unconfirmed questions.md"
        self.prepare()
        self.generate()
        self.assertIn("| UNCONFIRMED |", self.output.read_text())
        self.assertNotRegex(self.output.read_text(), r"\| UNCONFIRMED \| [^|]+ \| [^|]+ \| DOCUMENTED \|")

    def test_dependency_change_immediately_before_publication_is_detected(self):
        original_preflight = self.module._preflight
        def change_question(path, payload):
            original_preflight(path, payload)
            self.questions.write_bytes(self.questions.read_bytes() + b"\nChanged during publication.\n")
        with patch.object(self.module, "_preflight", side_effect=change_question):
            with self.assertRaisesRegex(self.module.ReportGenerationError, "changed before"):
                self.generate()
        self.assertFalse(self.output.exists())

    def test_unexpected_csv_and_incomplete_state_are_rejected(self):
        extra = self.codes / "unexpected.csv"
        extra.write_text("class_code,payroll_allocated,rationale_ref\n")
        with self.assertRaisesRegex(self.module.ReportGenerationError, "unexpected"):
            self.generate()
        extra.unlink()
        state = deepcopy(self.state)
        state["outputs"] = []
        self.review.write_text(json.dumps(state))
        with self.assertRaisesRegex(self.module.ReportGenerationError, "exactly one CSV"):
            self.generate()

    def test_cli_failure_reports_error_without_creating_output(self):
        self.questions.unlink()
        completed = subprocess.run([sys.executable, "-B", str(CLI), "--review-state", str(self.review),
            "--codes-dir", str(self.codes), "--questions", str(self.questions), "--output", str(self.output)], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 1)
        self.assertIn("ERROR:", completed.stderr)
        self.assertFalse(self.output.exists())

    def test_reusable_report_does_not_assign_an_unsupported_named_reviewer(self):
        self.interview.write_text(INTERVIEW.replace("Nadia Brennan", "Alex Example"))
        self.codes, self.review, self.questions = self.root / "other interview codes", self.root / "other.json", self.root / "other questions.md"
        self.prepare()
        self.generate()
        self.assertNotIn("Responsible policy reviewer: auditor (Nadia Brennan", self.output.read_text())

    def test_missing_dates_remain_unconfirmed(self):
        (self.employer / "business-description.md").write_text(
            BUSINESS.replace("Audit period January 1, 2025 to December 31, 2025.", "Dates not supplied."))
        self.codes, self.review, self.questions = self.root / "undated codes", self.root / "undated.json", self.root / "undated questions.md"
        self.prepare()
        self.generate()
        self.assertIn("unconfirmed audit dates", self.output.read_text())

    def test_cli_runs_with_supplied_paths_and_reports_invalid_arguments(self):
        completed = subprocess.run([sys.executable, "-B", str(CLI), "--review-state", str(self.review),
            "--codes-dir", str(self.codes), "--questions", str(self.questions), "--output", str(self.output)], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("SHA-256", completed.stdout)
        bad = subprocess.run([sys.executable, "-B", str(CLI), "--help"], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 0)
        self.assertIn("--questions", bad.stdout)


class RealAuditReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not CLI.is_file():
            return
        cls.module = importlib.import_module("audit_report")
        cls.review = REPO / "deliverables/classification-review.json"
        cls.codes = REPO / "deliverables/codes"
        cls.questions = REPO / "deliverables/audit-questions.md"
        cls.state = json.loads(cls.review.read_text())
        if not Path(cls.state["processing"]["guide"]).is_file():
            raise unittest.SkipTest("Auditor-supplied local snapshots are unavailable; synthetic tests remain portable")
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.output = Path(cls.temp.name) / "real report.md"
        cls.report = cls.module.generate_report(cls.review, codes_dir=cls.codes, questions=cls.questions, output=cls.output)
        cls.text = cls.output.read_text()

    def setUp(self):
        self.assertTrue(CLI.is_file(), "Reusable audit-report generator is missing")

    def test_all_csv_rows_and_application_deltas_are_in_employer_sections(self):
        self.assertEqual(len(self.report["employers"]), 6)
        for result, entry, output in zip(self.report["employers"], self.state["processing"]["employers"], self.state["outputs"]):
            self.assertEqual(result["employer"], entry["employer"])
            self.assertEqual(result["verified_total"], output["verified_total"])
            for row in output["rows"]:
                reported = next((r["payroll"] for r in entry["application"]["reported"] if r["class_code"] == row["class_code"]), "0.00")
                self.assertIn(f"| {row['class_code']} | {reported} | {row['payroll_allocated']} | {entry['application']['verified_differences'][row['class_code']]} | {row['rationale_ref']} |", self.text)

    def test_rendered_detail_matches_each_csv_row_and_payroll_part_in_its_own_section(self):
        sections = re.split(r'(?m)^## [^\n]+ \([^\n]+\)\n', self.text)[1:]
        self.assertEqual(len(sections), 6)
        for section, entry, output in zip(sections, self.state["processing"]["employers"], self.state["outputs"]):
            with Path(output["path"]).open(newline="") as stream:
                actual_rows = list(csv.DictReader(stream))
            for row in actual_rows:
                self.assertIn(row["class_code"], section)
                self.assertIn(row["payroll_allocated"], section)
                self.assertIn(row["rationale_ref"], section)
            for employee in entry["employee_payroll"]:
                for part in employee["parts"]:
                    self.assertIn("| " + " | ".join([part["part_id"], part.get("week_start", "audit period"),
                        part.get("week_end", "audit period"), part["wages"], part["class_code"] or "OPEN",
                        part["rationale_ref"] or "OPEN"]) + " |", section)
            for ref in entry["sources"]:
                self.assertIn(f"| {ref['id']} | {ref['source']} | {ref['locator']} | {ref['line_start']}-{ref['line_end']} |", section)

    def test_every_material_obligation_is_linked_to_existing_questions(self):
        self.assertEqual(self.report["uncovered"], {})
        self.assertEqual(self.report["coverage"], {"employers": 6, "employees": 45, "payroll_parts": 351,
            "adjustments": 15, "findings": 22, "proposals": 9, "questions": 78, "sources": 3354, "records": 3287})
        anchors = set(re.findall(r'<a id="([^"]+)"></a>', self.questions.read_text()))
        links = re.findall(r"audit-questions\.md#([^ )]+)", self.text)
        self.assertTrue(links)
        self.assertTrue(set(links) <= anchors)
        for entry in self.state["processing"]["employers"]:
            for finding in entry["questions"]:
                self.assertIn(finding["subject"], self.text)
                self.assertIn(finding["reason"].replace("|", "\\|"), self.text)

    def test_open_wage_omissions_are_provisional_not_verified_reductions(self):
        self.assertIn("provisional comparison", self.text)
        self.assertIn("not a verified payroll reduction", self.text)
        for amount in ("64212.48", "114293.80", "71250.45", "45945.65", "390.00"):
            self.assertIn(amount, self.text)

    def test_open_catering_conditional_proposals_reach_report_without_changing_csv(self):
        entry = next(e for e in self.state["processing"]["employers"] if e["employer"] == "larkspur-lane-bistro")
        self.assertEqual(entry["verified_by_code"], {"F-710": "226431.55"})
        self.assertEqual(entry["open_wages"], "114293.80")
        proposals = {p["subject"]: p["treatment"] for p in entry["proposals"]}
        self.assertEqual(set(proposals), {"LL-E07", "LL-E08", "LL-E09"})
        section = re.search(r"(?ms)^## Larkspur Lane Bistro .*?(?=^## Patuxent Electric)", self.text).group()
        for employee in entry["employee_payroll"]:
            if employee["employee_id"] not in proposals:
                continue
            proposal = proposals[employee["employee_id"]]
            self.assertEqual((proposal["class_code"], proposal["rationale_ref"], proposal["wages"]),
                             ("F-710", "CG-41", employee["register_wages"]))
            self.assertIn(f"**UNAPPROVED — {employee['employee_id']}**", section)
            self.assertTrue(all(part["status"] == "OPEN" for part in employee["parts"]))
            required = " ".join(proposal["required_confirmation"])
            self.assertTrue(all(term in required for term in ("2025-07-07", "2026-07-05", "below 40%", "timesheet", "auditor")))
            for confirmation in proposal["required_confirmation"]:
                self.assertIn(confirmation, section)
        self.assertEqual(self.report["uncovered"], {})

    def test_global_reconciliation_keeps_basis_and_known_payroll_distinct(self):
        self.assertIn("2521697.11 + 26853.39 = 2298793.77 + 249756.73", self.text)
        self.assertIn("2683038.16 = 2298793.77 + 249756.73 + 88152.01 + 46335.65", self.text)
        self.assertIn("Known payroll basis (includes OPEN wages)", self.text)
        self.assertIn("NOT EVALUATED", self.text)

    def test_names_identity_boundaries_owner_and_catering_uncertainty_survive(self):
        for detail in ("Tomas Reyes", "Marissa Gale", "County inspector", "2025-12-02", "Kent Island Roofing & Siding LLC",
                       "Kyle Brandt", "Raymond Dunmore", "Martin Severn", "Employee timesheets", "22.00%"):
            self.assertIn(detail, self.text)
        self.assertIn("UNAPPROVED PROPOSED treatments", self.text)
        self.assertIn("removed register wages $0.00", self.text)

    def test_every_individual_change_and_subcontractor_invoice_is_present(self):
        for name, amount in (("Luis Carrillo", "54880.40"), ("Brian Tull", "52115.75"), ("Owen Petrakis", "49607.30"),
            ("Rafael Duarte", "47918.65"), ("Jamal Whitfield", "46205.10"), ("Teresa Lindqvist", "68430.90"),
            ("Dana Whitcomb", "59840.70"), ("Raymond Dunmore", "118000.00"), ("Lena Ortiz", "22808.75")):
            self.assertIn(name, self.text)
            self.assertIn(amount, self.text)
        for entry in self.state["processing"]["employers"]:
            for line in entry["adjustments"]["lines"]:
                self.assertIn(line["adjustment_id"], self.text)
                self.assertIn(line["input_record"]["amount"], self.text)

    def test_recorded_priorities_keep_acknowledgement_and_evidence(self):
        self.assertEqual({p["employer"] for p in self.report["priorities"]}, {"severn-homebuilders", "bay-crest-exteriors"})
        self.assertIn("09:18 PM", self.text)
        self.assertIn("first-call group", self.text)

    def test_rule_boundaries_and_exact_interview_locators_are_preserved(self):
        self.assertIn("### Applied rule boundaries", self.text)
        for entry in self.state["processing"]["employers"]:
            for employee in entry["employee_payroll"]:
                for part in employee["parts"]:
                    decision = part["decision"]
                    if decision:
                        self.assertIn(decision["rule"], self.text)
                        self.assertIn(decision["scope"], self.text)
                        for boundary in decision["applicability"]:
                            self.assertIn(boundary.replace("|", "\\|"), self.text)

    def test_removing_report_detail_is_detected_as_uncovered(self):
        plan = self.module.load_report_plan(self.review, codes_dir=self.codes, questions=self.questions)
        employer = plan["employers"][0]
        employer["items"] = [item for item in employer["items"] if "employee:AC-E04" not in item["covers"]]
        gaps = self.module.report_coverage_gaps(plan)
        self.assertIn("employee:AC-E04", gaps["annapolis-courier"])
        with self.assertRaises(self.module.ReportGenerationError):
            self.module.render_report(plan)
