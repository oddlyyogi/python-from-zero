import json
from pathlib import Path

FILE = Path("ledger.json")

def export(transactions):
    items = []
    for date, description, amount in transactions:
        items.append({"date": date, "description": description, "amount": amount})
    data = {"version": 1, "transactions": items}
    FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

def load():
    data = json.loads(FILE.read_text(encoding="utf-8"))
    if data["version"] != 1:
        raise ValueError(f"unknown version {data['version']}")
    transactions = []
    for item in data["transactions"]:
        transactions.append((item["date"], item["description"], item["amount"]))
    return transactions

transactions = [("2026-10-01", "Coffee", 4.5), ("2026-10-02", "Rent", 900.0)]
export(transactions)
print(FILE.read_text())
print(load() == transactions)

FILE.write_text('{"version": 1, "transactions": [')
try:
    load()
except json.JSONDecodeError as error:
    print("damaged file:", error)
