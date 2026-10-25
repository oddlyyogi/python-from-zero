# Chapter 48: Profiling and Speed

How do you make a slow program fast without guessing? In this chapter we take a deliberately slow report, measure it, and find the culprit with a profiler: we try the new sampling profiler of Python 3.15 (and see its real permission message on macOS), then use profiling.tracing to find that nearly all the time is in one function. We explain why a list membership test is slow, prove with timeit that a set is thousands of times faster, fix the code with two small edits, and measure again. Every number is a real measurement, for Pocket Ledger.

## Files

- `slow_report.py`

## Run it

From this folder:

```bash
uv run slow_report.py
```


## Notes

The sampling profiler may need administrator rights on macOS. The tracing profiler works everywhere: `uv run python -m profiling.tracing -s tottime slow_report.py`.


## Practice

Try these on your own copy of the files:

1. Profile one of your own scripts.
2. Find a second slow spot and measure the fix.
3. Use `timeit` to compare two ways of joining strings.

Tested with Python 3.15.1 and uv 0.13.5.
