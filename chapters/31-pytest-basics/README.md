# Chapter 31: pytest Basics: Test the Money Helpers

How do you know your code still works after you change it? In this chapter we write tests with pytest for the money helpers: test functions and assert, running pytest with uv, reading a real failure (and finding a deliberate bug), going green, comparing floats with pytest.approx, checking errors with pytest.raises, and the -v, -k and -x options. Everything is typed live and run for real, and the tests become the safety net for Pocket Ledger.

## Files

- `money.py`
- `test_money.py`

## Run it

From this folder:

```bash
uv run --with pytest pytest -v
```

```bash
uv run money.py
```

Tested with Python 3.15.1 and uv 0.13.5.
