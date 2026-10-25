# Chapter 41: Configuration and Secrets

How do you change a program's settings without changing its code, and how do you keep passwords and API keys safe? In this chapter we read environment variables with os.environ and os.getenv, read a TOML config file with the standard tomllib, and write a layered loader where defaults, the file and the environment override each other in that order. We keep a demo secret in a .env file that git ignores, load it with uv run --env-file, never print the secret, and meet the secrets module. Every run is real, for Pocket Ledger.

## Files

- `settings.py`
- `config.toml`

## Run it

From this folder:

```bash
uv run settings.py
```


## Notes

Create the demo secret yourself: `echo 'LEDGER_API_KEY=demo-key-123456' > .env`, then `uv run --env-file .env settings.py`. Never commit a real `.env` file.


## Practice

Try these on your own copy of the files:

1. Add a `LEDGER_DB` setting and use it.
2. Make a missing API key a clear error message.
3. Generate a token with `secrets.token_urlsafe`.

Tested with Python 3.15.1 and uv 0.13.5.
