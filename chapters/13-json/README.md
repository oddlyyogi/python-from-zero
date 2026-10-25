# Chapter 13: JSON: Export and Backup

How do programs share data in a format any language can read? In this chapter we turn Python data into JSON with dumps and indent, read it back with loads, see which types change on the way (tuples become lists, True becomes true), write a versioned export and load for the Pocket Ledger transactions, and handle a damaged file with JSONDecodeError. Everything is typed live and run in the terminal.

## Files

- `backup.py`

## Run it

From this folder:

```bash
uv run backup.py
```


## Practice

Try these on your own copy of the files:

1. Add a new field `category` to the export and the load.
2. Bump the version to 2 and make `load` reject version 1 files politely.
3. Break `ledger.json` on purpose and handle the error.

Tested with Python 3.15.1 and uv 0.13.5.
