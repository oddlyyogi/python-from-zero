from decimal import Decimal

from pocket_ledger.importer import import_csv


def test_import_skips_bad_rows(tmp_path):
    path = tmp_path / "bank.csv"
    path.write_text(
        "Date,Description,Amount\n2026-10-01,Coffee,-4.5\n2026-10-02,Oops,n/a\n"
    )
    items = import_csv(path)
    assert len(items) == 1
    assert items[0].amount == Decimal("-4.50")
    assert items[0].category == "food"
