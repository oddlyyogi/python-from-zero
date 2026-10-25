# Chapter 38: HTTP Calls With httpx: Exchange Rates

How does a Python program talk to the web? Think of ordering at a restaurant window: request, response, status code. In this chapter we use httpx to fetch exchange rates from a small local server (so the video is repeatable): a script with inline dependencies that uv installs automatically (PEP 723), the response object, timeouts, the real 404 status and HTTPStatusError, the real ConnectError when nothing is listening, a get_rates function that handles failures, and a currency converter for Pocket Ledger.

## Files

- `rates.py`
- `site/rates.json`

## Run it

From this folder:

```bash
uv run rates.py
```

Tested with Python 3.15.1 and uv 0.13.5.
