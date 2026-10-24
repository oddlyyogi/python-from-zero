# Chapter 27: Functions in Depth: A Rule Engine

What are all the ways a function can take input, and how can functions themselves be data? In this chapter we use default values and keyword-only parameters, *args and **kwargs, and unpacking with * and ** when calling. Then we treat functions as values: functions that build functions with lambda, a list of (test, category) rules, a categorize function where the first matching rule wins, the real TypeError for a keyword-only mistake, and functools.partial. The result is the rule engine that categorizes Pocket Ledger transactions.

## Files

- `rules.py`

## Run it

From this folder:

```bash
uv run rules.py
```

Tested with Python 3.15.1 and uv 0.13.5.
