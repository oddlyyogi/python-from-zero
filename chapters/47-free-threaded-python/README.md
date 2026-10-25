# Chapter 47: Free-Threaded Python

What is the GIL, and what changes in the free-threaded build of Python 3.15? In this chapter we install both builds with uv, ask sys._is_gil_enabled() in each, and measure a CPU-bound job on four threads: no speed-up in the normal build, a real speed-up in the free-threaded build. We also see the other side of the coin, a counter race that loses updates only when threads truly run in parallel, switch the lock back on with PYTHON_GIL=1, and talk about extension-module compatibility. All timings are real, measured on the recording machine.

## Files

- `ft.py`

## Run it

From this folder:

```bash
uv run ft.py
```

Tested with Python 3.15.1 and uv 0.13.5.
