# Chapter 9: Errors and Exceptions: A Safe Amount Parser

What do you do when your program meets bad data? In this chapter we read a real traceback from the bottom up, write a parser that cleans amounts like $1,234.50, catch ValueError with try and except, raise our own error with a clearer message, handle ZeroDivisionError, and meet else and finally. We finish with a safe amount parser for Pocket Ledger that skips bad lines instead of crashing.

## Files

- `parse_amount.py`

## Run it

From this folder:

```bash
uv run parse_amount.py
```


## Practice

Try these on your own copy of the files:

1. Make `parse_amount` also accept amounts in brackets such as `(5.00)`.
2. Add a custom error message for an empty list in `average`.
3. Write a loop that keeps asking for a number until the input is valid.

Tested with Python 3.15.1 and uv 0.13.5.
