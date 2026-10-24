def format_money(amount):
    """Format an amount as money, for example $1,234.50."""
    return f"${amount:,.2f}"

def add_tax(amount, rate=0.08):
    return amount * (1 + rate)

def split_bill(total, people):
    cents = round(total * 100)
    each, leftover = divmod(cents, people)
    return each / 100, leftover

print(format_money(1234.5))
print(format_money(add_tax(100)))
print(format_money(add_tax(100, rate=0.2)))
each, extra = split_bill(100, 3)
print(f"Each person pays {each}, {extra} cent left over")
help(format_money)
