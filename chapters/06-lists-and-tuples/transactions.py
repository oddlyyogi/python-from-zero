transactions = [
    ("2026-10-01", "Coffee", 4.50),
    ("2026-10-02", "Rent", 900.00),
    ("2026-10-03", "Groceries", 62.30),
]
transactions.append(("2026-09-30", "Gym", 30.00))
transactions.sort()
transactions[0] = ("2026-09-30", "Gym", 35.00)
total = 0
for date, description, amount in transactions:
    print(f"{date}  {description:<10}{amount:>8.2f}")
    total += amount
print(f"{len(transactions)} transactions, total {total:.2f}")
