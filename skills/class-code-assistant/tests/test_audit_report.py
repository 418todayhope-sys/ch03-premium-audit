"""Audit report contracts against synthetic inputs and the six preserved results."""

from copy import deepcopy
import csv
from decimal import Decimal, localcontext
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
from real_audit_support import (
    fresh_real_chain, source_controls, source_open_workers, source_rows, source_subcontractors,
)

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
        cls.chain = fresh_real_chain(cls.addClassCleanup)
        cls.review, cls.codes = cls.chain.review, cls.chain.codes
        cls.questions, cls.output = cls.chain.questions, cls.chain.output
        cls.state, cls.report = cls.chain.state, cls.chain.report
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
        plan = self.module.load_report_plan(self.review, codes_dir=self.codes, questions=self.questions)
        employee_count = part_count = adjustment_count = record_count = 0
        for employer in plan["employers"]:
            entry = employer["entry"]
            directory = Path(entry["directory"])
            payroll = source_rows(directory / "payroll-register.csv")
            employee_count += len(payroll)
            weekly = directory / "weekly-payroll.csv"
            part_count += len(source_rows(weekly)) if weekly.exists() else len(payroll)
            payments = directory / "subcontractor-payments.csv"
            adjustment_count += len(source_rows(payments)) if payments.exists() else 0
            adjustment_count += sum("travel_allowance_paid" in r for r in payroll)
            source_records = [(str(path), line) for path in directory.glob("*.csv")
                              for line in range(2, len(source_rows(path)) + 2)]
            record_count += len(source_records)
            self.assertEqual({(r["source"], r["line_start"]) for r in employer["records"]}, set(source_records))
            covered = set().union(*(item["covers"] for item in employer["items"]))
            self.assertTrue({f"employee:{r['employee_id']}" for r in payroll} <= covered)
            self.assertTrue({f"record:{r['id']}" for r in employer["records"]} <= covered)
            self.assertTrue({f"source:{r['id']}" for r in employer["sources"]} <= covered)
            self.assertTrue({f"finding:{i}" for i in range(len(entry["questions"]))} <= covered)
            self.assertTrue({f"proposal:{i}" for i in range(len(entry["proposals"]))} <= covered)
            self.assertTrue({f"control:{name}" for name, value in entry["reconciliation"].items() if value is not None} <= covered)
            self.assertTrue(all(item["confirm"] for item in employer["items"]))
        coverage = self.report["coverage"]
        self.assertEqual(coverage["employers"], len(plan["employers"]))
        self.assertEqual(coverage["employees"], employee_count)
        self.assertEqual(coverage["payroll_parts"], part_count)
        self.assertEqual(coverage["adjustments"], adjustment_count)
        self.assertEqual(coverage["records"], record_count)
        for metric, collection in (("findings", "questions"), ("proposals", "proposals"), ("sources", "sources")):
            self.assertEqual(coverage[metric], sum(len(e["entry"][collection]) for e in plan["employers"]))
        self.assertEqual(coverage["questions"], sum(len(e["items"]) for e in plan["employers"]))
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
        for entry in self.state["processing"]["employers"]:
            directory = Path(entry["directory"])
            payroll = source_rows(directory / "payroll-register.csv")
            expected_open = source_open_workers(directory, payroll)
            employees = {e["employee_id"]: e for e in entry["employee_payroll"]}
            law_office = "law office" in " ".join((directory / "business-description.md").read_text().split())
            for row in payroll:
                employee = employees[row["employee_id"]]
                is_open = row["employee_id"] in expected_open
                self.assertEqual(Decimal(employee["open_wages"]),
                                 Decimal(row["wages_paid"]) if is_open else Decimal("0.00"))
                self.assertEqual({p["status"] for p in employee["parts"]}, {"OPEN" if is_open else "ALLOCATED"})
                self.assertIn(row["wages_paid"], self.text)
                if is_open and law_office:
                    proposal, = [p["treatment"] for p in entry["proposals"] if p["subject"] == row["employee_id"]]
                    self.assertEqual((proposal["class_code"], proposal["rationale_ref"]), ("C-110", "CG-04"))
                    self.assertEqual(Decimal(proposal["wages"]), Decimal(row["wages_paid"]))
                    self.assertTrue(proposal["required_confirmation"])
                    self.assertIn(f"**UNAPPROVED — {row['employee_id']}**", self.text)
                if row.get("travel_days") == "0" and Decimal(row.get("travel_allowance_paid", "0")):
                    line = next(line for line in entry["adjustments"]["lines"]
                                if line["adjustment_id"] == f"travel:{row['employee_id']}")
                    self.assertEqual(line["status"], "OPEN")
                    self.assertEqual(Decimal(line["payroll_added"]), Decimal("0.00"))
                    self.assertEqual(Decimal(line["proposal"]["payroll_added"]), Decimal(row["travel_allowance_paid"]))

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
        expected, employers = source_controls(self.chain.inputs)
        employee_equation = "{register:.2f} + {added:.2f} = {verified:.2f} + {open_wages:.2f}".format(**expected)
        cash_equation = "{cash:.2f} = {verified:.2f} + {open_wages:.2f} + {nonpayroll:.2f} + {open_basis:.2f}".format(**expected)
        self.assertTrue(employee_equation in self.text, employee_equation)
        self.assertTrue(cash_equation in self.text, cash_equation)
        for entry, result in zip(self.state["processing"]["employers"], self.report["employers"]):
            original = employers[entry["employer"]]
            self.assertEqual(Decimal(result["verified_total"]), original["verified"])
            self.assertEqual(Decimal(result["open_wages"]), original["open_wages"])
            self.assertEqual(Decimal(entry["reconciliation"]["independent"]["register_total"]), original["register"])
            for check in entry["reconciliation"].values():
                if check is not None:
                    self.assertTrue(check["reconciled"])
                    self.assertEqual(Decimal(check["difference"]), Decimal("0.00"))
        self.assertIn("Known payroll basis (includes OPEN wages)", self.text)
        self.assertIn("NOT EVALUATED", self.text)

    def test_severn_codes_and_review_obligations_follow_original_records(self):
        directory, = [p for p in (self.chain.inputs / "employer-files").iterdir()
                      if (p / "subcontractor-payments.csv").is_file()]
        payroll = source_rows(directory / "payroll-register.csv")
        visits = source_rows(directory / "site-signin-log.csv")
        employees = {r["employee_id"]: r for r in payroll}
        external = [r for r in visits if r["employee_id"] not in employees]
        self.assertTrue(external)
        self.assertTrue(all(not r["employee_id"] and r["name"] == "County inspector" for r in external))
        field_roles = {"Lead Carpenter", "Carpenter", "Laborer"}
        field_wages = sum(Decimal(r["wages_paid"]) for r in payroll if r["position"] in field_roles)
        payments = source_rows(directory / "subcontractor-payments.csv")
        competing = sum(Decimal(p["amount_paid"]) for p in payments if p["work"] == "roofing")
        self.assertGreater(field_wages, competing, "CG-15 own-crew wages establish H-420 without circular office wages")
        expected_codes, employee_codes = {}, {}
        for row in payroll:
            days = {r["date"] for r in visits if r["employee_id"] == row["employee_id"] and r["name"] == row["name"]}
            if row["position"] in field_roles:
                code = "H-420"
            else:
                self.assertIn(row["position"], {"Estimator", "Office Manager", "Bookkeeper"})
                code = "C-110" if len(days) <= 4 else "H-420"
            employee_codes[row["employee_id"]] = code
            expected_codes[code] = expected_codes.get(code, Decimal("0.00")) + Decimal(row["wages_paid"])
        sub, additions, open_invoices = source_subcontractors(directory)
        for code, amount in additions.items():
            expected_codes[code] = expected_codes.get(code, Decimal("0.00")) + amount
        entry = next(e for e in self.state["processing"]["employers"] if Path(e["directory"]) == directory)
        self.assertEqual({code: Decimal(amount) for code, amount in entry["verified_by_code"].items()}, expected_codes)
        guide_codes = dict((code, paragraph) for paragraph, code in re.findall(
            r"(?m)^\*\*(CG-\d+)\. ([A-Z]-\d+)\b", self.chain.guide.read_text()))
        actual_rows = source_rows(self.codes / f"{directory.name}.csv")
        self.assertEqual(actual_rows, [{"class_code": code, "payroll_allocated": f"{amount:.2f}",
                                      "rationale_ref": guide_codes[code]} for code, amount in sorted(expected_codes.items())])
        for employee in entry["employee_payroll"]:
            original = employees[employee["employee_id"]]
            self.assertEqual(employee["verified_wages_by_code"],
                             {employee_codes[original["employee_id"]]: original["wages_paid"]})
            self.assertEqual(Decimal(employee["open_wages"]), Decimal("0.00"))
        lines = entry["adjustments"]["lines"]
        self.assertEqual({line["adjustment_id"] for line in lines if line["status"] == "OPEN"}, open_invoices)
        proposals = {p["subject"]: p for p in entry["proposals"]}
        findings = {q["subject"]: q for q in entry["questions"]}
        self.assertEqual(set(proposals), open_invoices)
        self.assertTrue(open_invoices <= set(findings))
        refs = {ref["id"]: ref for ref in entry["sources"]}
        certificates = source_rows(directory / "insurance-certificates.csv")
        certificate, = [c for c in certificates if "roof" in c["subcontractor"].casefold()]
        question_blocks = re.split(r"(?m)(?=^### )", self.questions.read_text())
        for line in lines:
            if line["adjustment_id"] in open_invoices:
                invoice = line["adjustment_id"]
                payment = next(p for p in payments if p["invoice"] == invoice)
                self.assertEqual(Decimal(line["payroll_added"]), Decimal("0.00"))
                self.assertEqual(Decimal(line["proposal"]["payroll_added"]), Decimal(payment["amount_paid"]) * Decimal("0.60"))
                self.assertEqual(Decimal(proposals[invoice]["treatment"]["payroll_added"]),
                                 Decimal(payment["amount_paid"]) * Decimal("0.60"))
                for obligation, citation_field in ((findings[invoice], "sources"),
                                                   (proposals[invoice], "evidence_sources")):
                    self.assertTrue(obligation["required_confirmation"])
                    self.assertIn("identity", str(obligation["required_confirmation"]).lower())
                    evidence = [refs[key] for key in obligation[citation_field]]
                    self.assertTrue(any(ref["source"] == str(directory / "subcontractor-payments.csv")
                                        and ref["line_start"] == payments.index(payment) + 2 for ref in evidence))
                    self.assertTrue(any(ref["source"] == str(directory / "insurance-certificates.csv")
                                        and ref["line_start"] == certificates.index(certificate) + 2 for ref in evidence))
                block, = [b for b in question_blocks if b.startswith("### ")
                          and payment["subcontractor"] in b.splitlines()[0]]
                for detail in (invoice, payment["subcontractor"], certificate["subcontractor"],
                               "subcontractor-payments.csv", "insurance-certificates.csv",
                               "OPEN / HUMAN APPROVAL REQUIRED", "UNAPPROVED PROPOSAL"):
                    self.assertTrue(detail in block, f"Missing {detail} in {invoice}'s confirmation question")
                self.assertIn(f"**OPEN — {invoice}**", self.text)
                self.assertIn(f"**UNAPPROVED — {invoice}**", self.text)
        self.assertEqual(Decimal(entry["open_adjustment_basis"]), sub["open_basis"])
        self.assertEqual(Decimal(entry["reconciliation"]["combined"]["confirmed_payroll"]),
                         sum(Decimal(r["wages_paid"]) for r in payroll) + sub["added"])
        external_finding, = [q for q in entry["questions"] if q["subject"] == "External site visitors"]
        self.assertTrue(external_finding["required_confirmation"])
        self.assertTrue(any(Path(refs[key]["source"]).name == "site-signin-log.csv" for key in external_finding["sources"]))
        estimator = next(r for r in payroll if r["position"] == "Estimator")
        self.assertNotIn(estimator["employee_id"], {p["subject"] for p in entry["proposals"]})
        decision = next(e for e in entry["employee_payroll"] if e["employee_id"] == estimator["employee_id"])["parts"][0]["decision"]
        self.assertEqual((decision["class_code"], decision["rationale_ref"]), ("C-110", "CG-04"))
        self.assertTrue(any(refs[key]["source"] == str(self.chain.interview) for key in decision["rule_sources"]))
        result = next(e for e in self.report["employers"] if e["employer"] == directory.name)
        self.assertEqual(result["disposition"], "PARTIALLY UNRESOLVED")

    def test_five_other_employer_results_and_csvs_match_the_preserved_baseline(self):
        baseline = json.loads((REPO / "deliverables/classification-review.json").read_text())
        previous = {e["employer"]: e for e in baseline["processing"]["employers"]}
        old_root = str(Path(baseline["processing"]["guide"]).parent)
        old_interview = baseline["processing"]["interview"]
        def normalized(entry, root, interview):
            return json.dumps(entry, sort_keys=True).replace(root, "INPUTS").replace(interview, "INTERVIEW")
        compared = []
        for entry in self.state["processing"]["employers"]:
            if (Path(entry["directory"]) / "subcontractor-payments.csv").exists():
                continue
            with self.subTest(employer=entry["employer"]):
                self.assertEqual(normalized(entry, str(self.chain.inputs), str(self.chain.interview)),
                                 normalized(previous[entry["employer"]], old_root, old_interview))
                filename = f"{entry['employer']}.csv"
                self.assertEqual((self.codes / filename).read_bytes(), (REPO / "deliverables/codes" / filename).read_bytes())
                compared.append(entry["employer"])
        self.assertEqual(len(compared), 5)

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
