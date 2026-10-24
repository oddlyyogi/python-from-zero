from collections import defaultdict
from itertools import accumulate

transactions = [
    ("food", 9.0),
    ("rent", 900.0),
    ("food", 12.0),
    ("gym", 30.0),
    ("food", 62.0),
    ("health", 40.0),
    ("rent", 900.0),
]

totals = defaultdict(float)
for category, amount in transactions:
    totals[category] += amount

ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
for rank, (category, total) in enumerate(ranked, start=1):
    print(f"{rank}. {category:<8}{total:>10.2f}")

amounts = [amount for category, amount in transactions]
print(list(accumulate(amounts)))
