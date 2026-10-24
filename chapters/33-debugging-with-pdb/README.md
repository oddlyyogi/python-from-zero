# Chapter 33: Debugging With print and pdb

What do you do when your program gives the wrong answer and there is no error message? In this chapter we hunt a real bug in a running-balance function. We start with print debugging, then use breakpoint() and the pdb debugger with l, p, n and c to see the real values, find the off-by-one loop, fix it, use post-mortem debugging after a crash with w and p, and leave an assert behind. Every pdb session is a real run.

## Files

- `balance.py`
- `crash.py`

## Run it

From this folder:

```bash
uv run balance.py
```

```bash
uv run crash.py
```

Tested with Python 3.15.1 and uv 0.13.5.
