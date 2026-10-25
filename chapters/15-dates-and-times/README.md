# Chapter 15: Dates and Times: Group by Month

How do you calculate with dates when months and years have different lengths? In this chapter we use the datetime module: date objects, weekday, isoformat and fromisoformat, timedelta, strftime and strptime, and the calendar module. Then we group Pocket Ledger spending by month with a formatted key, count transactions per weekday, meet the real error for an impossible date, and work out how old each transaction is.

## Files

- `by_month.py`

## Run it

From this folder:

```bash
uv run by_month.py
```


## Practice

Try these on your own copy of the files:

1. Group the transactions by weekday and print the busiest day.
2. Compute how many days are left until the end of the month.
3. Print each date in the form `Saturday 3 October 2026`.

Tested with Python 3.15.1 and uv 0.13.5.
