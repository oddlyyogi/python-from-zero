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

Tested with Python 3.15.1 and uv 0.13.5.
