# Chapter 3: Variables, Types and f-strings

How does a receipt line up its columns, and how does Python remember and format values? In this chapter we use variables, meet int, float, str and bool, convert between types, and learn f-string formats for decimals, thousands separators, percentages, widths and alignment. Everything is typed live and tried in the terminal, and we finish with a receipt printer for Pocket Ledger, including an honest look at why a rounded total can be a cent off.

## Files

- `receipt.py`

## Run it

From this folder:

```bash
uv run receipt.py
```


## Practice

Try these on your own copy of the files:

1. Add a third item to the receipt and make the columns still line up.
2. Change `WIDTH` to 40 and see which parts follow it.
3. Print the tip rate as a percentage with an f-string format.

Tested with Python 3.15.1 and uv 0.13.5.
