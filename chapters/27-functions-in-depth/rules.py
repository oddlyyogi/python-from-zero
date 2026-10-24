def contains(*words):
    return lambda t: any(w in t["description"].lower() for w in words)


def over(limit):
    return lambda t: t["amount"] > limit


RULES = [
    (contains("coffee", "cafe", "lunch"), "Food"),
    (contains("rent"), "Housing"),
    (over(1000), "Large purchase"),
]


def categorize(t, *, default="Other"):
    for test, category in RULES:
        if test(t):
            return category
    return default


transactions = [
    {"description": "Starbucks Coffee", "amount": 4.5},
    {"description": "Monthly Rent", "amount": 900.0},
    {"description": "Laptop", "amount": 1899.0},
    {"description": "Gym", "amount": 30.0},
]
for t in transactions:
    print(f"{t['description']:<18}{categorize(t)}")
print(categorize(transactions[3], default="Health"))
