# Chapter 8: Functions: Reusable Money Helpers

How do you write a piece of code once and use it again and again? In this chapter we define functions with def, take parameters, return values, use default and keyword arguments, return two values at once, understand scope and read the real error for a name that does not exist outside a function, and add a docstring. We build three reusable money helpers for Pocket Ledger: format_money, add_tax and split_bill.

## Files

- `money_helpers.py`

## Run it

From this folder:

```bash
uv run money_helpers.py
```


## Practice

Try these on your own copy of the files:

1. Write `percent_change(old, new)` and test it by hand.
2. Give `split_bill` a `tip` parameter with a default of 0.
3. Add a docstring to every function and read them with `help()`.

Tested with Python 3.15.1 and uv 0.13.5.
