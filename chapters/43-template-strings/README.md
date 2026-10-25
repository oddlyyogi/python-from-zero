# Chapter 43: Template Strings (t-strings): Safe Reports

What if a string could keep its parts separate, so a function decides how to fill the gaps? In this chapter we meet t-strings, the template strings of modern Python: how they differ from f-strings, the Template object with its strings, values and Interpolation parts, a render function that rebuilds text, a render_html function that escapes user input (and the real escaped output), and a to_sql function that turns a template into a parameterised database query. All outputs are real runs on Python 3.15, for Pocket Ledger reports.

## Files

- `safe_report.py`

## Run it

From this folder:

```bash
uv run safe_report.py
```


## Practice

Try these on your own copy of the files:

1. Write a `render_markdown` function for templates.
2. Make `render_html` escape quotes too.
3. Print the interpolations of a template of your own.

Tested with Python 3.15.1 and uv 0.13.5.
