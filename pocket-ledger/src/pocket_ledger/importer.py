import csv
import logging
from decimal import InvalidOperation
from pathlib import Path

from .models import Transaction
from .money import to_money
from .rules import categorize

log = logging.getLogger(__name__)


def import_csv(path: Path | str) -> list[Transaction]:
    transactions: list[Transaction] = []
    with open(path, newline="", encoding="utf-8") as f:
        for number, row in enumerate(csv.DictReader(f), start=2):
            try:
                amount = to_money(row["Amount"])
            except InvalidOperation:
                log.warning("line %d: bad amount %r, skipped", number, row["Amount"])
                continue
            description = row["Description"].strip()
            transactions.append(
                Transaction(row["Date"], description, amount, categorize(description))
            )
    return transactions
