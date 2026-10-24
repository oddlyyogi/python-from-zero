import argparse


def main():
    parser = argparse.ArgumentParser(prog="ledger", description="Pocket Ledger")
    parser.add_argument("amount", type=float)
    parser.add_argument("description")
    args = parser.parse_args()
    print(f"added {args.description}: {args.amount:.2f}")
