import sqlite3
from decimal import Decimal
from pathlib import Path

from .models import Transaction
from .money import to_money

DEFAULT_DB = Path("ledger.db")


def connect(path: Path = DEFAULT_DB) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS tx "
        "(id INTEGER PRIMARY KEY, date TEXT, description TEXT, amount TEXT, category TEXT)"
    )
    return conn


def add_many(conn: sqlite3.Connection, items: list[Transaction]) -> None:
    with conn:
        conn.executemany(
            "INSERT INTO tx (date, description, amount, category) VALUES (?, ?, ?, ?)",
            [(t.date, t.description, str(t.amount), t.category) for t in items],
        )


def totals_by_category(conn: sqlite3.Connection) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}
    for category, amount in conn.execute("SELECT category, amount FROM tx"):
        totals[category] = totals.get(category, Decimal(0)) + to_money(amount)
    return totals
