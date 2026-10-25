# Chapter 49: Static Checks With mypy and ruff

How do you catch mistakes without running your program? Think of two proofreaders. In this chapter we use ruff to check style and suspicious code (unused imports, a mutable default argument, a bare except, a comparison to None), apply its automatic fixes, format the file, then fix the rest by hand and configure ruff's rule groups in pyproject.toml. Then mypy --strict finds the missing type hints, we add them, and we chain all three checks into one command. Every output is a real run, for Pocket Ledger.

## Files

- `messy.py`
- `pyproject.toml`

## Run it

From this folder:

```bash
uv run messy.py
```

Tested with Python 3.15.1 and uv 0.13.5.
