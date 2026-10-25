# Chapter 48: Profiling and Speed

How do you make a slow program fast without guessing? In this chapter we take a deliberately slow report, measure it, and find the culprit with a profiler: we try the new sampling profiler of Python 3.15 (and see its real permission message on macOS), then use profiling.tracing to find that nearly all the time is in one function. We explain why a list membership test is slow, prove with timeit that a set is thousands of times faster, fix the code with two small edits, and measure again. Every number is a real measurement, for Pocket Ledger.

## Files

- `slow_report.py`

## Run it

From this folder:

```bash
uv run slow_report.py
```

Tested with Python 3.15.1 and uv 0.13.5.
