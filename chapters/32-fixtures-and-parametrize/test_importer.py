import pytest
from importer import import_csv, parse_amount



@pytest.mark.parametrize("text, expected", [
    ("4.50", 4.5),
    ("$4.50", 4.5),
    ("1,234.50", 1234.5),
    ("-20", -20.0),
    ("  7  ", 7.0),
])
def test_parse_amount(text, expected):
    assert parse_amount(text) == expected


@pytest.mark.parametrize("text", ["abc", ""])
def test_bad_amount(text):
    with pytest.raises(ValueError):
        parse_amount(text)


@pytest.fixture
def sample_csv(tmp_path):
    path = tmp_path / "bank.csv"
    path.write_text('Date,Description,Amount\n2026-10-01,Coffee,-4.50\n2026-10-02,Rent,"-1,200.00"\n')
    return path


def test_import_csv(sample_csv):
    assert import_csv(sample_csv) == [("2026-10-01", "Coffee", -4.5), ("2026-10-02", "Rent", -1200.0)]


@pytest.mark.xfail(reason="brackets not supported yet")
def test_bracket_negative():
    assert parse_amount("(5.00)") == -5
