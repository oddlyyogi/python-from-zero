# Chapter 4: Decisions With if

How does a program choose between two or three paths? In this chapter we write a spending category picker. We learn comparisons, and, or and not, truthiness, and if, elif and else, then read two real errors (indentation and a single equals sign where two belong) and see why the order of your questions matters. Everything is typed live and tried in the terminal, and the finished picker is the first step of categorising expenses in Pocket Ledger.

## Files

- `categorize.py`

## Run it

From this folder:

```bash
uv run categorize.py
```


## Practice

Try these on your own copy of the files:

1. Add a `health` category for the words `pharmacy` and `doctor`.
2. Reorder the questions so that large purchases are checked first. What changes?
3. Add a check that prints `refund` when the amount is negative.

Tested with Python 3.15.1 and uv 0.13.5.
