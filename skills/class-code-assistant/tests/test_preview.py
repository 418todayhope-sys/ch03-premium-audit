"""Exercise the preview command with fresh sources and isolated employers."""

import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from decimal import Decimal
from unittest.mock import patch

from test_electrical_processing import GUIDE, INTERVIEW, BUSINESS, NOTES, PAYROLL, APPLICATION, SIGNINS

COMPONENT = Path(__file__).resolve().parents[1]
CLI = COMPONENT / "preview.py"


class PreviewCommandTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(CLI.is_file(), "Unified preview command is not implemented")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.guide = self.root / "guide.md"
        self.interview = self.root / "interview.md"
        self.guide.write_text(GUIDE, encoding="utf-8")
        self.interview.write_text(INTERVIEW, encoding="utf-8")
        self.container = self.root / "companies"
        self.container.mkdir()
        self.employer = self.make_employer("one-business")

    def make_employer(self, name, payroll=PAYROLL):
        directory = self.container / name
        directory.mkdir()
        for filename, text in {"business-description.md": BUSINESS, "field-notes.md": NOTES,
            "payroll-register.csv": payroll, "application.md": APPLICATION, "site-signin-log.csv": SIGNINS}.items():
            (directory / filename).write_text(text, encoding="utf-8")
        return directory

    def command(self, *args, output="json"):
        return subprocess.run([sys.executable, "-B", str(CLI), "--guide", str(self.guide), "--interview", str(self.interview),
            "--format", output, *map(str, args)], cwd=self.root, capture_output=True, text=True, check=False)

    def single(self):
        completed = self.command("--employer", self.employer)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        return json.loads(completed.stdout)

    def test_single_employer_preserves_verified_open_and_proposed_amounts(self):
        report = self.single()
        self.assertTrue(report["preview_only"])
        self.assertEqual(report["status"], "REVIEW")
        self.assertEqual(len(report["employers"]), 1)
        employer = report["employers"][0]
        self.assertEqual(employer["verified_by_code"], {"E-510": "186.08", "C-110": "20.02"})
        self.assertEqual(employer["open_wages"], "0.00")
        self.assertEqual(employer["open_adjustment_basis"], "3.90")
        proposed = next(item for item in employer["proposals"] if item["kind"] == "adjustment")
        self.assertEqual(proposed["treatment"]["payroll_added"], "3.90")
        self.assertEqual(proposed["work_code"], "E-510")
        self.assertTrue(employer["reconciliation"]["independent"]["reconciled"])
        self.assertEqual(employer["reconciliation"]["travel"]["cash_total"], "304.00")
        self.assertEqual(employer["application"]["verified_differences"], {"C-110": "-100.00", "E-510": "106.00"})
        self.assertTrue(employer["questions"])

    def test_text_preview_clearly_labels_open_proposals_sources_and_reconciliation(self):
        completed = self.command("--employer", self.employer, output="text")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        for value in ("PREVIEW ONLY", "186.08", "OPEN wages", "OPEN adjustment basis", "UNAPPROVED", "3.90", "Reconciliation", "Reported differences", "CG-21", "SHA-256", str(self.guide)):
            self.assertIn(value, completed.stdout)

    def test_employee_preview_separates_wages_and_additions_in_verified_payroll(self):
        employer = self.single()["employers"][0]
        field = next(item for item in employer["employee_payroll"] if item["employee_id"] == "F1")
        self.assertEqual(field["verified_by_code"], {"E-510": "56.05"})
        self.assertEqual(field["verified_wages_by_code"], {"E-510": "50.05"})
        self.assertEqual(field["verified_adjustment_by_code"], {"E-510": "6.00"})
        self.assertEqual(field["register_wages"], "50.05")
        self.assertEqual(field["open_wages"], "0.00")

    def test_text_proposal_identifies_its_conditional_work_code(self):
        completed = self.command("--employer", self.employer, output="text")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("work code E-510", completed.stdout)

    def test_zero_net_open_wages_still_require_review_for_each_employee(self):
        (self.employer / "business-description.md").write_text(BUSINESS.replace("does residential and light commercial wiring", "assembles clocks"), encoding="utf-8")
        (self.employer / "payroll-register.csv").write_text("employee_id,name,position,wages_paid\nX1,First Person,Unknown,50.05\nX2,Second Person,Unknown,-50.05\n", encoding="utf-8")
        employer = self.single()["employers"][0]
        self.assertEqual(employer["open_wages"], "0.00")
        self.assertEqual(employer["status"], "REVIEW")
        self.assertTrue(all(item["parts"][0]["status"] == "OPEN" for item in employer["employee_payroll"]))
        self.assertEqual([item["open_wages"] for item in employer["employee_payroll"]], ["50.05", "-50.05"])

    def test_all_employers_are_sorted_and_never_merge_shared_employee_ids(self):
        self.make_employer("aaa-business", PAYROLL.replace("50.05,2,100.00", "75.05,2,100.00"))
        completed = self.command("--all-employers", self.container)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        employers = json.loads(completed.stdout)["employers"]
        self.assertEqual([item["employer"] for item in employers], ["aaa-business", "one-business"])
        self.assertEqual(employers[0]["verified_by_code"]["E-510"], "211.08")
        self.assertEqual(employers[1]["verified_by_code"]["E-510"], "186.08")
        self.assertNotEqual(employers[0]["directory"], employers[1]["directory"])

    def test_repeated_invocations_are_identical_until_supplied_sources_change(self):
        first = self.command("--employer", self.employer)
        self.assertEqual(first.stdout, self.command("--employer", self.employer).stdout)
        path = self.employer / "payroll-register.csv"
        path.write_text(PAYROLL.replace("50.05,2,100.00", "75.05,2,100.00"), encoding="utf-8")
        changed = self.single()["employers"][0]
        self.assertEqual(changed["verified_by_code"]["E-510"], "211.08")
        self.guide.write_text(GUIDE.replace("Installation and repair of electrical wiring", "UNVERIFIED CHANGED ELECTRICAL POLICY"), encoding="utf-8")
        self.assertGreater(Decimal(self.single()["employers"][0]["open_wages"]), 0)

    def test_newly_supplied_interview_is_reread_without_using_preserved_snapshots(self):
        self.interview.write_text(INTERVIEW.replace("forty-seven dollars", "unverified dollars"), encoding="utf-8")
        employer = self.single()["employers"][0]
        self.assertEqual(employer["verified_by_code"]["E-510"], "180.08")
        self.assertTrue(employer["questions"])

    def test_missing_shared_guide_or_interview_is_an_explicit_error(self):
        for path, contents in ((self.guide, GUIDE), (self.interview, INTERVIEW)):
            with self.subTest(path=path):
                path.unlink()
                completed = self.command("--employer", self.employer)
                self.assertEqual(completed.returncode, 1)
                report = json.loads(completed.stdout)
                self.assertEqual(report["status"], "ERROR")
                self.assertTrue(report["errors"])
                self.assertIn(str(path), completed.stderr)
                path.write_text(contents, encoding="utf-8")

    def test_missing_employer_or_empty_all_directory_never_reports_zero_payroll_success(self):
        for flag, path in (("--employer", self.root / "absent"), ("--all-employers", self.root / "empty")):
            with self.subTest(flag=flag):
                if flag == "--all-employers":
                    path.mkdir()
                completed = self.command(flag, path)
                self.assertEqual(completed.returncode, 1)
                self.assertEqual(json.loads(completed.stdout)["status"], "ERROR")

    def test_malformed_one_of_many_is_reported_without_losing_valid_employer(self):
        self.make_employer("broken", PAYROLL.replace("50.05", "not-money"))
        completed = self.command("--all-employers", self.container)
        self.assertEqual(completed.returncode, 1)
        report = json.loads(completed.stdout)
        by_name = {item["employer"]: item for item in report["employers"]}
        self.assertEqual(by_name["broken"]["status"], "ERROR")
        self.assertIsNone(by_name["broken"]["open_wages"])
        self.assertIsNone(by_name["broken"]["verified_by_code"])
        self.assertEqual(by_name["one-business"]["verified_by_code"]["E-510"], "186.08")
        self.assertIn("broken", completed.stderr)

    def test_directory_missing_base_files_is_included_as_an_error(self):
        (self.container / "incomplete").mkdir()
        completed = self.command("--all-employers", self.container)
        self.assertEqual(completed.returncode, 1)
        employers = json.loads(completed.stdout)["employers"]
        self.assertEqual(len(employers), 2)
        self.assertEqual(employers[0]["employer"], "incomplete")
        self.assertEqual(employers[0]["status"], "ERROR")

    def test_filename_overrides_apply_without_hard_coded_source_names(self):
        (self.employer / "payroll-register.csv").rename(self.employer / "wages.csv")
        completed = self.command("--employer", self.employer, "--file", "payroll=wages.csv")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        employer = json.loads(completed.stdout)["employers"][0]
        self.assertEqual(employer["verified_by_code"]["E-510"], "186.08")
        self.assertTrue(any(source["path"].endswith("wages.csv") for source in employer["source_manifest"]))

    def test_dot_relative_filename_override_reads_the_existing_source(self):
        completed = self.command("--employer", self.employer, "--file", "payroll=./payroll-register.csv")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        employer = json.loads(completed.stdout)["employers"][0]
        self.assertEqual(employer["verified_by_code"]["E-510"], "186.08")

    def test_usage_errors_for_ambiguous_modes_and_invalid_filename_overrides(self):
        cases = [("--employer", self.employer, "--all-employers", self.container),
            ("--employer", self.employer, "--file", "unknown=anything.csv"),
            ("--employer", self.employer, "--file", "payroll=../outside.csv")]
        for args in cases:
            with self.subTest(args=args):
                self.assertEqual(self.command(*args).returncode, 2)

    def test_discovery_reports_excluded_entries_and_duplicate_directory_aliases(self):
        (self.container / ".metadata").mkdir()
        (self.container / "notice.md").write_text("Container metadata", encoding="utf-8")
        completed = self.command("--all-employers", self.container)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(sorted(json.loads(completed.stdout)["discovery"]["excluded_entries"]), [".metadata", "notice.md"])
        (self.container / "zzz-alias").symlink_to(self.employer, target_is_directory=True)
        completed = self.command("--all-employers", self.container)
        self.assertEqual(completed.returncode, 1)
        employers = json.loads(completed.stdout)["employers"]
        self.assertEqual(employers[-1]["status"], "ERROR")
        self.assertIn("alias", str(employers[-1]["errors"]).lower())

    def test_preview_preserves_citations_and_never_writes_evidence_or_outputs(self):
        before = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in self.root.rglob("*") if path.is_file()}
        employer = self.single()["employers"][0]
        after = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(before, after)
        references = employer["sources"]
        self.assertEqual(len({ref["id"] for ref in references}), len(references))
        for ref in references:
            self.assertEqual(ref["sha256"], hashlib.sha256(Path(ref["source"]).read_bytes()).hexdigest())
            self.assertGreater(ref["line_start"], 0)
        self.assertTrue(any(ref["locator"] == "CG-21" for ref in references))
        self.assertTrue(any(ref["locator"] == "Nadia Brennan · 06:05 PM" for ref in references))

    def test_unexpected_employer_exception_is_isolated_and_has_nonzero_exit(self):
        other = self.make_employer("zzz-valid")
        spec = importlib.util.spec_from_file_location("insurance01_preview_test", CLI)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        real = module.process_employer
        def process(guide, employer, interview, **kwargs):
            if Path(employer).name == "one-business":
                raise RuntimeError("Synthetic isolated execution failure")
            return real(guide, employer, interview, **kwargs)
        output, errors = io.StringIO(), io.StringIO()
        with patch.object(module, "process_employer", side_effect=process), redirect_stdout(output), redirect_stderr(errors):
            status = module.main(["--guide", str(self.guide), "--interview", str(self.interview), "--all-employers", str(self.container), "--format", "json"])
        report = json.loads(output.getvalue())
        self.assertEqual(status, 1)
        self.assertEqual(report["employers"][0]["errors"][0]["type"], "RuntimeError")
        self.assertEqual(report["employers"][1]["directory"], str(other))
        self.assertEqual(report["employers"][1]["verified_by_code"]["E-510"], "186.08")


