"""Question coverage against real engine results, CSVs and individual source rows."""

from copy import deepcopy
import hashlib
import importlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

from test_electrical_processing import APPLICATION, BUSINESS, GUIDE, INTERVIEW, NOTES, PAYROLL, SIGNINS
from employer_processing import process_employer
from generate_codes import generate_csvs
from input_reader import read_markdown
from real_audit_support import fresh_real_chain, source_rows

COMPONENT = Path(__file__).resolve().parents[1]
CLI = COMPONENT / "audit_questions.py"


class AuditQuestionTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(CLI.is_file(), "Reusable audit-question generator is missing")
        self.module = importlib.import_module("audit_questions")
        self.temp = tempfile.TemporaryDirectory(prefix="audit question sources ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.employer = self.root / "fresh-employer"
        self.employer.mkdir()
        self.guide = self.root / "current guide.md"
        self.interview = self.root / "original interview.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        for filename, text in {
            "business-description.md": BUSINESS, "field-notes.md": NOTES,
            "payroll-register.csv": PAYROLL, "application.md": APPLICATION,
            "site-signin-log.csv": SIGNINS,
        }.items():
            (self.employer / filename).write_text(text, encoding="utf-8")
        self.codes = self.root / "deliverables/codes"
        self.review = self.root / "deliverables/classification-review.json"
        self.output = self.root / "deliverables/audit-questions.md"
        self.state = generate_csvs(self.guide, self.interview, employer=self.employer,
                                  output_dir=self.codes, review_state=self.review)

    def plan(self):
        native = process_employer(self.guide, self.employer, self.interview)
        return self.module.build_question_plan(self.state,
            {str(self.employer): native}, read_markdown(self.guide), read_markdown(self.interview))

    def generate(self):
        return self.module.generate_questions(self.review, codes_dir=self.codes, output=self.output)

    def test_new_employer_questions_cover_every_part_adjustment_finding_and_source(self):
        plan = self.plan()
        questions = plan["employers"][0]["questions"]
        covered = set().union(*(set(q["covers"]) for q in questions))
        entry = self.state["processing"]["employers"][0]
        for employee in entry["employee_payroll"]:
            self.assertIn(f"employee:{employee['employee_id']}", covered)
            for part in employee["parts"]:
                self.assertIn(f"part:{part['part_id']}", covered)
        for line in entry["adjustments"]["lines"]:
            self.assertIn(f"adjustment:{line['adjustment_id']}", covered)
        for index, _ in enumerate(entry["questions"]):
            self.assertIn(f"finding:{index}", covered)
        for index, _ in enumerate(entry["proposals"]):
            self.assertIn(f"proposal:{index}", covered)
        for source in entry["sources"]:
            self.assertIn(f"source:{source['id']}", covered)
        self.assertEqual(self.module.coverage_gaps(plan), {})

    def test_zero_day_allowance_stays_separate_from_verified_wages_and_requires_approval(self):
        plan = self.plan()
        allowance = next(q for q in plan["employers"][0]["questions"]
                         if "adjustment:travel:A1" in q["covers"])
        text = self.module.render_questions(plan)
        self.assertEqual(allowance["status"], "OPEN / HUMAN APPROVAL REQUIRED")
        self.assertIn("Apprentice Person", allowance["subject"])
        self.assertIn("travel:A1", text)
        self.assertIn("3.90", text)
        self.assertIn("UNAPPROVED PROPOSAL", text)
        self.assertIn("already included", text)
        self.assertIn("Verified CSV payroll: $206.10", text)

    def test_record_index_keeps_employee_ids_date_source_lines_and_question_links(self):
        plan = self.plan()
        records = plan["employers"][0]["records"]
        self.assertTrue(records)
        signin = next(record for record in records if record["values"].get("site") == "Example Site")
        self.assertEqual(signin["values"]["employee_id"], "O1")
        self.assertEqual(signin["values"]["date"], "2025-02-03")
        self.assertTrue(signin["questions"])
        text = self.module.render_questions(plan)
        self.assertIn("site-signin-log.csv", text)
        self.assertIn("2025-02-03", text)
        self.assertIn(signin["id"], text)
        self.assertIn("O1", text)

    def test_removing_material_question_reports_specific_uncovered_obligations(self):
        plan = self.plan()
        employer = plan["employers"][0]
        employer["questions"] = [q for q in employer["questions"]
                                 if "adjustment:travel:A1" not in q["covers"]]
        gaps = self.module.coverage_gaps(plan)
        self.assertIn("adjustment:travel:A1", gaps["fresh-employer"])
        self.assertIn("proposal:0", gaps["fresh-employer"])

    def test_duplicate_question_obligations_are_grouped_without_losing_original_findings(self):
        state = deepcopy(self.state)
        findings = state["processing"]["employers"][0]["questions"]
        findings.append(deepcopy(findings[0]))
        native = process_employer(self.guide, self.employer, self.interview)
        plan = self.module.build_question_plan(state, {str(self.employer): native},
                    read_markdown(self.guide), read_markdown(self.interview))
        questions = plan["employers"][0]["questions"]
        affected = [q for q in questions if "finding:0" in q["covers"]]
        self.assertEqual(len(affected), 1)
        self.assertIn(f"finding:{len(findings)-1}", affected[0]["covers"])
        self.assertEqual(self.module.coverage_gaps(plan), {})

    def test_application_question_marks_open_findings_separately_from_verified_calculations(self):
        application = next(q for q in self.plan()["employers"][0]["questions"] if q["kind"] == "application")
        self.assertIn("VERIFIED", application["status"])
        self.assertIn("OPEN", application["status"])

    def test_confirmation_bullets_are_not_duplicated_as_a_concatenated_prompt(self):
        for question in self.plan()["employers"][0]["questions"]:
            for prompt in question["confirm"]:
                components = re.split(r"(?<=\.)\s*;\s+", prompt)
                self.assertFalse(len(components) > 1 and all(piece in question["confirm"] for piece in components),
                                 f"Duplicate combined prompt in {question['subject']}")

    def test_unacknowledged_priority_is_not_invented_for_a_new_employer(self):
        plan = self.plan()
        self.assertEqual(plan["priorities"], [])
        self.assertIn("No source-bound first-call choices", self.module.render_questions(plan))

    def test_acknowledged_priority_uses_current_employer_identity_and_source(self):
        self.interview.write_text(INTERVIEW + "\n**Nadia Brennan** · Voice · 09:18 PM\n\n"
            "I have noted your choices of Independent Electric, along with your reasoning regarding the records.\n",
            encoding="utf-8")
        # Match the state to the newly supplied interview, as a new CSV run would.
        changed_codes = self.root / "new codes"
        changed_review = self.root / "new review.json"
        state = generate_csvs(self.guide, self.interview, employer=self.employer,
                             output_dir=changed_codes, review_state=changed_review)
        native = process_employer(self.guide, self.employer, self.interview)
        plan = self.module.build_question_plan(state, {str(self.employer): native},
                    read_markdown(self.guide), read_markdown(self.interview))
        self.assertEqual([p["employer"] for p in plan["priorities"]], ["fresh-employer"])
        self.assertIn("09:18 PM", plan["priorities"][0]["source"]["locator"])

    def test_priority_names_cannot_match_a_different_company_by_prefix_or_suffix(self):
        for index, (title, acknowledged) in enumerate((("Independent", "Independent Electric"),
                                                       ("Independent Electric", "Independent Electric Services"),
                                                       ("Independent", "Independent and Sons"))):
            with self.subTest(title=title, acknowledged=acknowledged):
                (self.employer / "business-description.md").write_text(
                    BUSINESS.replace("# Independent Electric\n", f"# {title}\n"), encoding="utf-8")
                self.interview.write_text(INTERVIEW + "\n**Nadia Brennan** · Voice · 09:18 PM\n\n"
                    f"I have noted your choices of {acknowledged}, along with your reasoning regarding the records.\n", encoding="utf-8")
                state = generate_csvs(self.guide, self.interview, employer=self.employer,
                    output_dir=self.root / f"other codes {index}", review_state=self.root / f"other state {index}.json")
                native = process_employer(self.guide, self.employer, self.interview)
                plan = self.module.build_question_plan(state, {str(self.employer): native},
                    read_markdown(self.guide), read_markdown(self.interview))
                self.assertEqual(plan["priorities"], [])

    def test_generation_is_repeatable_and_preserves_inputs_csvs_and_review_state(self):
        protected = [self.guide, self.interview, self.review, *self.codes.glob("*.csv")]
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in protected}
        report = self.generate()
        content = self.output.read_bytes()
        self.assertEqual(report, self.generate())
        self.assertEqual(self.output.read_bytes(), content)
        self.assertEqual(before, {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in protected})
        self.assertEqual(report["uncovered"], {})
        self.assertFalse((self.output.parent / "audit-report.md").exists())

    def test_copied_csv_and_review_inputs_are_identified_by_their_supplied_locations(self):
        copied_review = self.root / "relocated review.json"
        copied_review.write_bytes(self.review.read_bytes())
        copied_codes = self.root / "relocated codes"
        copied_codes.mkdir()
        original = next(self.codes.glob("*.csv"))
        copied_csv = copied_codes / original.name
        copied_csv.write_bytes(original.read_bytes())
        self.module.generate_questions(copied_review, codes_dir=copied_codes, output=self.output)
        text = self.output.read_text()
        self.assertIn(f"Review-state input: {copied_review}", text)
        self.assertIn(f"CSV: {copied_csv}", text)

    def test_changed_original_source_or_review_state_blocks_publication(self):
        for mutation in ("source", "review"):
            with self.subTest(mutation=mutation):
                if mutation == "source":
                    self.guide.write_text(GUIDE + "\nChanged source edition.\n", encoding="utf-8")
                else:
                    self.guide.write_text(GUIDE, encoding="utf-8")
                    state = deepcopy(self.state)
                    state["processing"]["employers"][0]["open_adjustment_basis"] = "0.00"
                    self.review.write_text(json.dumps(state), encoding="utf-8")
                with self.assertRaises(self.module.QuestionGenerationError):
                    self.generate()
                self.assertFalse(self.output.exists())

    def test_missing_audit_period_generates_confirmation_questions_instead_of_invented_dates(self):
        (self.employer / "business-description.md").write_text(
            BUSINESS.replace("Audit period January 1, 2025 to December 31, 2025.", "Audit dates were not supplied."), encoding="utf-8")
        codes, review = self.root / "undated codes", self.root / "undated review.json"
        state = generate_csvs(self.guide, self.interview, employer=self.employer,
                             output_dir=codes, review_state=review)
        self.assertIsNone(state["processing"]["employers"][0]["audit_period"])
        report = self.module.generate_questions(review, codes_dir=codes, output=self.output)
        self.assertEqual(report["uncovered"], {})
        self.assertIn("Audit period", self.output.read_text())
        self.assertIn("unconfirmed audit dates", self.output.read_text())

    def test_missing_or_tampered_csv_blocks_document(self):
        csv = next(self.codes.glob("*.csv"))
        original = csv.read_bytes()
        for contents in (None, original.replace(b"186.08", b"186.09")):
            with self.subTest(contents=contents):
                if csv.exists():
                    csv.unlink()
                if contents is not None:
                    csv.write_bytes(contents)
                with self.assertRaises(self.module.QuestionGenerationError):
                    self.generate()
                self.assertFalse(self.output.exists())

    def test_output_cannot_replace_evidence_csv_state_or_differing_operator_work(self):
        self.output.write_text("Existing operator questions\n", encoding="utf-8")
        for output in (self.guide, self.review, next(self.codes.glob("*.csv")),
                       self.employer / "questions.md", self.output):
            with self.subTest(output=output), self.assertRaises(self.module.QuestionGenerationError):
                self.module.generate_questions(self.review, codes_dir=self.codes, output=output)
        self.assertEqual(self.output.read_text(), "Existing operator questions\n")

    def test_cli_uses_configurable_review_csv_and_output_paths(self):
        completed = subprocess.run([sys.executable, "-B", str(CLI), "--review-state", str(self.review),
            "--codes-dir", str(self.codes), "--output", str(self.output)], cwd=self.root,
            capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertTrue(self.output.exists())
        self.assertIn("Uncovered", completed.stdout)


class RealAuditQuestionCoverageTests(unittest.TestCase):
    def test_all_six_real_employers_and_named_exceptions_have_traceable_coverage(self):
        self.assertTrue(CLI.is_file(), "Reusable audit-question generator is missing")
        chain = fresh_real_chain(self.addCleanup)
        report, state = chain.question_result, chain.state
        text = chain.questions.read_text(encoding="utf-8")
        self.assertEqual(set(report["counts"]), {e["employer"] for e in state["processing"]["employers"]})
        self.assertEqual(report["uncovered"], {})
        self.assertEqual([p["employer"] for p in report["priorities"]],
                         ["severn-homebuilders", "bay-crest-exteriors"])
        for token in ("Tomas Reyes", "HP-E03", "Hannah Pryor", "Ivan Petrov", "Clara Bose",
                      "Marissa Gale", "SH-E06", "County inspector", "Kent Island Roofing",
                      "Kent Island Roofing & Siding LLC", "SV-KEN-01", "SV-KEN-02", "SV-KEN-03",
                      "Kyle Brandt", "travel:PE-E06", "Employee timesheets", "Lena Ortiz"):
            self.assertIn(token, text)
        self.assertIn("27567.39", text)
        self.assertIn("390.00", text)
        marissa = re.search(r"### E\d+-Q\d+ — Marissa Gale \[SH-E06\]\n(.*?)(?=\n### |\n<details>)", text, re.S)
        self.assertIsNotNone(marissa)
        for token in ("2025-12-02", "County inspector", "Lot 7 Mill Pond Rd", "C-110", "CG-04"):
            self.assertIn(token, marissa.group(1))
        original = source_rows(chain.inputs / "employer-files/severn-homebuilders/payroll-register.csv")
        estimator = next(r for r in original if r["position"] == "Estimator")
        self.assertIn("**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**", marissa.group(1))
        self.assertIn(f"| {estimator['employee_id']} | audit period | audit period | {estimator['wages_paid']} | C-110 | CG-04 |", marissa.group(1))
        self.assertNotIn("UNAPPROVED alternatives", marissa.group(1))
        self.assertIn("External site visitors", text)
        for entry in state["processing"]["employers"]:
            self.assertGreater(report["counts"][entry["employer"]], len(entry["employee_payroll"]))
            for employee in entry["employee_payroll"]:
                self.assertIn(employee["employee_id"], text)
                for part in employee["parts"]:
                    self.assertIn(part["part_id"], text)
                    if "week_start" in part:
                        self.assertIn(part["week_start"], text)
                        self.assertIn(part["week_end"], text)
            for source in entry["sources"]:
                self.assertIn(source["locator"], text)


if __name__ == "__main__":
    unittest.main()
