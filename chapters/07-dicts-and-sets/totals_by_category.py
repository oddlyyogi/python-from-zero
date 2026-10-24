transactions = [
    ("Coffee", "Food", 4.50),
    ("Rent", "Housing", 900.00),
    ("Lunch", "Food", 12.00),
    ("Gym", "Health", 30.00),
    ("Groceries", "Food", 62.30),
]
totals = {}
categories = set()

for description, category, amount in transactions:
    totals[category] = totals.get(category, 0) + amount
    categories.add(category)

for category in sorted(totals):
    print(f"{category:<10}{totals[category]:>10.2f}")
print(sorted(categories))
