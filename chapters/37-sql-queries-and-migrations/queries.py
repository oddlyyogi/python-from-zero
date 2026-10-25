import sqlite3

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
conn.execute(
    "CREATE TABLE tx (id INTEGER PRIMARY KEY, date TEXT, description TEXT, amount REAL, category TEXT)"
)
conn.executemany(
    "INSERT INTO tx (date, description, amount, category) VALUES (?, ?, ?, ?)",
    [
        ("2026-09-28", "Coffee", -4.5, "food"),
        ("2026-09-30", "Salary", 3200.0, "income"),
        ("2026-10-01", "Rent", -900.0, "housing"),
        ("2026-10-02", "Lunch", -12.0, "food"),
        ("2026-10-03", "Groceries", -62.3, "food"),
        ("2026-10-05", "Gym", -30.0, "health"),
        ("2026-10-07", "Salary", 3200.0, "income"),
        ("2026-10-09", "Pharmacy", -18.4, "health"),
        ("2026-10-12", "Coffee", -4.5, "food"),
    ],
)


def show(sql, *params):
    for row in conn.execute(sql, params):
        print(dict(row))
    print()

conn.execute("ALTER TABLE tx ADD COLUMN note TEXT")
show("SELECT id, description, note FROM tx LIMIT 2")
print(conn.execute("PRAGMA user_version").fetchone()[0])
