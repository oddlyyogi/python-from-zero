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


## Notes

The script talks to a tiny local server. Start it first, in a second terminal: `cd site && python3 -m http.server 8765`, then run `uv run rates.py`.


## Practice

Try these on your own copy of the files:

1. Fetch another currency from the local server.
2. Add a retry when the request times out.
3. Print the response headers.

Tested with Python 3.15.1 and uv 0.13.5.
