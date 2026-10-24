import sqlite3

DB = "ledger.db"


def connect():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with connect() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS transactions ("
            "id INTEGER PRIMARY KEY, date TEXT, description TEXT, amount REAL)"
        )


def add(date, description, amount):
    with connect() as conn:
        conn.execute(
            "INSERT INTO transactions (date, description, amount) VALUES (?, ?, ?)",
            (date, description, amount),
        )


def all_rows():
    with connect() as conn:
        return [dict(r) for r in conn.execute("SELECT * FROM transactions ORDER BY date")]


init_db()
add("2026-10-01", "Coffee", -4.5)
add("2026-10-02", "Rent", -900.0)
add("2026-10-03", "O'Brien's Pub", -32.0)
for row in all_rows():
    print(row)

