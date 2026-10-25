# Chapter 16: Decimal and Money

Why does 0.1 + 0.2 not equal 0.3, and how should a program handle money? In this chapter we see float surprises in a real session, then use the decimal module: create Decimals from strings, round with quantize and choose a rounding rule, hit the real TypeError for mixing Decimal and float, and write money helpers. We rebuild a receipt whose totals add up to the cent and split a bill without losing a penny, for Pocket Ledger.

## Files

- `money_decimal.py`

## Run it

From this folder:

```bash
uv run money_decimal.py
```


## Practice

Try these on your own copy of the files:

1. Add a `refund` helper that returns a `Decimal` rounded half up.
2. Split 100.00 between 7 people without losing a cent.
3. Find a calculation where `float` and `Decimal` disagree.

Tested with Python 3.15.1 and uv 0.13.5.
