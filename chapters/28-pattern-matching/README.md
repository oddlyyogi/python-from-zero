# Chapter 28: Pattern Matching: A Command Parser

How do you read commands like 'add 4.50 coffee' without a pile of if statements and index numbers? In this chapter we learn match and case: literal patterns, the | for 'or', the _ wildcard, sequence patterns that unpack values such as ['add', amount, *words], guards with if, and dictionary patterns. We also hit the classic capture trap, where a bare name in a case matches everything, and read the real SyntaxError. The result is the command parser for Pocket Ledger.

## Files

- `commands.py`

## Run it

From this folder:

```bash
uv run commands.py
```

Tested with Python 3.15.1 and uv 0.13.5.
