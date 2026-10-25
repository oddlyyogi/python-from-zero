# Chapter 19: Classes: A Transaction Class

What is a class, and how do you build your own objects? Think of a cookie cutter and the cookies it makes. In this chapter we write a Transaction class step by step: __init__ and self, attributes, creating objects, methods that use the object's own data, the real error you get when a method forgets self, a class attribute shared by every object, and a method that changes the object's state. It is the building block for Pocket Ledger.

## Files

- `transaction.py`

## Run it

From this folder:

```bash
uv run transaction.py
```


## Practice

Try these on your own copy of the files:

1. Add a method `is_income()` to the `Transaction` class.
2. Add a class attribute for the currency and print it.
3. Create three objects and sort them by amount.

Tested with Python 3.15.1 and uv 0.13.5.
