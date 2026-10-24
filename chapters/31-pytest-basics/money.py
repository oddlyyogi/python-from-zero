def format_money(amount):
    return f"${amount:,.2f}"


def add_tax(amount, rate=0.08):
    return amount * (1 + rate)


def split_bill(total, people):
    cents = round(total * 100)
    each, leftover = divmod(cents, people)
    return each / 100, leftover
