from dataclasses import dataclass, field, replace, asdict

@dataclass(frozen=True, order=True)
class Transaction:
    date: str
    description: str
    amount: float
    reviewed: bool = False
    tags: list = field(default_factory=list)


    def __post_init__(self):
        if not self.description:
            raise ValueError("description is required")

t1 = Transaction("2026-10-01", "Coffee", -4.50)
t2 = Transaction("2026-10-01", "Coffee", -4.50)
print(t1)
print(t1 == t2)
t3 = replace(t1, amount=-5.0)
print(t3)
print(asdict(t1))
late = Transaction("2026-10-09", "Gym", -30.0)
print(t1 < late)
Transaction("2026-10-01", "", 1.0)
