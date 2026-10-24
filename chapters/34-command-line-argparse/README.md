# Chapter 34: Command Line Tools With argparse

How do you build a real command line tool, like git, with sub-commands and helpful errors? In this chapter we see what sys.argv gives a program, then use argparse: positional arguments with a type, the automatic error for a bad value, generated -h help, optional flags with choices and defaults, sub-commands add and list wired up with set_defaults, a main(argv) function, and a JSON-backed ledger you can really use. All commands and outputs are real runs, for Pocket Ledger.

## Files

- `cli.py`

## Run it

From this folder:

```bash
uv run cli.py
```

Tested with Python 3.15.1 and uv 0.13.5.
