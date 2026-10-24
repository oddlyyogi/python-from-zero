from datetime import date

transactions = [
    ("2026-09-28", "Coffee", 4.50),
    ("2026-10-01", "Rent", 900.00),
    ("2026-10-03", "Lunch", 12.00),
    ("2026-10-15", "Gym", 30.00),
    ("2026-11-02", "Coffee", 5.00),
]
totals = {}
by_day = {}
for text, description, amount in transactions:
    d = date.fromisoformat(text)
    key = f"{d:%Y-%m}"
    totals[key] = totals.get(key, 0) + amount
    name = d.strftime("%A")
    by_day[name] = by_day.get(name, 0) + 1

for month in sorted(totals):
    print(f"{date.fromisoformat(month + '-01'):%B %Y}  {totals[month]:>8.2f}")
print(by_day)

today = date(2026, 11, 5)
for text, description, amount in transactions:
    print(text, (today - date.fromisoformat(text)).days)
