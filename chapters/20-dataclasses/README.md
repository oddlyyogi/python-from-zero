# Chapter 20: Dataclasses: A Cleaner Transaction

How do you write a class without all the repetitive code? In this chapter we compare a hand-written class with a dataclass: automatic init, a readable display and field-by-field equality. We add defaults and field(default_factory=list), meet the real error that protects you from a shared mutable default, freeze an object with frozen=True, make modified copies with replace, convert to a dictionary with asdict, sort with order=True, and validate in __post_init__. The result is a cleaner Transaction for Pocket Ledger.

## Files

- `transaction_dc.py`

## Run it

From this folder:

```bash
uv run transaction_dc.py
```

Tested with Python 3.15.1 and uv 0.13.5.
