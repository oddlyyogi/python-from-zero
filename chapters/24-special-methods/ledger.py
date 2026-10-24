from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    date: str
    description: str
    amount: float


class Ledger:
    def __init__(self, transactions=None):
        self._items = list(transactions or [])

    def __repr__(self):
        return f"Ledger({len(self._items)} transactions)"

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __contains__(self, description):
        return any(t.description == description for t in self._items)

    def __add__(self, other):
        return Ledger(self._items + other._items)

    def __str__(self):
        return "\n".join(f"{t.date} {t.description:<8}{t.amount:>9.2f}" for t in self._items)


ledger = Ledger([
    Transaction("2026-10-01", "Coffee", -4.5),
    Transaction("2026-10-02", "Rent", -900.0),
    Transaction("2026-10-03", "Salary", 3200.0),
])
print(ledger)
print(len(ledger))
for t in ledger:
    print(t.description)
print(ledger[0])
print("Rent" in ledger)
more = Ledger([Transaction("2026-10-04", "Gym", -30.0)])
print(len(ledger + more))
print("---")
print(ledger)
