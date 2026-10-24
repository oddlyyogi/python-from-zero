import pytest
from money import add_tax, format_money, split_bill


def test_format_money():
    assert format_money(1234.5) == "$1,234.50"


def test_add_tax_default_rate():
    assert add_tax(100) == 108


def test_split_bill():
    assert split_bill(100, 3) == (33.33, 1)


def test_add_tax_cents():
    assert add_tax(19.99) == pytest.approx(21.5892)


def test_split_bill_zero_people():
    with pytest.raises(ZeroDivisionError):
        split_bill(100, 0)
