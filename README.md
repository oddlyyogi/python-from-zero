# Python From Zero

[![Python 3.15](https://img.shields.io/badge/python-3.15-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Managed with uv](https://img.shields.io/badge/managed%20with-uv-DE5FE9)](https://docs.astral.sh/uv/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Source code for the **Python From Zero** video course: a practical, live-coding introduction to modern Python (3.15), from your first script to a tested, packaged, web-enabled application.

Every example in the videos is typed and run on screen. This repository holds the exact files from each chapter, so you can run them, change them and break them yourself.

## What you will build

Along the way the chapters build the pieces of **Pocket Ledger**, a small personal expense tracker: parsing messy bank lines, handling money correctly, reading and writing CSV and JSON, storing data in SQLite, a command line tool, a web API, tests, and packaging.

## Getting started

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/), the Python package and project manager used throughout the course.
2. Clone this repository:

   ```bash
   git clone https://github.com/oddlyyogi/python-from-zero.git
   cd python-from-zero
   ```

3. Run any chapter file. uv downloads the right Python version automatically:

   ```bash
   uv run --python 3.15 chapters/01-setup-with-uv-and-your-first-script/hello.py
   ```

Some chapters declare their own third-party dependencies at the top of the script ([PEP 723](https://peps.python.org/pep-0723/)); `uv run` installs them on demand, so there is nothing to set up by hand.

## Chapters

### Part 1: Foundations

| # | Chapter | Code |
|---:|---|---|
| 1 | Setup With uv and Your First Script | [`chapters/01-setup-with-uv-and-your-first-script`](chapters/01-setup-with-uv-and-your-first-script) |
| 2 | Numbers and Strings | [`chapters/02-numbers-and-strings`](chapters/02-numbers-and-strings) |
| 3 | Variables, Types and f-strings | [`chapters/03-variables-types-and-f-strings`](chapters/03-variables-types-and-f-strings) |
| 4 | Decisions With if | [`chapters/04-decisions-with-if`](chapters/04-decisions-with-if) |
| 5 | Loops: for, while, break and continue | [`chapters/05-loops`](chapters/05-loops) |
| 6 | Lists and Tuples | [`chapters/06-lists-and-tuples`](chapters/06-lists-and-tuples) |
| 7 | Dictionaries and Sets | [`chapters/07-dicts-and-sets`](chapters/07-dicts-and-sets) |
| 8 | Functions: Reusable Money Helpers | [`chapters/08-functions`](chapters/08-functions) |
| 9 | Errors and Exceptions: A Safe Amount Parser | [`chapters/09-errors-and-exceptions`](chapters/09-errors-and-exceptions) |
| 10 | Modules and Imports | [`chapters/10-modules-and-imports`](chapters/10-modules-and-imports) |

### Part 2: Data and files

| # | Chapter | Code |
|---:|---|---|
| 11 | Files and pathlib: Save and Load | [`chapters/11-files-and-pathlib`](chapters/11-files-and-pathlib) |
| 12 | CSV Files: Import a Bank Export | [`chapters/12-csv-files`](chapters/12-csv-files) |
| 13 | JSON: Export and Backup | [`chapters/13-json`](chapters/13-json) |
| 14 | Text Parsing and Regular Expressions | [`chapters/14-text-parsing-and-regex`](chapters/14-text-parsing-and-regex) |
| 15 | Dates and Times: Group by Month | [`chapters/15-dates-and-times`](chapters/15-dates-and-times) |
| 16 | Decimal and Money | [`chapters/16-decimal-and-money`](chapters/16-decimal-and-money) |
| 17 | Comprehensions and Generators | [`chapters/17-comprehensions-and-generators`](chapters/17-comprehensions-and-generators) |
| 18 | Sorting, Grouping, collections and itertools | [`chapters/18-sorting-grouping-collections-itertools`](chapters/18-sorting-grouping-collections-itertools) |

### Part 3: Structure

| # | Chapter | Code |
|---:|---|---|
| 19 | Classes: A Transaction Class | [`chapters/19-classes`](chapters/19-classes) |
| 20 | Dataclasses: A Cleaner Transaction | [`chapters/20-dataclasses`](chapters/20-dataclasses) |
| 21 | Enums: Safe Categories | [`chapters/21-enums`](chapters/21-enums) |
| 22 | Inheritance and Protocols: Pluggable Importers | [`chapters/22-inheritance-and-protocols`](chapters/22-inheritance-and-protocols) |
| 23 | Type Hints: A Typed Ledger | [`chapters/23-type-hints`](chapters/23-type-hints) |
| 24 | Special Methods: A Ledger You Can Loop Over | [`chapters/24-special-methods`](chapters/24-special-methods) |
| 25 | Decorators: Timing, Caching and Retry | [`chapters/25-decorators`](chapters/25-decorators) |
| 26 | Context Managers: Safe Files and Cleanup | [`chapters/26-context-managers`](chapters/26-context-managers) |
| 27 | Functions in Depth: A Rule Engine | [`chapters/27-functions-in-depth`](chapters/27-functions-in-depth) |

### Part 4: Quality

| # | Chapter | Code |
|---:|---|---|
| 28 | Pattern Matching: A Command Parser | [`chapters/28-pattern-matching`](chapters/28-pattern-matching) |
| 29 | Custom Exceptions: Clear Ledger Errors | [`chapters/29-custom-exceptions`](chapters/29-custom-exceptions) |
| 30 | Logging: An Audit Trail | [`chapters/30-logging`](chapters/30-logging) |
| 31 | pytest Basics: Test the Money Helpers | [`chapters/31-pytest-basics`](chapters/31-pytest-basics) |
| 32 | pytest: Fixtures and Parametrize | [`chapters/32-fixtures-and-parametrize`](chapters/32-fixtures-and-parametrize) |
| 33 | Debugging With print and pdb | [`chapters/33-debugging-with-pdb`](chapters/33-debugging-with-pdb) |
| 34 | Command Line Tools With argparse | [`chapters/34-command-line-argparse`](chapters/34-command-line-argparse) |
| 35 | Packaging With pyproject and uv | [`chapters/35-packaging-with-pyproject-and-uv`](chapters/35-packaging-with-pyproject-and-uv) |

### Part 5: The real world

| # | Chapter | Code |
|---:|---|---|
| 36 | SQLite: Store Transactions in a Database | [`chapters/36-sqlite`](chapters/36-sqlite) |
| 37 | SQL Queries and Migrations | _coming soon_ |
| 38 | HTTP Calls With httpx: Exchange Rates | _coming soon_ |
| 39 | A Web API With FastAPI | _coming soon_ |
| 40 | Validation With Pydantic | _coming soon_ |
| 41 | Configuration and Secrets | _coming soon_ |
| 42 | Automation With subprocess | _coming soon_ |
| 43 | Template Strings (t-strings): Safe Reports | _coming soon_ |
| 44 | Charts: A Spending Chart | _coming soon_ |

### Part 6: Advanced

| # | Chapter | Code |
|---:|---|---|
| 45 | Threads and Processes | _coming soon_ |
| 46 | asyncio: Concurrent Rate Fetching | _coming soon_ |
| 47 | Free-Threaded Python | _coming soon_ |
| 48 | Profiling and Speed | _coming soon_ |
| 49 | Static Checks With mypy and ruff | _coming soon_ |
| 50 | Capstone: Assemble Pocket Ledger | _coming soon_ |

## Repository layout

```text
chapters/NN-title/    the files typed in the chapter, each with its own README
.gitignore, LICENSE, README.md
```

## Requirements

- Python 3.15 (the course was recorded with 3.15.1)
- [uv](https://docs.astral.sh/uv/) 0.13 or newer
- macOS, Linux or Windows

## License

Released under the [MIT License](LICENSE).
