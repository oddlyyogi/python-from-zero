# Chapter 50: Capstone: Assemble Pocket Ledger

Put it all together. In this final chapter we build Pocket Ledger, a small but complete Python application, module by module: exact money with Decimal, a frozen dataclass model, a rule-based categoriser, a CSV importer that skips bad rows and logs a warning, an SQLite store, a text report, a command line tool with sub-commands, pytest tests, a FastAPI web API, and finally ruff and mypy --strict checks. Every command and output is a real run, and the finished project is in the course repository.

## The project

The finished application is in [`pocket-ledger/`](../../pocket-ledger). From that folder:

```bash
uv run ledger import bank.csv
uv run ledger report
uv run pytest -q
```

Tested with Python 3.15.1 and uv 0.13.5.

## Practice

1. Add a `ledger export` command that writes JSON.
2. Add a new endpoint `GET /transactions`.
3. Add a test for the report text.
