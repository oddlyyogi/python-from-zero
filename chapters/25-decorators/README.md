# Chapter 25: Decorators: Timing, Caching and Retry

What is a decorator, and how can you add timing, caching or retries to a function without touching its code? In this chapter we see that functions are values, build a closure, and write a timed decorator step by step, with *args and **kwargs. We fix the lost function name with functools.wraps, speed up a slow Fibonacci with functools.cache and watch the real timing drop to zero, and write a decorator with its own settings: retry(3). These are reusable helpers for Pocket Ledger.

## Files

- `decorators.py`

## Run it

From this folder:

```bash
uv run decorators.py
```


## Practice

Try these on your own copy of the files:

1. Write a `@logged` decorator that prints the function name.
2. Use `functools.cache` on a function of your own and time it.
3. Change `retry` so it waits between attempts.

Tested with Python 3.15.1 and uv 0.13.5.
