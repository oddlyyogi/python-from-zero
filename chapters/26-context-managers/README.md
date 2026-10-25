# Chapter 26: Context Managers: Safe Files and Cleanup

How does the with statement guarantee cleanup, and how can you build your own? In this chapter we see why open() needs closing, then write a class with __enter__ and __exit__ and watch cleanup happen even when the block raises an error. We use contextlib.contextmanager to do the same in fewer lines, build an atomic_write that never leaves a half-written file when a crash happens, and meet contextlib.suppress and tempfile.TemporaryDirectory. It is a safe-storage piece for Pocket Ledger.

## Files

- `safe_save.py`

## Run it

From this folder:

```bash
uv run safe_save.py
```


## Practice

Try these on your own copy of the files:

1. Write a context manager that times a block of code.
2. Make `atomic_write` keep a backup of the old file.
3. Use `suppress` to delete a file that may not exist.

Tested with Python 3.15.1 and uv 0.13.5.
