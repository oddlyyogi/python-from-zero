# Chapter 46: asyncio: Concurrent Rate Fetching

How can one program wait for many things at once? Think of a waiter looking after many tables. In this chapter we learn asyncio: async def and await, asyncio.run, the difference between awaiting calls one after another (2 seconds) and asyncio.gather (1 second), then real HTTP calls with httpx.AsyncClient to a deliberately slow test server: four exchange rates one by one (2.4 seconds) versus together (0.5 seconds). We add asyncio.timeout and talk about the two classic mistakes: forgetting await, and blocking calls. All timings are real, for Pocket Ledger.

## Files

- `basics.py`
- `rates_async.py`
- `slow_server.py`

## Run it

From this folder:

```bash
uv run basics.py
```

```bash
uv run rates_async.py
```

```bash
uv run slow_server.py
```

Tested with Python 3.15.1 and uv 0.13.5.
