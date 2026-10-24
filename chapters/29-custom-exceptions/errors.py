class LedgerError(Exception):
    """Base class for every error this ledger raises."""


class InvalidAmount(LedgerError):
    def __init__(self, value):
        super().__init__(f"not a valid amount: {value!r}")
        self.value = value


class UnknownCategory(LedgerError):
    pass


CATEGORIES = {"food", "housing", "health"}


def parse_entry(line):
    amount_text, category = line.split()
    try:
        amount = float(amount_text)
    except ValueError as error:
        raise InvalidAmount(amount_text) from None
    if category not in CATEGORIES:
        raise UnknownCategory(f"unknown category: {category}")
    return amount, category


for line in ["4.50 food", "abc food", "12 pets"]:
    try:
        print(parse_entry(line))
    except InvalidAmount as error:
        print("bad amount:", error.value)
    except LedgerError as error:
        print("ledger problem:", error)

try:
    parse_entry("abc food")
except InvalidAmount as error:
    error.add_note("seen while importing line 3")
    raise
