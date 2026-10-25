import argparse
import logging
from pathlib import Path

from . import report, store
from .importer import import_csv


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(prog="ledger", description="Pocket Ledger")
    sub = parser.add_subparsers(dest="command", required=True)
    imp = sub.add_parser("import", help="import a bank CSV")
    imp.add_argument("csv_file", type=Path)
    sub.add_parser("report", help="print spending by category")
    args = parser.parse_args(argv)
    conn = store.connect()
    if args.command == "import":
        items = import_csv(args.csv_file)
        store.add_many(conn, items)
        print(f"imported {len(items)} transactions")
    else:
        print(report.text_report(store.totals_by_category(conn)))
