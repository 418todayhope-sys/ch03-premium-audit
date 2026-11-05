"""Read configurable local Markdown/CSV evidence without classifying payroll."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from decimal import Decimal
import csv
import io
import json
import os
from pathlib import Path
import re
import sys
from typing import Iterable


# These are column names, not employer names or classification rules.
DEFAULT_MONEY_COLUMNS = frozenset({
    "wages_paid", "gross_pay", "travel_allowance_paid", "amount_paid",
    "dine_in_receipts", "offsite_catering_receipts",
})
_MONEY = re.compile(r"[+-]?[0-9]+(?:\.[0-9]{1,2})?")
_PARAGRAPH = re.compile(r"(?m)^[ \t]*(?:#{1,6}[ \t]+)?(?:\*\*)?(CG-[0-9]+)\.")


class InputError(ValueError):
    """A source cannot be read or does not meet the documented input format."""


@dataclass(frozen=True)
class MarkdownSource:
    path: Path
    text: str
    paragraph_ids: tuple[str, ...]


@dataclass(frozen=True)
class CSVRow:
    line_number: int
    values: dict[str, str | Decimal]


@dataclass(frozen=True)
class CSVSource:
    path: Path
    text: str
    columns: tuple[str, ...]
    rows: tuple[CSVRow, ...]


@dataclass(frozen=True)
class Inputs:
    guide: MarkdownSource
    records_root: Path
    records: tuple[MarkdownSource | CSVSource, ...]


def _read_text(path: Path) -> str:
    try:
        # Preserve line endings and any BOM in source text for later citation.
        with path.open(encoding="utf-8", newline="") as source:
            return source.read()
    except UnicodeError as exc:
        raise InputError(f"{path}: expected UTF-8 text: {exc}") from exc
    except OSError as exc:
        raise InputError(f"{path}: cannot read source: {exc.strerror or exc}") from exc


def read_markdown(path: str | Path) -> MarkdownSource:
    """Preserve Markdown text and paragraph-definition identifiers in source order."""
    path = Path(path)
    text = _read_text(path)
    identifiers = tuple(_PARAGRAPH.findall(text.removeprefix("\ufeff")))
    return MarkdownSource(path, text, identifiers)


def _csv_lines(text: str, path: Path) -> Iterable[str]:
    """Check quote placement that csv.reader(strict=True) otherwise accepts."""
    state = "start"
    for line_number, line in enumerate(io.StringIO(text.removeprefix("\ufeff"), newline=""), 1):
        for character in line:
            if state == "quoted":
                if character == '"':
                    state = "closed"
            elif state == "closed":
                if character == '"':  # Doubled quote within a quoted field.
                    state = "quoted"
                elif character in ",\r\n":
                    state = "start"
                else:
                    raise InputError(f"{path}:{line_number}: malformed CSV: character after closing quote")
            elif character == '"':
                if state != "start":
                    raise InputError(f"{path}:{line_number}: malformed CSV: quote inside unquoted field")
                state = "quoted"
            elif character in ",\r\n":
                state = "start"
            else:
                state = "bare"
        yield line


def read_csv(
    path: str | Path, *, money_columns: Iterable[str] = DEFAULT_MONEY_COLUMNS,
) -> CSVSource:
    """Read a strict CSV table, converting configured money columns to Decimal."""
    path = Path(path)
    text = _read_text(path)
    money_columns = frozenset(money_columns)
    parser = csv.reader(_csv_lines(text, path), strict=True)
    rows = []
    try:
        header = next(parser, None)
        if not header:
            raise InputError(f"{path}:1: CSV header is missing")
        if any(not name or name != name.strip() for name in header):
            raise InputError(f"{path}:1: CSV headers must be nonblank without surrounding whitespace")
        if len(set(header)) != len(header):
            raise InputError(f"{path}:1: duplicate CSV header")
        while True:
            line_number = parser.line_num + 1
            row = next(parser, None)
            if row is None:
                break
            if not row:  # Blank physical lines do not create evidence rows.
                continue
            if len(row) != len(header):
                raise InputError(f"{path}:{line_number}: expected {len(header)} fields, got {len(row)}")
            values: dict[str, str | Decimal] = dict(zip(header, row))
            for column, value in zip(header, row):
                if column in money_columns:
                    if not _MONEY.fullmatch(value.strip()):
                        raise InputError(
                            f"{path}:{line_number}: invalid money in column {column!r}: {value!r}; "
                            "expected plain decimal dollars with at most two fractional digits"
                        )
                    values[column] = Decimal(value.strip())
            rows.append(CSVRow(line_number, values))
    except csv.Error as exc:
        raise InputError(f"{path}:{parser.line_num}: malformed CSV: {exc}") from exc
    return CSVSource(path, text, tuple(header), tuple(rows))


def read_inputs(
    guide_path: str | Path,
    employer_records_path: str | Path,
    *,
    money_columns: Iterable[str] = DEFAULT_MONEY_COLUMNS,
) -> Inputs:
    """Reread a guide and all Markdown/CSV records below a caller-supplied directory.

    The directory can hold one employer or any number of employer subdirectories.
    No employer names, minimum employer count, or classification answers are assumed.
    """
    guide = read_markdown(guide_path)
    if not guide.paragraph_ids:
        raise InputError(f"{guide.path}: no classification paragraph identifiers (CG-...) found")
    root = Path(employer_records_path)
    try:
        is_directory = root.is_dir()
    except OSError as exc:
        raise InputError(f"{root}: cannot access employer records directory: {exc.strerror or exc}") from exc
    if not is_directory:
        raise InputError(f"{root}: employer records directory is missing or is not a directory")

    def walk_error(exc: OSError) -> None:
        raise InputError(f"{exc.filename}: cannot list employer records: {exc.strerror}") from exc

    paths = sorted(
        Path(directory) / name
        for directory, _, names in os.walk(root, onerror=walk_error)
        for name in names
        if Path(name).suffix.lower() in {".md", ".csv"}
    )
    if not paths:
        raise InputError(f"{root}: no Markdown or CSV employer records found")
    money_columns = frozenset(money_columns)
    records = tuple(
        read_csv(path, money_columns=money_columns)
        if path.suffix.lower() == ".csv" else read_markdown(path)
        for path in paths
    )
    return Inputs(guide, root, records)


def inventory(inputs: Inputs) -> dict:
    """Summarize the input inventory without calculating payroll totals or allocations."""
    tables = [doc for doc in inputs.records if isinstance(doc, CSVSource)]
    return {
        "guide": {"path": str(inputs.guide.path), "paragraph_ids": inputs.guide.paragraph_ids},
        "records_root": str(inputs.records_root),
        "record_files": len(inputs.records),
        "markdown_files": len(inputs.records) - len(tables),
        "csv_files": len(tables),
        "csv_rows": sum(len(table.rows) for table in tables),
        "decimal_values": sum(
            isinstance(value, Decimal)
            for table in tables for row in table.rows for value in row.values.values()
        ),
        "records_by_directory": dict(sorted(Counter(
            doc.path.parent.relative_to(inputs.records_root).as_posix()
            for doc in inputs.records
        ).items())),
        "sources": [doc.path.relative_to(inputs.records_root).as_posix() for doc in inputs.records],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guide", required=True, type=Path, help="Classification Guide Markdown path")
    parser.add_argument("--employers", required=True, type=Path, help="Directory of employer Markdown/CSV records")
    parser.add_argument("--money-column", action="append", default=[], help="Additional CSV money column; repeat as needed")
    args = parser.parse_args(argv)
    try:
        inputs = read_inputs(
            args.guide, args.employers,
            money_columns=DEFAULT_MONEY_COLUMNS.union(args.money_column),
        )
    except InputError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(inventory(inputs), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
