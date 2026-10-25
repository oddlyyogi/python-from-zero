# Chapter 42: Automation With subprocess

How can a Python program run other programs and automate chores? Imagine an assistant who can pick up the phone. In this chapter we use subprocess.run with a list of arguments, capture output and read return codes, make failures loud with check=True (and read the real CalledProcessError), then build a timestamped zip backup with shutil.make_archive and inspect it with unzip. We see the real danger of shell=True, use timeouts, and talk about scheduling with cron. All runs are real, for Pocket Ledger.

## Files

- `backup.py`

## Run it

From this folder:

```bash
uv run backup.py
```


## Notes

Create the sample folder first (a `data/` folder is included here). The last lines run a command with a timeout, which ends with `TimeoutExpired` on purpose.


## Practice

Try these on your own copy of the files:

1. Keep only the five newest backups.
2. Run `ls -l` from Python and print the sizes.
3. Add a timeout to every command you run.

Tested with Python 3.15.1 and uv 0.13.5.
