# Chapter 5: Loops: for, while, break and continue

How do you repeat a step for every receipt in a pile? In this chapter we learn for loops with range and lists, keep a running total, number items with enumerate, skip refunds with continue, stop early with break, and repeat until a goal with while. Everything is typed live and tried in the terminal, and we finish with a monthly total calculator with a budget guard for Pocket Ledger.

## Files

- `monthly_total.py`
- `savings.py`

## Run it

From this folder:

```bash
uv run monthly_total.py
```

```bash
uv run savings.py
```


## Practice

Try these on your own copy of the files:

1. Change the budget to 100 and predict where the loop stops before you run it.
2. Use `continue` to also skip amounts larger than 1000.
3. Write a `while` loop that counts the months until savings reach 1000 at 125 a month.

Tested with Python 3.15.1 and uv 0.13.5.
