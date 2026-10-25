import random
import time

random.seed(1)
categories = ["food", "rent", "gym", "health", "travel", "fun"]
transactions = [
    (i, random.choice(categories), round(random.uniform(1, 200), 2))
    for i in range(20000)
]


def find_duplicates(transactions):
    seen = set()
    duplicates = 0
    for t in transactions:
        if t[1:] in seen:
            duplicates += 1
        else:
            seen.add(t[1:])
    return duplicates


def totals(transactions):
    result = {}
    for _, category, amount in transactions:
        result[category] = result.get(category, 0) + amount
    return result


start = time.perf_counter()
print("duplicates:", find_duplicates(transactions))
print({k: round(v, 2) for k, v in totals(transactions).items()})
print(f"took {time.perf_counter() - start:.2f}s")
