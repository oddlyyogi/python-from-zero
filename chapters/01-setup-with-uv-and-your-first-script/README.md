# Chapter 1: Setup With uv and Your First Script

How do you go from nothing installed to a working Python program? In this first chapter we install Python 3.15 with uv, create a file, run it, read two kinds of error message, use variables and f-strings, try the interactive prompt, and write the first piece of Pocket Ledger, a small spending tracker we grow through the series. Everything is typed live and explained as it is typed. Think of Python as a patient assistant that follows your written list one line at a time.

## Files

- `hello.py`
- `ledger_hello.py`

## Run it

From this folder:

```bash
uv run hello.py
```

```bash
uv run ledger_hello.py
```


## Practice

Try these on your own copy of the files:

1. Change the greeting in `hello.py` to your own name, then run it again.
2. Add a second variable `rent` to `ledger_hello.py` and subtract it from the balance.
3. Open `uv run python` and use it as a calculator for three of your own sums.

Tested with Python 3.15.1 and uv 0.13.5.
