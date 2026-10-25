from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    date: str
    description: str
    amount: Decimal
    category: str = "other"
