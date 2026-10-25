from decimal import Decimal

import pytest

from pocket_ledger.money import format_money, to_money


@pytest.mark.parametrize(
    "text, expected",
    [("4.5", "4.50"), ("$1,234.5", "1234.50"), ("-20", "-20.00")],
)
def test_to_money(text, expected):
    assert to_money(text) == Decimal(expected)


def test_format_money():
    assert format_money(Decimal("1234.5")) == "$1,234.50"
