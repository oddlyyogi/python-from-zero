import csv

def import_bank_csv(path):
    transactions = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                amount = float(row["Amount"].replace(",", ""))
            except ValueError:
                print(f"skipping row: {row}")
                continue
            transactions.append((row["Date"], row["Description"].strip(), amount))
    return transactions

transactions = import_bank_csv("bank_export.csv")
for t in transactions:
    print(t)
print(f"{len(transactions)} transactions imported")

with open("summary.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "description", "amount", "kind"])
    for date, description, amount in transactions:
        kind = "income" if amount > 0 else "expense"
        writer.writerow([date, description, amount, kind])
