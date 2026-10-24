# Chapter 32: pytest: Fixtures and Parametrize

How do you test one function against many inputs without copying and pasting, and how do you prepare sample data for tests? In this chapter we write a small CSV importer and test it with pytest: first the copy-and-paste way, then @pytest.mark.parametrize with a list of cases, parametrized error tests with pytest.raises, a fixture that builds a sample file in tmp_path, and the xfail mark for a known gap. Everything is typed live and run for real, as a test suite for the Pocket Ledger importer.

## Files

- `importer.py`
- `test_importer.py`

## Run it

From this folder:

```bash
uv run --with pytest pytest -v
```

```bash
uv run importer.py
```

Tested with Python 3.15.1 and uv 0.13.5.
