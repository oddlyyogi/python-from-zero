# Chapter 21: Enums: Safe Categories

How do you stop a typo like "Food" instead of "food" from silently becoming a bug? In this chapter we meet enums: we start with a function that compares category strings and quietly returns the wrong answer, define a Category Enum, read name and value, convert text back to a choice, loop over all choices, see the real AttributeError and ValueError for bad names, use the enum in a budget function, add a method, and try StrEnum. The Category enum is a safe building block for Pocket Ledger.

## Files

- `categories.py`

## Run it

From this folder:

```bash
uv run categories.py
```


## Practice

Try these on your own copy of the files:

1. Add a `TRAVEL` category and update `budget`.
2. Loop over the enum and print every name and value.
3. Turn a text from a file into a `Category` safely.

Tested with Python 3.15.1 and uv 0.13.5.
