# /// script
# dependencies = ["matplotlib"]
# ///
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

totals = {"food": 83.3, "housing": 900.0, "health": 48.4, "other": 22.0}
names = list(totals)
values = list(totals.values())

order = sorted(totals, key=totals.get)
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(order, [totals[k] for k in order], color="#4C9BE8")
ax.set_title("Spending by category, October")
ax.set_xlabel("Amount ($)")
ax.bar_label(bars, fmt="$%.2f")
fig.tight_layout()
fig.savefig("spending.png", dpi=120)

days = [1, 5, 10, 15, 20, 25, 30]
balance = [1250, 1245.5, 345.5, 315.5, 3515.5, 3453.2, 3410.8]

fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.plot(days, balance, marker="o")
ax2.set_xlabel("Day of month")
ax2.set_ylabel("Balance ($)")
ax2.grid(True, alpha=0.3)
fig2.savefig("balance.png", dpi=120)

fig3, (left, right) = plt.subplots(1, 2, figsize=(12, 4))
left.barh(order, [totals[k] for k in order])
right.plot(days, balance, marker="o")
fig3.suptitle("Pocket Ledger, October")
fig3.savefig("dashboard.png", dpi=120)
