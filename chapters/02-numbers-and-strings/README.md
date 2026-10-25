# Chapter 2: Numbers and Strings

How do you turn a messy bank line like a lower case name with a dollar sign stuck to the amount into a clean name and a real number? In this chapter we use Python as a calculator, meet integers and floats, slice and search text, use string methods like strip, split, title and replace, fix a real type error, and format money with an f-string. Everything is typed live in the editor and tried in the terminal, and we finish with a small expense-line cleaner for Pocket Ledger.

## Files

- `clean_line.py`

## Run it

From this folder:

```bash
uv run clean_line.py
```


## Practice

Try these on your own copy of the files:

1. Run the cleaner on `"  NETFLIX   $15.99 "` and check the result.
2. Make the cleaner also turn the name to `Title Case` only when it is all upper case.
3. Print the amount with the `$` sign and thousands separators.

Tested with Python 3.15.1 and uv 0.13.5.
