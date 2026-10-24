# Chapter 24: Special Methods: A Ledger You Can Loop Over

How do the built-in tools like len, for loops, square brackets, in and + work, and how can your own classes join in? In this chapter we build a Ledger class and teach it Python's special (dunder) methods one at a time: __repr__, __len__, __iter__, __getitem__, __contains__, __add__ and __str__. At each step we first see the real error Python gives (no len, not iterable, not subscriptable, unsupported operand), then fix it. We also see why 'Rent' in ledger quietly returns False without __contains__.

## Files

- `ledger.py`

## Run it

From this folder:

```bash
uv run ledger.py
```

Tested with Python 3.15.1 and uv 0.13.5.
