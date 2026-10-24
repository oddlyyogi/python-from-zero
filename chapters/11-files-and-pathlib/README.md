# Chapter 11: Files and pathlib: Save and Load

How does a program remember anything after it ends? In this chapter we use pathlib to build paths and check whether a file exists, write and append text, read a whole file or loop over its lines, and let the with statement close files safely. We hit the real FileNotFoundError and handle it, then write a save and load pair that stores the Pocket Ledger transactions in a plain text file and reads them back exactly.

## Files

- `ledger_store.py`

## Run it

From this folder:

```bash
uv run ledger_store.py
```

Tested with Python 3.15.1 and uv 0.13.5.
