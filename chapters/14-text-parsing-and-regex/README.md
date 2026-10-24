# Chapter 14: Text Parsing and Regular Expressions

How do you pull a date, a description and an amount out of a messy statement line? In this chapter we use the re module: findall, search, sub, groups and named groups, greedy versus lazy matching, and the ignore-case flag. Then we build a readable pattern in three pieces, run it over sample statement lines, skip the line that is not a transaction, and produce clean tuples for Pocket Ledger.

## Files

- `parse_line.py`

## Run it

From this folder:

```bash
uv run parse_line.py
```

Tested with Python 3.15.1 and uv 0.13.5.
