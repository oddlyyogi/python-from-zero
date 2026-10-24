type Transaction = tuple[str, str, float]


def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))
amounts: list[float] = [4.5, 12.0]
totals: dict[str, float] = {}
pair: tuple[str, str, float] = ("2026-10-01", "Coffee", 4.5)

def total(items: list[Transaction]) -> float:
    return sum(amount for _, _, amount in items)

def find(description: str, items: list[Transaction]) -> Transaction | None:
    for item in items:
        if item[1] == description:
            return item
    return None

ledger: list[Transaction] = [("2026-10-01", "Coffee", 4.5), ("2026-10-02", "Rent", 900.0)]
found = find("Rent", ledger)
if found is not None:
    print(found[2])

def first[T](items: list[T]) -> T:
    return items[0]

reveal_type(first([1, 2]))
