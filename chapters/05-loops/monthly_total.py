amounts = [4.50, 3.25, 12.00, -20.00, 30.00, 15.00, 8.00]
budget = 40.00
total = 0

for number, amount in enumerate(amounts, start=1):
    if amount < 0:
        print(f"{number}. refund skipped")
        continue
    total += amount
    print(f"{number}. {amount:>8.2f}  running total {total:>8.2f}")
    if total > budget:
        print("over budget, stopping")
        break

print(f"total: {total:.2f}")
