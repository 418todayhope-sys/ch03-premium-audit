"""Fresh real-source dependency chains; never replace the published artifacts."""

from dataclasses import dataclass
import csv
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP
import os
from pathlib import Path
import re
import tempfile
import unittest

from audit_questions import generate_questions
from audit_report import generate_report
from generate_codes import generate_csvs


@dataclass(frozen=True)
class RealAuditChain:
    inputs: Path
    guide: Path
    interview: Path
    codes: Path
    review: Path
    questions: Path
    output: Path
    state: dict
    question_result: dict
    report: dict


def fresh_real_chain(register_cleanup):
    """Reread configurable sources and build every dependency in a new directory."""
    component = Path(__file__).resolve().parents[1]
    inputs = Path(os.environ.get("INSURANCE01_TEST_INPUTS", Path.home() / "insurance01-inputs")).expanduser().resolve()
    guide = inputs / "classification-guide.md"
    employers = inputs / "employer-files"
    interview = Path(os.environ.get("INSURANCE01_TEST_INTERVIEW",
        component.parents[1] / "interviews/ch03-premium-audit-20261105-0222(1).md")).expanduser().resolve()
    if not guide.is_file() or not employers.is_dir() or not interview.is_file():
        raise unittest.SkipTest("Auditor-supplied local sources are unavailable; synthetic tests remain portable")
    temporary = tempfile.TemporaryDirectory(prefix="independent real audit ")
    register_cleanup(temporary.cleanup)
    root = Path(temporary.name)
    codes, review = root / "codes", root / "classification-review.json"
    questions, output = root / "audit-questions.md", root / "audit-report.md"
    state = generate_csvs(guide, interview, all_employers=employers,
                         output_dir=codes, review_state=review)
    if state["errors"] or state["processing"]["errors"] or state["status"] == "ERROR":
        errors = [*state["errors"], *state["processing"]["errors"],
                  *(error for entry in state["processing"]["employers"] for error in entry["errors"])]
        raise AssertionError(f"Fresh real-source processing failed: {errors}")
    question_result = generate_questions(review, codes_dir=codes, output=questions)
    report = generate_report(review, codes_dir=codes, questions=questions, output=output)
    return RealAuditChain(inputs, guide, interview, codes, review, questions, output,
                         state, question_result, report)


def source_rows(path):
    """Read original CSV values independently of the production input reader."""
    with Path(path).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def source_period(directory):
    text = (directory / "business-description.md").read_text()
    match = re.search(r"Audit period ([A-Za-z]+ \d+, \d{4}) to ([A-Za-z]+ \d+, \d{4})\.", text)
    assert match, "Original fixture must document its audit period"
    return tuple(datetime.strptime(value, "%B %d, %Y").date() for value in match.groups())


def source_subcontractors(directory):
    """Independent arithmetic for the reviewed homebuilding source fixture.

    This is a test oracle, not an adapter for arbitrary new evidence. Roofing
    invoices here have differently named proof; they require identity review.
    Full-period exact-name coverage excludes payments; missing/expired proof
    adds 60%, per CG-06 and Nadia's confirmed full-period rule.
    """
    payments = source_rows(directory / "subcontractor-payments.csv")
    certificates = source_rows(directory / "insurance-certificates.csv")
    start, end = source_period(directory)
    totals = dict.fromkeys(("basis", "added", "nonpayroll", "open_basis"), Decimal("0.00"))
    by_code, open_invoices = {}, set()
    for payment in payments:
        amount = Decimal(payment["amount_paid"])
        totals["basis"] += amount
        exact = [c for c in certificates if c["subcontractor"] == payment["subcontractor"]]
        if any(date.fromisoformat(c["coverage_from"]) <= start and
               date.fromisoformat(c["coverage_to"]) >= end for c in exact):
            totals["nonpayroll"] += amount
        elif not exact and payment["work"] == "roofing":
            assert any("roof" in c["subcontractor"].casefold() for c in certificates), "Review the changed fixture's certificate evidence"
            totals["open_basis"] += amount
            open_invoices.add(payment["invoice"])
        else:
            addition = (amount * Decimal("0.60")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            code = {"framing": "H-420", "drywall": "H-420", "roofing": "R-310"}[payment["work"]]
            by_code[code] = by_code.get(code, Decimal("0.00")) + addition
            totals["added"] += addition
            totals["nonpayroll"] += amount - addition
    return totals, by_code, open_invoices


def source_controls(inputs):
    """Resum original registers/payments under the reviewed evidence boundaries.

    No generated decisions, CSVs, review JSON or report totals are read here.
    Legal site visits lack an established field rule; mixed catering duties
    lack complete audit-period receipts. Their original wages stay OPEN.
    Allowances above $47/documented day count; zero-day allowances stay OPEN.
    """
    portfolio = dict.fromkeys(("register", "added", "open_wages", "basis", "nonpayroll", "open_basis"), Decimal("0.00"))
    employers = {}
    for directory in sorted((inputs / "employer-files").iterdir()):
        if not directory.is_dir() or directory.name.startswith("."):
            continue
        payroll = source_rows(directory / "payroll-register.csv")
        values = dict.fromkeys(portfolio, Decimal("0.00"))
        values["register"] = sum((Decimal(r["wages_paid"]) for r in payroll), Decimal("0.00"))
        open_workers = source_open_workers(directory, payroll)
        values["open_wages"] = sum((Decimal(r["wages_paid"]) for r in payroll
                                    if r["employee_id"] in open_workers), Decimal("0.00"))
        if (directory / "subcontractor-payments.csv").is_file():
            subcontractors, _, _ = source_subcontractors(directory)
            for key, amount in subcontractors.items():
                values[key] += amount
        for row in payroll:
            if "travel_allowance_paid" not in row:
                continue
            allowance, days = Decimal(row["travel_allowance_paid"]), int(row["travel_days"])
            values["basis"] += allowance
            if days == 0 and allowance:
                values["open_basis"] += allowance
            else:
                excluded = min(allowance, Decimal("47") * days)
                values["nonpayroll"] += excluded
                values["added"] += allowance - excluded
        for key in portfolio:
            portfolio[key] += values[key]
        employers[directory.name] = values
    for values in [portfolio, *employers.values()]:
        values["verified"] = values["register"] - values["open_wages"] + values["added"]
        values["cash"] = values["register"] + values["basis"]
        values["known_payroll"] = values["register"] + values["added"]
    return portfolio, employers


def source_open_workers(directory, payroll):
    """Identify the reviewed fixture's unsupported duties from original records."""
    business = " ".join((directory / "business-description.md").read_text().split())
    if "law office" in business:
        visits = source_rows(directory / "site-signin-log.csv")
        return {r["employee_id"] for r in visits}
    if (directory / "gross-receipts.csv").is_file():
        receipts = source_rows(directory / "gross-receipts.csv")
        _, end = source_period(directory)
        assert end.strftime("%Y-%m") not in {r["month"] for r in receipts}, "Review newly complete catering evidence"
        return {r["employee_id"] for r in payroll if r["position"] in {"Catering Lead", "Event Cook", "Event Server"}}
    return set()
