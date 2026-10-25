# Chapter 7: Dictionaries and Sets

How do you look something up by name, and how do you keep only unique values? In this chapter we use dictionaries for lookup by key, with get, del, keys, values and items, and sets for unique values, with add, union and intersection. We hit a real KeyError and fix it with get and a default, then total transactions by category. The result is the totals-by-category report for Pocket Ledger.

## Files

- `totals_by_category.py`

## Run it

From this folder:

```bash
uv run totals_by_category.py
```


## Practice

Try these on your own copy of the files:

1. Add a new category and check that the totals still work.
2. Use a set to find which categories appear in both of two lists of transactions.
3. Replace `totals.get(...)` with `collections.defaultdict(float)`.

Tested with Python 3.15.1 and uv 0.13.5.
