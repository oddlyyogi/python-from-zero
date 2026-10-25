# Chapter 18: Sorting, Grouping, collections and itertools

How do you find the biggest spenders, count categories, group items and build a running balance? In this chapter we use sorted with key, lambda, Counter and most_common, defaultdict, and itertools tools like accumulate, islice and chain. We combine them into a top-spenders report that ranks categories by total, plus a running balance, for Pocket Ledger. Everything is typed live and run for real.

## Files

- `top_spenders.py`

## Run it

From this folder:

```bash
uv run top_spenders.py
```


## Practice

Try these on your own copy of the files:

1. Find the three smallest transactions with `sorted` and `key`.
2. Count how many transactions each category has with `Counter`.
3. Compute a running balance with `itertools.accumulate`.

Tested with Python 3.15.1 and uv 0.13.5.
