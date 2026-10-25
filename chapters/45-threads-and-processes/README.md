# Chapter 45: Threads and Processes

How can a program do several things at once? Think of cooks in a kitchen: one cook can start the water boiling and chop onions while waiting. In this chapter we compare reading five files one at a time (2.5 seconds) with a ThreadPoolExecutor (half a second), use map, submit and as_completed, then see that threads do not speed up heavy arithmetic but processes do, learn why the if __name__ == '__main__' guard matters, and create a real race condition with threads and fix it with a Lock. All timings are measured on the recording machine.

## Files

- `parallel.py`
- `cpu.py`
- `race.py`

## Run it

From this folder:

```bash
uv run parallel.py
```

```bash
uv run cpu.py
```

```bash
uv run race.py
```

Tested with Python 3.15.1 and uv 0.13.5.