class LocalUnifiedPreviewTest(unittest.TestCase):
    def test_all_six_real_employers_retain_totals_and_open_bases(self):
        self.assertTrue(CLI.is_file(), "Unified preview command is not implemented")
        root = Path(os.environ.get("INSURANCE01_TEST_INPUTS", "/home/maxg/insurance01-inputs"))
        interview = COMPONENT.parents[1] / "interviews/ch03-premium-audit-20261105-0222(1).md"
        if not root.is_dir() or not interview.is_file():
            self.skipTest("Local development snapshots are unavailable")
        completed = subprocess.run([sys.executable, "-B", str(CLI), "--guide", str(root / "classification-guide.md"), "--interview", str(interview),
            "--all-employers", str(root / "employer-files"), "--format", "json"], capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        employers = {item["employer"]: item for item in json.loads(completed.stdout)["employers"]}
        self.assertEqual(len(employers), 6)
        expected = {
            "larkspur-lane-bistro": ({"F-710": "226431.55"}, "114293.80", None),
            "harbor-point-legal": ({"C-110": "360935.68"}, "64212.48", None),
            "bay-crest-exteriors": ({"C-110": "44812.35", "R-310": "450480.60", "R-320": "46205.10"}, "0.00", None),
            "severn-homebuilders": ({"C-110": "117368.70", "H-420": "369204.39"}, "0.00", "45945.65"),
            "annapolis-courier": ({"C-110": "107820.45", "T-610": "176694.95"}, "0.00", None),
            "patuxent-electric": ({"C-110": "43905.60", "E-510": "426184.85"}, "0.00", "390.00"),
        }
        for name, (codes, wages, adjustments) in expected.items():
            with self.subTest(employer=name):
                self.assertEqual(employers[name]["verified_by_code"], codes)
                self.assertEqual(employers[name]["open_wages"], wages)
                self.assertEqual(employers[name]["open_adjustment_basis"], adjustments)
                self.assertTrue(employers[name]["reconciliation"]["independent"]["reconciled"])


if __name__ == "__main__":
    unittest.main()
