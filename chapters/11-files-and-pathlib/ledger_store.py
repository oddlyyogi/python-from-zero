from pathlib import Path

FILE = Path("ledger.txt")

def save(transactions):
    with FILE.open("w", encoding="utf-8") as f:
        for date, description, amount in transactions:
            f.write(f"{date}|{description}|{amount}\n")

def load():
    if not FILE.exists():
        return []
    transactions = []
    for line in FILE.read_text(encoding="utf-8").splitlines():
        date, description, amount = line.split("|")
        transactions.append((date, description, float(amount)))
    return transactions

data = [
    ("2026-10-01", "Coffee", 4.5),
    ("2026-10-02", "Rent", 900.0),
    ("2026-10-03", "Lunch", 12.0),
]
print(load())
save(data)
print(FILE.read_text())
print(load() == data)
