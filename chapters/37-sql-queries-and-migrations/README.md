# Chapter 37: SQL Queries and Migrations

How do you ask a database questions like 'how much did I spend on food in October?' In this chapter we load nine sample transactions into SQLite and write real queries: WHERE, ORDER BY, LIMIT, GROUP BY with SUM and COUNT, LIKE for a month, parameters with ?, and single answers with fetchone. Then we change a table with ALTER TABLE and build a tiny migration runner with PRAGMA user_version so a program can evolve its database without losing data. Every output is a real run, for Pocket Ledger.

## Files

- `queries.py`
- `migrate.py`

## Run it

From this folder:

```bash
uv run queries.py
```

```bash
uv run migrate.py
```

Tested with Python 3.15.1 and uv 0.13.5.
