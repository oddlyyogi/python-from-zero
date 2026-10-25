# Chapter 36: SQLite: Store Transactions in a Database

How do you store data so you can ask questions of it later? Think of a filing cabinet with drawers (tables), folders (rows) and labelled sections (columns). In this chapter we use SQLite from the standard library: connect, create a table, insert rows with ? placeholders, commit, select with fetchall, then build a db module with row_factory, init_db, add and all_rows, see the data persist across runs, and see the real syntax error that shows why you must never build SQL with f-strings. The result is the storage layer for Pocket Ledger.

## Files

- `db.py`

## Run it

From this folder:

```bash
uv run db.py
```


## Practice

Try these on your own copy of the files:

1. Add a column `category` to the table.
2. Write a function that deletes a transaction by id.
3. Select only the rows from one month.

Tested with Python 3.15.1 and uv 0.13.5.
