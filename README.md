# Python From Zero

[![CI](https://github.com/oddlyyogi/python-from-zero/actions/workflows/ci.yml/badge.svg)](https://github.com/oddlyyogi/python-from-zero/actions/workflows/ci.yml)
[![Python 3.15](https://img.shields.io/badge/python-3.15-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Managed with uv](https://img.shields.io/badge/managed%20with-uv-DE5FE9)](https://docs.astral.sh/uv/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Source code and exercises for the **Python From Zero** video course: a practical, live-coding introduction to modern Python (3.15), in 50 chapters, from your first script to a tested, packaged application with a command line tool and a web API.

Every example in the videos is typed and run on screen. This repository holds the exact files from each chapter, so you can run them, change them and break them yourself. Each chapter folder also has a short list of practice exercises.

## Contents

- [Getting started](#getting-started)
- [How to practice](#how-to-practice)
- [Chapters](#chapters)
- [The Pocket Ledger project](#the-pocket-ledger-project)
- [Repository layout](#repository-layout)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Getting started

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/), the Python package and project manager used throughout the course. uv also downloads the right Python version for you.
2. Clone the repository:

   ```bash
   git clone https://github.com/oddlyyogi/python-from-zero.git
   cd python-from-zero
   ```

3. Run your first chapter file:

   ```bash
   cd chapters/01-setup-with-uv-and-your-first-script
   uv run --python 3.15 hello.py
   ```

Some scripts declare their own third-party dependencies at the top ([PEP 723](https://peps.python.org/pep-0723/)), and `uv run` installs them on demand, so there is nothing to set up by hand.

## How to practice

1. Watch a chapter, then open its folder here and run the files yourself.
2. Do not just read them: change a value, break a line on purpose, read the error, and fix it.
3. Finish the **Practice** exercises at the bottom of the chapter README. Work in a copy (for example `cp -r chapters/05-loops ~/practice/05`) so that you can always get back to the original.
4. When you are stuck, compare with the files in the chapter folder, and open an issue if something does not run.

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
| 37 | SQL Queries and Migrations | [`chapters/37-sql-queries-and-migrations`](chapters/37-sql-queries-and-migrations) |
| 38 | HTTP Calls With httpx: Exchange Rates | [`chapters/38-http-with-httpx`](chapters/38-http-with-httpx) |
| 39 | A Web API With FastAPI | [`chapters/39-web-api-with-fastapi`](chapters/39-web-api-with-fastapi) |
| 40 | Validation With Pydantic | [`chapters/40-validation-with-pydantic`](chapters/40-validation-with-pydantic) |
| 41 | Configuration and Secrets | [`chapters/41-configuration-and-secrets`](chapters/41-configuration-and-secrets) |
| 42 | Automation With subprocess | [`chapters/42-automation-with-subprocess`](chapters/42-automation-with-subprocess) |
| 43 | Template Strings (t-strings): Safe Reports | [`chapters/43-template-strings`](chapters/43-template-strings) |
| 44 | Charts: A Spending Chart | [`chapters/44-charts-with-matplotlib`](chapters/44-charts-with-matplotlib) |

### Part 6: Advanced

| # | Chapter | Code |
|---:|---|---|
| 45 | Threads and Processes | [`chapters/45-threads-and-processes`](chapters/45-threads-and-processes) |
| 46 | asyncio: Concurrent Rate Fetching | [`chapters/46-asyncio`](chapters/46-asyncio) |
| 47 | Free-Threaded Python | [`chapters/47-free-threaded-python`](chapters/47-free-threaded-python) |
| 48 | Profiling and Speed | [`chapters/48-profiling-and-speed`](chapters/48-profiling-and-speed) |
| 49 | Static Checks With mypy and ruff | [`chapters/49-ruff-and-mypy`](chapters/49-ruff-and-mypy) |
| 50 | Capstone: Assemble Pocket Ledger | [`chapters/50-capstone-assemble-pocket-ledger`](chapters/50-capstone-assemble-pocket-ledger) |

## The Pocket Ledger project

Along the way the chapters build the pieces of **Pocket Ledger**, a small personal expense tracker. The finished application is in [`pocket-ledger/`](pocket-ledger): it imports a messy bank CSV, handles money exactly, categorises transactions, stores them in SQLite, prints a report, and offers a command line tool and a web API, with tests and static checks.

```bash
cd pocket-ledger
uv run ledger import bank.csv
uv run ledger report
uv run pytest -q
```

## Repository layout

```text
chapters/NN-title/    the files typed in each chapter, with a README and exercises
pocket-ledger/        the finished Pocket Ledger application (chapter 50)
.github/workflows/    continuous integration
```

## Troubleshooting

- **`uv: command not found`**: install uv and open a new terminal.
- **A chapter needs a server** (chapters 38, 39, 40, 46): the chapter README says which command to start first, in a second terminal.
- **Different output on your machine**: timings, memory addresses, dates and random values will differ. That is expected.
- **Older Python**: the code uses Python 3.15 features in places (for example `lazy import` and t-strings). Run it with `uv run --python 3.15`.

## Contributing

Found a typo, a broken example or a better exercise? Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE).
