"""Input contract tests using temporary, synthetic source documents only."""

import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from decimal import Decimal


COMPONENT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPONENT))


class InputReaderTests(unittest.TestCase):
    def setUp(self):
        # Report an unimplemented component as an assertion during the first red run.
        self.assertTrue((COMPONENT / "input_reader.py").is_file(), "Input reader is not implemented")
        self.reader = importlib.import_module("input_reader")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.guide = self.write("guide.md", "# Guide\r\n\r\n**CG-88. Test wording.** See CG-03.\r\n\r\n**CG-03. Other wording.**\r\n")
        self.records = self.root / "records"
        self.records.mkdir()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))
        return path

    def test_arbitrary_sources_retain_names_text_ids_and_decimal_cents(self):
        notes = "# Synthetic employer\r\nDuties need review.\r\n"
        self.write("records/new-company/notes.md", notes)
        self.write("records/new-company/pay.csv", "name,wages_paid\r\nAda,0.10\r\nBo,0.20\r\n")
        bundle = self.reader.read_inputs(self.guide, self.records)
        self.assertEqual(bundle.guide.paragraph_ids, ("CG-88", "CG-03"))
        self.assertEqual(bundle.guide.text, self.guide.read_bytes().decode("utf-8"))
        self.assertEqual([doc.path.relative_to(bundle.records_root).as_posix() for doc in bundle.records], ["new-company/notes.md", "new-company/pay.csv"])
        self.assertEqual(bundle.records[0].text, notes)
        payroll = bundle.records[1]
        self.assertEqual(payroll.columns, ("name", "wages_paid"))
        self.assertEqual(payroll.rows[0].line_number, 2)
        amounts = [row.values["wages_paid"] for row in payroll.rows]
        self.assertTrue(all(isinstance(value, Decimal) for value in amounts))
        self.assertEqual(amounts, [Decimal("0.10"), Decimal("0.20")])
        self.assertEqual(sum(amounts), Decimal("0.30"))

    def test_large_signed_money_and_zero_remain_exact(self):
        path = self.write("money.csv", "wages_paid\n9007199254740993.01\n-1.25\n0\n")
        result = self.reader.read_csv(path)
        self.assertEqual([row.values["wages_paid"] for row in result.rows], [Decimal("9007199254740993.01"), Decimal("-1.25"), Decimal("0")])

    def test_money_columns_are_configurable_and_other_fields_stay_strings(self):
        self.write("records/different-company/source.csv", "worker,total_compensation,hours\n007,12.34,8.0\n")
        bundle = self.reader.read_inputs(self.guide, self.records, money_columns={"total_compensation"})
        self.assertEqual(bundle.records[0].rows[0].values, {"worker": "007", "total_compensation": Decimal("12.34"), "hours": "8.0"})

    def test_invalid_money_reports_source_line_column_and_value(self):
        for value in ["", "NaN", "sNaN", "Infinity", "-Infinity", "1e3", "$10.00", "1,000.00", "1.001", "not-money"]:
            with self.subTest(value=value):
                escaped = value.replace('"', '""')
                path = self.write("invalid.csv", 'name,wages_paid\nAda,"' + escaped + '"\n')
                with self.assertRaises(self.reader.InputError) as caught:
                    self.reader.read_csv(path)
                message = str(caught.exception)
                self.assertIn(str(path), message)
                self.assertIn(":2:", message)
                self.assertIn("wages_paid", message)
                self.assertIn(repr(value), message)

    def test_csv_missing_or_extra_fields_are_rejected(self):
        for row in ["Ada", "Ada,10.00,extra"]:
            with self.subTest(row=row):
                path = self.write("width.csv", "name,wages_paid\n" + row + "\n")
                with self.assertRaisesRegex(self.reader.InputError, r"width.csv:2:.*fields"):
                    self.reader.read_csv(path)

    def test_csv_duplicate_blank_or_whitespace_headers_are_rejected(self):
        for header in ["name,name", "name,", "name, ", "name, wages_paid"]:
            with self.subTest(header=header):
                path = self.write("headers.csv", header + "\nAda,10.00\n")
                with self.assertRaisesRegex(self.reader.InputError, "header"):
                    self.reader.read_csv(path)

    def test_empty_csv_and_unterminated_quotes_are_rejected(self):
        for text in ["", 'name,wages_paid\n"Ada,10.00\n', 'name,wages_paid\n"Ada"junk,10.00\n']:
            with self.subTest(text=text):
                path = self.write("broken.csv", text)
                with self.assertRaisesRegex(self.reader.InputError, "broken.csv"):
                    self.reader.read_csv(path)

    def test_unescaped_quotes_in_unquoted_fields_or_headers_are_rejected(self):
        for text, line in [('name,wages_paid\nAd"a,10.00\n', 2), ('na"me,wages_paid\nAda,10.00\n', 1)]:
            with self.subTest(text=text):
                path = self.write("bare-quote.csv", text)
                with self.assertRaises(self.reader.InputError) as caught:
                    self.reader.read_csv(path)
                self.assertIn(f"{path}:{line}:", str(caught.exception))
                self.assertIn("quote", str(caught.exception))

    def test_escaped_quotes_inside_quoted_fields_are_preserved(self):
        path = self.write("escaped.csv", 'name,wages_paid\n"Ad""a",10.00\n')
        row = self.reader.read_csv(path).rows[0]
        self.assertEqual(row.values, {"name": 'Ad"a', "wages_paid": Decimal("10.00")})

    def test_bom_quoted_commas_and_multiline_rows_preserve_provenance(self):
        path = self.write("quoted.csv", '\ufeffname,wages_paid\r\n"Ada, A\r\nTeam",10.25\r\nBo,1.00\r\n')
        source = self.reader.read_csv(path)
        self.assertEqual(source.text, path.read_bytes().decode("utf-8"))
        self.assertEqual(source.rows[0].values, {"name": "Ada, A\r\nTeam", "wages_paid": Decimal("10.25")})
        self.assertEqual([row.line_number for row in source.rows], [2, 4])

    def test_header_only_supporting_csv_is_valid(self):
        path = self.write("empty-log.csv", "date,person\n")
        self.assertEqual(self.reader.read_csv(path).rows, ())

    def test_missing_guide_reports_its_path(self):
        missing = self.root / "missing-guide.md"
        with self.assertRaises(self.reader.InputError) as caught:
            self.reader.read_inputs(missing, self.records)
        self.assertIn(str(missing), str(caught.exception))

    def test_missing_employer_root_and_wrong_path_type_are_rejected(self):
        for path in [self.root / "missing-records", self.guide]:
            with self.subTest(path=path):
                with self.assertRaises(self.reader.InputError) as caught:
                    self.reader.read_inputs(self.guide, path)
                self.assertIn(str(path), str(caught.exception))

    @unittest.skipUnless(os.name == "posix" and os.geteuid() != 0, "Requires POSIX permissions and a non-root user")
    def test_inaccessible_parent_directory_has_contextual_error_without_traceback(self):
        self.write("restricted/records/notes.md", "# Notes\n")
        restricted = self.root / "restricted"
        records = restricted / "records"
        restricted.chmod(0)
        try:
            with self.assertRaises(self.reader.InputError) as caught:
                self.reader.read_inputs(self.guide, records)
            self.assertIn(str(records), str(caught.exception))
            result = subprocess.run([sys.executable, "-B", str(COMPONENT / "input_reader.py"), "--guide", str(self.guide), "--employers", str(records)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")
            self.assertIn(str(records), result.stderr)
            self.assertNotIn("Traceback", result.stderr)
        finally:
            restricted.chmod(0o700)

    def test_empty_records_and_unidentified_guide_are_rejected(self):
        with self.assertRaisesRegex(self.reader.InputError, "Markdown or CSV"):
            self.reader.read_inputs(self.guide, self.records)
        self.write("records/notes.md", "# Notes\n")
        for text in ["", "# Guide without paragraph identifiers\n"]:
            with self.subTest(text=text):
                self.guide.write_text(text, encoding="utf-8")
                with self.assertRaisesRegex(self.reader.InputError, "paragraph"):
                    self.reader.read_inputs(self.guide, self.records)

    def test_invalid_utf8_reports_source_path(self):
        path = self.root / "records" / "broken.md"
        path.write_bytes(b"\xff")
        with self.assertRaises(self.reader.InputError) as caught:
            self.reader.read_inputs(self.guide, self.records)
        self.assertIn(str(path), str(caught.exception))
        self.assertIn("UTF-8", str(caught.exception))

    def test_new_invocations_reread_sources_and_do_not_modify_them(self):
        payroll = self.write("records/other-company/pay.csv", "wages_paid\n1.00\n")
        first = self.reader.read_inputs(self.guide, self.records)
        payroll.write_bytes(b"wages_paid\n2.00\n")
        self.guide.write_bytes(b"**CG-99. Updated.**\n")
        before = {path: path.read_bytes() for path in [self.guide, payroll]}
        second = self.reader.read_inputs(self.guide, self.records)
        self.assertEqual(first.records[0].rows[0].values["wages_paid"], Decimal("1.00"))
        self.assertEqual(second.records[0].rows[0].values["wages_paid"], Decimal("2.00"))
        self.assertEqual(second.guide.paragraph_ids, ("CG-99",))
        self.assertEqual({path: path.read_bytes() for path in before}, before)

    def test_cli_prints_inventory_for_configured_sources(self):
        self.write("records/unlisted-company/notes.md", "# Notes\n")
        self.write("records/unlisted-company/pay.csv", "total_compensation\n12.34\n")
        result = subprocess.run([sys.executable, "-B", str(COMPONENT / "input_reader.py"), "--guide", str(self.guide), "--employers", str(self.records), "--money-column", "total_compensation"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = json.loads(result.stdout)
        self.assertEqual(summary["record_files"], 2)
        self.assertEqual(summary["csv_files"], 1)
        self.assertEqual(summary["markdown_files"], 1)
        self.assertEqual(summary["csv_rows"], 1)
        self.assertEqual(summary["decimal_values"], 1)
        self.assertEqual(summary["records_by_directory"], {"unlisted-company": 2})
        self.assertEqual(summary["guide"]["paragraph_ids"], ["CG-88", "CG-03"])
        self.assertEqual(summary["sources"], ["unlisted-company/notes.md", "unlisted-company/pay.csv"])

    def test_cli_invalid_input_exits_nonzero_with_context_and_no_traceback(self):
        self.write("records/pay.csv", "wages_paid\nNaN\n")
        result = subprocess.run([sys.executable, "-B", str(COMPONENT / "input_reader.py"), "--guide", str(self.guide), "--employers", str(self.records)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("pay.csv:2:", result.stderr)
        self.assertIn("wages_paid", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
