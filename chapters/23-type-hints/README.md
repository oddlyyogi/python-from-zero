# Chapter 23: Type Hints: A Typed Ledger

How do you label your code so that mistakes are caught before you run it? In this chapter we add type hints to functions, variables, lists, dictionaries and tuples, see that Python itself ignores them at runtime, and then run the mypy type checker with uvx to catch the real bugs. We use the modern type statement for aliases, X | None for optional results (and the error the checker gives when you forget the None case), and generic functions with def first[T]. Everything is typed live and run for real.

## Files

- `typed_ledger.py`

## Run it

From this folder:

```bash
uv run typed_ledger.py
```

Tested with Python 3.15.1 and uv 0.13.5.
