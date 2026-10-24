# Chapter 29: Custom Exceptions: Clear Ledger Errors

Why is a vague ValueError a poor label, and how do you give your own errors clear names? In this chapter we write a base LedgerError and specific children InvalidAmount and UnknownCategory, make an error carry data, raise them from a parse function, and catch them from specific to general. We read a real chained traceback made with raise ... from error, hide the chain with from None, and attach context with add_note. This is the error family for Pocket Ledger.

## Files

- `errors.py`

## Run it

From this folder:

```bash
uv run errors.py
```

Tested with Python 3.15.1 and uv 0.13.5.
