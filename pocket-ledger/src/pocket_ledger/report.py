from decimal import Decimal

from .money import format_money


def text_report(totals: dict[str, Decimal]) -> str:
    lines = ["Pocket Ledger", "-------------"]
    for category, total in sorted(totals.items(), key=lambda item: item[1]):
        lines.append(f"{category:<10}{format_money(total):>12}")
    balance = sum(totals.values(), Decimal(0))
    lines.append(f"{'balance':<10}{format_money(balance):>12}")
    return "\n".join(lines)
