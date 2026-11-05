"""Verified-only CSVs, exact guide references and durable unresolved evidence."""

from copy import deepcopy
from decimal import localcontext
import hashlib
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from test_electrical_processing import (
    APPLICATION, BUSINESS, GUIDE, INTERVIEW, NOTES, PAYROLL, SIGNINS,
)
import test_homebuilding_processing as homes
from employer_processing import EmployerFiles
from input_reader import read_markdown
from preview import run_preview

COMPONENT = Path(__file__).resolve().parents[1]
CLI = COMPONENT / "generate_codes.py"


class ClassificationCSVTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(CLI.is_file(), "Reusable CSV generator is missing")
        self.generator = importlib.import_module("generate_codes")
        self.temp = tempfile.TemporaryDirectory(prefix="csv sources ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.guide = self.root / "current guide.md"
        self.interview = self.root / "original interview.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        self.container = self.root / "employer files"
        self.container.mkdir()
        self.employer = self.make_employer("New Electric Company")
        self.output = self.root / "deliverables" / "codes"
        self.review = self.output.parent / "classification-review.json"

    def make_employer(self, name, payroll=PAYROLL):
        directory = self.container / name
        directory.mkdir()
        for filename, text in {
            "business-description.md": BUSINESS, "field-notes.md": NOTES,
            "payroll-register.csv": payroll, "application.md": APPLICATION,
            "site-signin-log.csv": SIGNINS,
        }.items():
            (directory / filename).write_text(text, encoding="utf-8")
        return directory

    def generate(self, *, all_employers=False, **kwargs):
        selected = {"all_employers": self.container} if all_employers else {"employer": self.employer}
        return self.generator.generate_csvs(self.guide, self.interview,
            output_dir=self.output, review_state=self.review, **selected, **kwargs)

    def entry(self):
        return run_preview(self.guide, self.interview, employer=self.employer)["employers"][0]

    def test_csv_has_exact_header_two_decimal_payroll_and_code_paragraphs(self):
        report = self.generate()
        self.assertEqual(report["status"], "REVIEW")
        path = self.output / "new-electric-company.csv"
        self.assertEqual(path.read_bytes(),
            b"class_code,payroll_allocated,rationale_ref\nC-110,20.02,CG-04\nE-510,186.08,CG-21\n")
        self.assertEqual(report["outputs"][0]["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertEqual(report["outputs"][0]["verified_total"], "206.10")

    def test_review_state_preserves_open_proposals_controls_and_evidence(self):
        report = self.generate()
        persisted = json.loads(self.review.read_text(encoding="utf-8"))
        self.assertEqual(persisted, report)
        entry = persisted["processing"]["employers"][0]
        self.assertEqual(entry["open_wages"], "0.00")
        self.assertEqual(entry["open_adjustment_basis"], "3.90")
        proposal = next(p for p in entry["proposals"] if p["kind"] == "adjustment")
        self.assertEqual(proposal["treatment"]["payroll_added"], "3.90")
        self.assertTrue(entry["reconciliation"]["travel"]["reconciled"])
        self.assertEqual(entry["reconciliation"]["travel"]["cash_total"], "304.00")
        self.assertTrue(entry["questions"])
        self.assertTrue(entry["sources"])
        self.assertFalse((self.review.parent / "audit-report.md").exists())
        self.assertFalse((self.review.parent / "audit-questions.md").exists())

    def test_zero_class_is_omitted(self):
        (self.employer / "payroll-register.csv").write_text(
            PAYROLL.replace("20.02,0,0.00", "0.00,0,0.00"), encoding="utf-8")
        self.generate()
        self.assertEqual((self.output / "new-electric-company.csv").read_text(),
            "class_code,payroll_allocated,rationale_ref\nE-510,186.08,CG-21\n")

    def test_unknown_industry_retains_all_wages_open_and_exports_header_only(self):
        (self.employer / "business-description.md").write_text(
            BUSINESS.replace("does residential and light commercial wiring", "assembles clocks"), encoding="utf-8")
        report = self.generate()
        self.assertEqual(report["status"], "REVIEW")
        self.assertEqual((self.output / "new-electric-company.csv").read_text(),
                         "class_code,payroll_allocated,rationale_ref\n")
        self.assertEqual(report["processing"]["employers"][0]["open_wages"], "200.10")

    def test_missing_guide_is_explicit_error_without_csv_or_fallback(self):
        self.guide.unlink()
        report = self.generate()
        self.assertEqual(report["status"], "ERROR")
        self.assertFalse(list(self.output.glob("*.csv")))
        self.assertTrue(json.loads(self.review.read_text())["processing"]["errors"])

    def test_missing_notes_blocks_only_affected_employer(self):
        other = self.make_employer("Other-New-Employer")
        (other / "field-notes.md").unlink()
        report = self.generate(all_employers=True)
        self.assertEqual(report["status"], "ERROR")
        self.assertEqual([p.name for p in self.output.glob("*.csv")], ["new-electric-company.csv"])
        self.assertTrue(any(error["employer"] == other.name for error in report["errors"]))
        self.assertEqual(len(report["processing"]["employers"]), 2)

    def test_missing_class_definition_leaves_payroll_open_without_invented_csv_reference(self):
        self.guide.write_text(GUIDE.replace("**CG-21. E-510 Electrical wiring.**",
                                           "**CG-99. Changed definition.**"), encoding="utf-8")
        report = self.generate()
        self.assertEqual((self.output / "new-electric-company.csv").read_text(),
                         "class_code,payroll_allocated,rationale_ref\nC-110,20.02,CG-04\n")
        self.assertEqual(report["processing"]["employers"][0]["open_wages"], "180.08")
        self.assertEqual(report["status"], "REVIEW")

    def test_source_change_after_engine_read_blocks_export_and_is_preserved_as_error(self):
        actual_run = self.generator.run_preview

        def change_source_after_processing(*args, **kwargs):
            result = actual_run(*args, **kwargs)
            (self.employer / "field-notes.md").write_text(NOTES + "Additional unreviewed observation.\n", encoding="utf-8")
            return result

        with patch.object(self.generator, "run_preview", side_effect=change_source_after_processing):
            report = self.generate()
        self.assertEqual(report["status"], "ERROR")
        self.assertFalse(list(self.output.glob("*.csv")))
        self.assertIn("changed", str(report["errors"]).lower())
        self.assertEqual(json.loads(self.review.read_text()), report)

    def test_new_employer_changed_payroll_and_filename_override_are_read_fresh(self):
        path = self.employer / "payroll-register.csv"
        path.write_text(PAYROLL.replace("50.05,2,100.00", "75.05,2,100.00"), encoding="utf-8")
        path.rename(self.employer / "new wages.csv")
        report = self.generate(files=EmployerFiles(payroll="new wages.csv"))
        self.assertEqual(report["outputs"][0]["verified_total"], "231.10")
        self.assertIn("E-510,211.08,CG-21", (self.output / "new-electric-company.csv").read_text())

    def test_low_decimal_precision_cannot_round_cents(self):
        with localcontext() as context:
            context.prec = 2
            report = self.generate()
        self.assertEqual(report["outputs"][0]["verified_total"], "206.10")

    def test_unsupported_line_reference_blocks_entire_employer_csv(self):
        entry = self.entry()
        entry["employee_payroll"][0]["parts"][0]["rationale_ref"] = "CG-02"
        with self.assertRaisesRegex(self.generator.CSVGenerationError, "reference|paragraph"):
            self.generator.build_rows(entry, read_markdown(self.guide))

    def test_ambiguous_code_definition_is_not_replaced_with_a_guessed_reference(self):
        entry = self.entry()
        self.guide.write_text(GUIDE + "\n**CG-99. E-510 Alternate electrical definition.** Changed.\n", encoding="utf-8")
        with self.assertRaisesRegex(self.generator.CSVGenerationError, "ambiguous|unique|changed"):
            self.generator.build_rows(entry, read_markdown(self.guide))

    def test_failed_reconciliation_or_mismatched_engine_totals_block_export(self):
        original = self.entry()
        for mutation in ("control", "total", "part"):
            with self.subTest(mutation=mutation):
                entry = deepcopy(original)
                if mutation == "control":
                    entry["reconciliation"]["independent"]["reconciled"] = False
                elif mutation == "total":
                    entry["verified_by_code"]["E-510"] = "186.09"
                else:
                    entry["employee_payroll"][0]["parts"][0]["wages"] = "100.01"
                with self.assertRaises(self.generator.CSVGenerationError):
                    self.generator.build_rows(entry, read_markdown(self.guide))

    def test_duplicate_payroll_parts_cannot_double_count(self):
        entry = self.entry()
        employee = entry["employee_payroll"][0]
        employee["parts"].append(deepcopy(employee["parts"][0]))
        with self.assertRaisesRegex(self.generator.CSVGenerationError, "duplicate"):
            self.generator.build_rows(entry, read_markdown(self.guide))

    def test_duplicate_adjustments_cannot_double_count_additions(self):
        entry = self.entry()
        line = next(line for line in entry["adjustments"]["lines"] if line["payroll_added"] == "6.00")
        entry["adjustments"]["lines"].append(deepcopy(line))
        with self.assertRaisesRegex(self.generator.CSVGenerationError, "duplicate"):
            self.generator.build_rows(entry, read_markdown(self.guide))

    def test_csv_validator_detects_wrong_amount_reference_precision_and_header(self):
        entry, guide = self.entry(), read_markdown(self.guide)
        valid = "class_code,payroll_allocated,rationale_ref\nC-110,20.02,CG-04\nE-510,186.08,CG-21\n"
        self.generator.validate_csv(valid, entry, guide)
        for corrupted in (valid.replace("186.08", "186.09"), valid.replace("CG-21", "CG-03"),
                          valid.replace("20.02", "20.020"), valid.replace("rationale_ref", "reason")):
            with self.subTest(corrupted=corrupted), self.assertRaises(self.generator.CSVGenerationError):
                self.generator.validate_csv(corrupted, entry, guide)

    def test_filename_slug_collision_reports_both_without_overwriting(self):
        self.make_employer("New-Electric-Company")
        report = self.generate(all_employers=True)
        self.assertEqual(report["status"], "ERROR")
        self.assertEqual(report["outputs"], [])
        self.assertFalse(list(self.output.glob("*.csv")))
        self.assertIn("collision", str(report["errors"]).lower())

    def test_repeated_run_is_identical_and_differing_existing_csv_is_preserved(self):
        first = self.generate()
        self.assertEqual(first, self.generate())
        path = self.output / "new-electric-company.csv"
        path.write_bytes(b"existing operator work\n")
        with self.assertRaisesRegex(self.generator.CSVGenerationError, "existing|overwrite"):
            self.generate()
        self.assertEqual(path.read_bytes(), b"existing operator work\n")

    def test_output_inside_sources_or_review_colliding_with_csv_is_rejected(self):
        for output, review in ((self.employer / "outputs", self.root / "review.json"),
                               (self.output, self.output / "new-electric-company.csv"),
                               (self.output, self.guide)):
            with self.subTest(output=output, review=review):
                with self.assertRaises(self.generator.CSVGenerationError):
                    self.generator.generate_csvs(self.guide, self.interview, employer=self.employer,
                        output_dir=output, review_state=review)
        self.assertEqual(self.guide.read_text(), GUIDE)

    def test_aliased_employer_outside_container_still_protects_actual_source_directory(self):
        outside = self.root / "outside authoritative records"
        self.employer.rename(outside)
        self.employer.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(self.generator.CSVGenerationError):
            self.generator.generate_csvs(self.guide, self.interview, all_employers=self.container,
                output_dir=outside / "generated", review_state=self.review)
        self.assertFalse((outside / "generated").exists())
        self.assertFalse(self.review.exists())

    def test_review_file_and_csv_directory_ancestor_collisions_fail_before_writes(self):
        for review in (self.output, self.output.parent,
                       self.output / "new-electric-company.csv" / "review.json"):
            with self.subTest(review=review):
                with self.assertRaises(self.generator.CSVGenerationError):
                    self.generator.generate_csvs(self.guide, self.interview, employer=self.employer,
                        output_dir=self.output, review_state=review)
                self.assertFalse(self.output.exists(), "Path conflicts must be rejected before publication")

    def test_review_state_symlink_is_refused_without_writing_its_target(self):
        target = self.root / "another operators state.json"
        self.review.parent.mkdir(parents=True)
        self.review.symlink_to(target)
        with self.assertRaises(self.generator.CSVGenerationError):
            self.generate()
        self.assertFalse(target.exists())

    def test_subcontractor_verified_additions_and_mismatched_certificate_stay_separate(self):
        self.interview.write_text(homes.INTERVIEW, encoding="utf-8")
        for filename, text in {
            "business-description.md": homes.BUSINESS, "field-notes.md": homes.NOTES,
            "payroll-register.csv": homes.PAYROLL, "application.md": homes.APPLICATION,
            "subcontractor-payments.csv": homes.PAYMENTS,
            "insurance-certificates.csv": homes.CERTIFICATES,
            "site-signin-log.csv": homes.SITE_HEADER + "".join(
                f"2025-02-{day:02d},E1,Estimator One,Site A,09:00\n" for day in range(1, 4))
                + "".join(f"2025-03-{day:02d},M1,Manager One,Site A,10:00\n" for day in range(1, 6))
                + "2025-04-15,,County inspector,Site A,11:00\n",
        }.items():
            (self.employer / filename).write_text(text, encoding="utf-8")
        report = self.generate()
        self.assertEqual((self.output / "new-electric-company.csv").read_text(),
            "class_code,payroll_allocated,rationale_ref\nC-110,90.00,CG-04\nH-420,172.03,CG-15\n")
        entry = report["processing"]["employers"][0]
        self.assertEqual(entry["open_adjustment_basis"], "30.00")
        self.assertTrue(entry["reconciliation"]["combined"]["reconciled"])
        self.assertEqual(entry["reconciliation"]["combined"]["subcontractor_added"], "12.03")

    def test_cli_creates_csv_and_review_state_from_configurable_paths(self):
        completed = subprocess.run([sys.executable, "-B", str(CLI), "--guide", str(self.guide),
            "--interview", str(self.interview), "--employer", str(self.employer),
            "--output-dir", str(self.output), "--review-state", str(self.review)],
            cwd=self.root, capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("206.10", completed.stdout)
        self.assertIn("3.90", completed.stdout)
        self.assertIn("REVIEW", completed.stdout)
        self.assertTrue(self.review.is_file())


if __name__ == "__main__":
    unittest.main()
