# Chapter 47: Free-Threaded Python

What is the GIL, and what changes in the free-threaded build of Python 3.15? In this chapter we install both builds with uv, ask sys._is_gil_enabled() in each, and measure a CPU-bound job on four threads: no speed-up in the normal build, a real speed-up in the free-threaded build. We also see the other side of the coin, a counter race that loses updates only when threads truly run in parallel, switch the lock back on with PYTHON_GIL=1, and talk about extension-module compatibility. All timings are real, measured on the recording machine.

## Files

- `ft.py`

## Run it

From this folder:

```bash
uv run ft.py
```


## Notes

Install the free-threaded build with `uv python install 3.15t`, then compare `uv run ft.py` with `uv run --python 3.15t ft.py`.


## Practice

Try these on your own copy of the files:

1. Run your own CPU-bound function under both builds.
2. Test a library of your choice with `PYTHON_GIL=0`.
3. Measure the single-thread time on both builds.

Tested with Python 3.15.1 and uv 0.13.5.
