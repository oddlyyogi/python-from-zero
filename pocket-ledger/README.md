# Pocket Ledger

A small personal expense tracker, assembled in the final chapter of the **Python From Zero** course.

## Features

- Reads a messy bank CSV (quoted commas, thousands separators, bad rows are skipped with a warning)
- Exact money with `Decimal`, always rounded to cents
- Rule-based categories (food, housing, health, income, other)
- SQLite storage
- Command line tool: `ledger import` and `ledger report`
- Web API: `GET /totals` (FastAPI)
- Tests with pytest; checked with ruff and mypy (strict)

## Quick start

```bash
cd pocket-ledger
uv run ledger import bank.csv
uv run ledger report
```

Start the web API and ask for the totals:

```bash
uv run ledger-api
curl -s localhost:8000/totals
```

Run the tests and the checks:

```bash
uv run pytest -q
uvx ruff check && uvx ruff format --check
uv run --with mypy mypy --strict src
```

## Layout

```text
src/pocket_ledger/
    money.py      exact money helpers
    models.py     the Transaction dataclass
    rules.py      category rules
    importer.py   CSV importer
    store.py      SQLite storage
    report.py     text report
    cli.py        command line interface
    api.py        web API
tests/            pytest tests
bank.csv          sample bank export (made-up data)
```

Requires Python 3.15 and [uv](https://docs.astral.sh/uv/).
