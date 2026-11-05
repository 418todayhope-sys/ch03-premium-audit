"""Validate the packaged Skill and execute its documented preview commands."""

import hashlib
import json
from pathlib import Path
import re
import shlex
from string import Template
import subprocess
import sys
import tempfile
import unittest

from test_electrical_processing import (
    APPLICATION, BUSINESS, GUIDE, INTERVIEW, NOTES, PAYROLL, SIGNINS,
)

COMPONENT = Path(__file__).resolve().parents[1]
SKILL = COMPONENT / "SKILL.md"


class SkillPackageTests(unittest.TestCase):
    def skill_text(self):
        self.assertTrue(SKILL.is_file(), "The reusable SKILL.md is missing")
        return SKILL.read_text(encoding="utf-8")

    def test_metadata_has_valid_name_and_nonempty_description(self):
        text = self.skill_text()
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(match, "Skill requires YAML frontmatter")
        # This package uses two plain, single-line YAML scalars; no YAML runtime
        # dependency is needed to check that deliberately small metadata contract.
        entries = {}
        for line in match.group(1).splitlines():
            field = re.fullmatch(r"(name|description): ([^\n]+)", line)
            self.assertIsNotNone(field, f"Invalid plain metadata entry: {line!r}")
            key, value = field.groups()
            self.assertNotIn(key, entries, "Duplicate metadata field")
            self.assertNotRegex(value, r"[:#\[\]{}<>]|\A[-?&*!|>'\"%@`]")
            entries[key] = value
        self.assertEqual(set(entries), {"name", "description"})
        self.assertEqual(entries["name"], COMPONENT.name)
        self.assertRegex(entries["name"], r"\A[a-z0-9]+(?:-[a-z0-9]+)*\Z")
        self.assertLessEqual(len(entries["name"]), 64)
        self.assertTrue(entries["description"].strip())
        self.assertLessEqual(len(entries["description"]), 1024)

    def test_local_references_resolve_to_existing_supporting_files(self):
        references = re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", self.skill_text())
        self.assertTrue(references, "Skill must link to its supporting files")
        targets = set()
        for reference in references:
            self.assertNotIn("://", reference, "Package references should be local")
            path = (COMPONENT / reference.split("#", 1)[0]).resolve()
            self.assertTrue(path.is_relative_to(COMPONENT))
            self.assertTrue(path.is_file(), f"Broken Skill reference: {reference}")
            targets.add(path.name)
        self.assertTrue({"preview.py", "input_reader.py", "rule_evaluator.py",
                         "payroll_allocation.py", "payroll_adjustments.py",
                         "employer_processing.py"}.issubset(targets))

    def prepare_sources(self):
        temp = tempfile.TemporaryDirectory(prefix="skill inputs ")
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        guide, interview = root / "current guide.md", root / "complete interview.md"
        guide.write_text(GUIDE, encoding="utf-8")
        interview.write_text(INTERVIEW, encoding="utf-8")
        container = root / "new employer folders"
        container.mkdir()
        employer = container / "previously unseen business"
        employer.mkdir()
        for filename, contents in {
            "business-description.md": BUSINESS, "field-notes.md": NOTES,
            "payroll-register.csv": PAYROLL, "application.md": APPLICATION,
            "site-signin-log.csv": SIGNINS,
        }.items():
            (employer / filename).write_text(contents, encoding="utf-8")
        return {
            "AUDIT_GUIDE_PATH": str(guide), "AUDIT_INTERVIEW_PATH": str(interview),
            "AUDIT_EMPLOYER_DIR": str(employer),
            "AUDIT_EMPLOYERS_ROOT": str(container),
        }

    def documented_command(self, mode, locations):
        blocks = re.findall(r"```bash\n(.*?)\n```", self.skill_text(), re.DOTALL)
        candidates = []
        for block in blocks:
            words = shlex.split(block.replace("\\\n", ""))
            if mode in words:
                candidates.append(words)
        self.assertEqual(len(candidates), 1, f"Need one complete {mode} example")
        words = candidates[0]
        self.assertEqual(words[:3], ["python3", "-B", "preview.py"])
        expanded = [Template(word).substitute(locations) for word in words]
        return [sys.executable, *expanded[1:]]

    def run_documented(self, mode, locations, *, structured=True):
        command = self.documented_command(mode, locations)
        if structured:
            command += ["--format", "json"]
        return subprocess.run(command, cwd=COMPONENT, capture_output=True,
                              text=True, check=False)

    def test_documented_single_command_keeps_open_money_out_of_verified_totals(self):
        locations = self.prepare_sources()
        completed = self.run_documented("--employer", locations)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        report = json.loads(completed.stdout)
        self.assertTrue(report["preview_only"])
        employer = report["employers"][0]
        self.assertEqual(employer["verified_by_code"],
                         {"E-510": "186.08", "C-110": "20.02"})
        self.assertEqual(employer["open_adjustment_basis"], "3.90")
        proposal = next(p for p in employer["proposals"] if p["kind"] == "adjustment")
        self.assertEqual(proposal["treatment"]["payroll_added"], "3.90")
        self.assertEqual(employer["status"], "REVIEW")
        self.assertTrue(employer["reconciliation"]["independent"]["reconciled"])
        self.assertTrue(employer["sources"])

    def test_documented_all_command_preserves_valid_employer_after_neighbor_error(self):
        locations = self.prepare_sources()
        broken = Path(locations["AUDIT_EMPLOYERS_ROOT"]) / "incomplete neighbor"
        broken.mkdir()
        completed = self.run_documented("--all-employers", locations)
        self.assertEqual(completed.returncode, 1)
        employers = json.loads(completed.stdout)["employers"]
        self.assertEqual(len(employers), 2)
        by_name = {item["employer"]: item for item in employers}
        self.assertEqual(by_name[broken.name]["status"], "ERROR")
        self.assertEqual(by_name["previously unseen business"]["verified_by_code"]["E-510"], "186.08")

    def test_documented_command_rereads_changed_authoritative_payroll(self):
        locations = self.prepare_sources()
        first = self.run_documented("--employer", locations)
        self.assertEqual(first.returncode, 0, first.stderr)
        payroll = Path(locations["AUDIT_EMPLOYER_DIR"]) / "payroll-register.csv"
        payroll.write_text(PAYROLL.replace("50.05,2,100.00", "75.05,2,100.00"),
                           encoding="utf-8")
        second = self.run_documented("--employer", locations)
        self.assertEqual(second.returncode, 0, second.stderr)
        changed = json.loads(second.stdout)["employers"][0]
        self.assertEqual(changed["verified_by_code"]["E-510"], "211.08")
        self.assertNotEqual(first.stdout, second.stdout)

    def test_documented_command_missing_guide_reports_error_without_snapshot_fallback(self):
        locations = self.prepare_sources()
        locations["AUDIT_GUIDE_PATH"] = str(Path(locations["AUDIT_GUIDE_PATH"]).with_name("missing.md"))
        completed = self.run_documented("--employer", locations)
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(json.loads(completed.stdout)["status"], "ERROR")
        self.assertIn(locations["AUDIT_GUIDE_PATH"], completed.stderr)

    def test_documented_text_preview_preserves_inputs_and_creates_no_deliverables(self):
        locations = self.prepare_sources()
        root = Path(locations["AUDIT_GUIDE_PATH"]).parent

        def hashes():
            return {p.relative_to(root): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in root.rglob("*") if p.is_file()}

        before = hashes()
        for mode in ("--employer", "--all-employers"):
            completed = self.run_documented(mode, locations, structured=False)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            for label in ("PREVIEW ONLY", "OPEN", "UNAPPROVED", "SHA-256"):
                self.assertIn(label, completed.stdout)
        self.assertEqual(hashes(), before)


if __name__ == "__main__":
    unittest.main()
