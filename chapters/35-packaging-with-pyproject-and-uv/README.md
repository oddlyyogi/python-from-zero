# Chapter 35: Packaging With pyproject and uv

How do you turn a folder of code into something anyone can install and run with one word? Think of packing labelled boxes for a move. In this chapter we use uv: uv init --package to create the layout, read every section of pyproject.toml, add our own cli module, point [project.scripts] at it to get a real ledger command, add a dependency with uv add (and meet uv.lock), build a wheel with uv build, and install the command anywhere with uv tool install. Every command is a real run, for Pocket Ledger.

## Files

- `pocket-ledger/pyproject.toml`
- `pocket-ledger/src/pocket_ledger/cli.py`

## Run it

From this folder:

```bash
uv run pocket-ledger/src/pocket_ledger/cli.py
```

Tested with Python 3.15.1 and uv 0.13.5.
