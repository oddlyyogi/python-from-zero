def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def run(line):
    match line.split():
        case ["add", amount, *words] if is_number(amount) and words:
            return f"added {amount} for {' '.join(words)}"
        case ["add", *_]:
            return "usage: add AMOUNT DESCRIPTION"
        case ["remove", index]:
            return f"removed item {index}"
        case ["list"]:
            return "listing all"
        case ["total"] | ["total", "all"]:
            return "total of everything"
        case ["total", category]:
            return f"total for {category}"
        case []:
            return "empty command"
        case _:
            return f"unknown command: {line}"


for line in [
    "add 4.50 coffee",
    "add 12 lunch with friends",
    "remove 2",
    "list",
    "total",
    "total food",
    "hello there",
    "add banana lunch",
    "add",
]:
    print(f"{line!r:<28} -> {run(line)}")


def describe(record):
    match record:
        case {"type": "expense", "amount": amount}:
            return f"expense of {amount}"
        case {"type": "income", "amount": amount}:
            return f"income of {amount}"
        case _:
            return "unknown record"
print(describe({"type": "expense", "amount": 4.5, "note": "x"}))
print(describe({"type": "income", "amount": 3200}))
print(describe({"hello": 1}))
