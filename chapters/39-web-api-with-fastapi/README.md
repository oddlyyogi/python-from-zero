# Chapter 39: A Web API With FastAPI

How can other programs use your ledger over the network? Think of a menu for programs: routes, methods and answers in JSON. In this chapter we build a web API with FastAPI and uvicorn, step by step: a health route, a list with a query parameter filter, a path parameter route with a real 404, a POST route that adds data and returns 201, and the automatic OpenAPI description. We start the real server and call it with curl, so every response you see is real. This is the web interface of Pocket Ledger.

## Files

- `app.py`

## Run it

From this folder:

```bash
uv run app.py
```


## Notes

`uv run app.py` starts the server on port 8000. Call it from a second terminal with `curl`, for example `curl -s localhost:8000/transactions`.


## Practice

Try these on your own copy of the files:

1. Add a `DELETE /transactions/{id}` route.
2. Return a 422 for a negative id.
3. Open `/docs` in a browser and try a request there.

Tested with Python 3.15.1 and uv 0.13.5.
