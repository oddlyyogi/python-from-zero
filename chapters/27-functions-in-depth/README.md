# Chapter 27: Functions in Depth: A Rule Engine

What are all the ways a function can take input, and how can functions themselves be data? In this chapter we use default values and keyword-only parameters, *args and **kwargs, and unpacking with * and ** when calling. Then we treat functions as values: functions that build functions with lambda, a list of (test, category) rules, a categorize function where the first matching rule wins, the real TypeError for a keyword-only mistake, and functools.partial. The result is the rule engine that categorizes Pocket Ledger transactions.

## Files

- `rules.py`

## Run it

From this folder:

```bash
uv run rules.py
```


## Practice

Try these on your own copy of the files:

1. Add a rule for `salary` to the rule engine.
2. Write a function that makes a rule from a word and a category.
3. Use `functools.partial` to preset an argument.

Tested with Python 3.15.1 and uv 0.13.5.
