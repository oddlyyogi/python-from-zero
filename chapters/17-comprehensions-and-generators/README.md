# Chapter 17: Comprehensions and Generators

How do you build a new list in one line, and how do you process a huge file without loading it all into memory? In this chapter we write list, dictionary and set comprehensions with filters, then switch the brackets to get generator expressions, use next, measure the memory difference with sys.getsizeof, and write a generator function with yield that streams amounts from raw lines. Everything is typed live and run for real, for Pocket Ledger.

## Files

- `stream.py`

## Run it

From this folder:

```bash
uv run stream.py
```


## Practice

Try these on your own copy of the files:

1. Write a generator that yields only the expenses from a list of lines.
2. Rewrite one of your loops as a list comprehension.
3. Compare `sys.getsizeof` for a list and a generator over a million numbers.

Tested with Python 3.15.1 and uv 0.13.5.
