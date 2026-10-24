import argparse
import json
from pathlib import Path

FILE = Path("ledger.json")


def load():
    return json.loads(FILE.read_text()) if FILE.exists() else []


def cmd_add(args):
    items = load()
    items.append({"amount": args.amount, "description": args.description, "category": args.category})
    FILE.write_text(json.dumps(items, indent=2))
    print(f"added {args.description}: {args.amount:.2f} ({args.category})")


def cmd_list(args):
    for number, item in enumerate(load(), start=1):
        print(f"{number}. {item['description']:<12}{item['amount']:>9.2f}  {item['category']}")

def build_parser():
    parser = argparse.ArgumentParser(prog="ledger", description="A tiny expense ledger")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add", help="add an expense")
    add.add_argument("amount", type=float)
    add.add_argument("description")
    add.add_argument("--category", choices=["food", "housing", "health", "other"], default="other")
    add.set_defaults(func=cmd_add)
    lst = sub.add_parser("list", help="list all expenses")
    lst.set_defaults(func=cmd_list)
    return parser

def main(argv=None):
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
