# Chapter 12: CSV Files: Import a Bank Export

How do you read the file your bank lets you download? In this chapter we see why splitting on commas breaks on real data, then use the csv module: reader, DictReader and writer. We handle quoted commas, thousands separators, stray spaces and a row with n/a, skip the bad row with try and except, and write a summary CSV back out. The result is the importer that sits at the front door of Pocket Ledger.

## Files

- `import_csv.py`
- `bank_export.csv`

## Run it

From this folder:

```bash
uv run import_csv.py
```


## Practice

Try these on your own copy of the files:

1. Add a row with a quoted comma to `bank_export.csv` and check that it imports.
2. Write a CSV with the totals per category.
3. Skip rows whose date is not in `YYYY-MM-DD` format.

Tested with Python 3.15.1 and uv 0.13.5.
