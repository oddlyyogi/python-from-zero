from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


def to_money(value: str | float | Decimal) -> Decimal:
    """Turn text or a number into a Decimal rounded to cents."""
    cleaned = str(value).strip().replace("$", "").replace(",", "")
    return Decimal(cleaned).quantize(CENT, ROUND_HALF_UP)


def format_money(amount: Decimal) -> str:
    return f"${amount:,.2f}"
