# Chapter 23: Type Hints: A Typed Ledger

How do you label your code so that mistakes are caught before you run it? In this chapter we add type hints to functions, variables, lists, dictionaries and tuples, see that Python itself ignores them at runtime, and then run the mypy type checker with uvx to catch the real bugs. We use the modern type statement for aliases, X | None for optional results (and the error the checker gives when you forget the None case), and generic functions with def first[T]. Everything is typed live and run for real.

## Files

- `typed_ledger.py`

## Run it

From this folder:

```bash
uv run typed_ledger.py
```


## Notes

`reveal_type(...)` is understood by the type checker. To run the file with plain Python as well, add `from typing import reveal_type` at the top.


## Practice

Try these on your own copy of the files:

1. Add type hints to a function of your own and check it with `mypy`.
2. Define a type alias for a list of transactions.
3. Write a generic `last[T]` function.

Tested with Python 3.15.1 and uv 0.13.5.
