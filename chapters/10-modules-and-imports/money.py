def format_money(amount):
    return f"${amount:,.2f}"

def add_tax(amount, rate=0.08):
    return amount * (1 + rate)

if __name__ == "__main__":
    print("money.py self test:", format_money(add_tax(100)))
