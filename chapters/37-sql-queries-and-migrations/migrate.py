import sqlite3

STEPS = [
    "CREATE TABLE tx (id INTEGER PRIMARY KEY, date TEXT, description TEXT, amount REAL)",
    "ALTER TABLE tx ADD COLUMN note TEXT",
]


def migrate(conn):
    version = conn.execute("PRAGMA user_version").fetchone()[0]
    for number, sql in enumerate(STEPS, start=1):
        if number > version:
            conn.execute(sql)
            conn.execute(f"PRAGMA user_version = {number}")
    conn.commit()
    return conn.execute("PRAGMA user_version").fetchone()[0]


conn = sqlite3.connect("migrated.db")
print("version:", migrate(conn))
print("version:", migrate(conn))
