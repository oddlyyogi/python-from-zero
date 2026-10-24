# Chapter 25: Decorators: Timing, Caching and Retry

What is a decorator, and how can you add timing, caching or retries to a function without touching its code? In this chapter we see that functions are values, build a closure, and write a timed decorator step by step, with *args and **kwargs. We fix the lost function name with functools.wraps, speed up a slow Fibonacci with functools.cache and watch the real timing drop to zero, and write a decorator with its own settings: retry(3). These are reusable helpers for Pocket Ledger.

## Files

- `decorators.py`

## Run it

From this folder:

```bash
uv run decorators.py
```

Tested with Python 3.15.1 and uv 0.13.5.
