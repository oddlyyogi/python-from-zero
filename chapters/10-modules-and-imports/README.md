# Chapter 10: Modules and Imports

How do you split a program into files and reuse code from Python's standard library? In this chapter we import math and statistics, use import, from import and import as, write our own money module, guard a file with if __name__ == "__main__" so it works as both script and module, read the real ModuleNotFoundError, and try the new lazy import of Python 3.15 with a before-and-after check of sys.modules.

## Files

- `money.py`
- `report.py`

## Run it

From this folder:

```bash
uv run money.py
```

```bash
uv run report.py
```


## Practice

Try these on your own copy of the files:

1. Move `add_tax` into its own module and import it.
2. Add a function to `money.py` and use it from `report.py`.
3. Use `lazy import` for another standard library module and check `sys.modules`.

Tested with Python 3.15.1 and uv 0.13.5.
