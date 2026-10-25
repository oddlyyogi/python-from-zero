# Chapter 40: Validation With Pydantic

How do you make sure bad data is stopped at the gate, like a passport check at an airport? In this chapter we describe a Transaction with Pydantic: type hints that convert text into real dates and floats, ValidationError that collects every problem, Field constraints, field validators with our own rules (no zero amounts, known categories), defaults, model_dump and model_validate_json, and finally the model at the door of a FastAPI route, where a bad request gets a real 422 answer. Everything is a real run, for Pocket Ledger.

## Files

- `models.py`
- `api.py`

## Run it

From this folder:

```bash
uv run models.py
```

```bash
uv run api.py
```


## Notes

`uv run api.py` starts a small server on port 8000 that uses the model from `models.py`.


## Practice

Try these on your own copy of the files:

1. Add a `max_length` to the description.
2. Validate that the date is not in the future.
3. Parse a JSON list of transactions with `model_validate_json`.

Tested with Python 3.15.1 and uv 0.13.5.
