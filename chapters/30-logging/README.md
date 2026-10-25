# Chapter 30: Logging: An Audit Trail

How do you keep a record of what your program did, with time stamps and levels, instead of scattered print statements? In this chapter we use the logging module: the five levels, why info is hidden by default, named loggers, basicConfig with a format and a date format, logging to a file, log.exception to save a full traceback, and lazy % formatting. We finish with an audit trail logbook for Pocket Ledger.

## Files

- `audit.py`

## Run it

From this folder:

```bash
uv run audit.py
```


## Practice

Try these on your own copy of the files:

1. Send warnings and errors to the console and everything to a file.
2. Log the number of rows imported.
3. Change the log format to include the function name.

Tested with Python 3.15.1 and uv 0.13.5.
