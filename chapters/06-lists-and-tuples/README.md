# Chapter 6: Lists and Tuples

How does Python hold a whole collection of values, and when should it be a list or a tuple? In this chapter we use lists for things that grow and change, append, insert, pop, remove, sort and slice, and tuples for fixed records, with unpacking to read them in one line. We hit the real error you get when changing a tuple, and see why copying a list matters. We finish with the transaction list that holds the data in Pocket Ledger.

## Files

- `transactions.py`
- `alias.py`

## Run it

From this folder:

```bash
uv run transactions.py
```

```bash
uv run alias.py
```


## Practice

Try these on your own copy of the files:

1. Add two more transactions and sort them by amount instead of date.
2. Try to change a tuple and read the error message carefully.
3. Show the difference between `alias = original` and `original.copy()` with your own list.

Tested with Python 3.15.1 and uv 0.13.5.
