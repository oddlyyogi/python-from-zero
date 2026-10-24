from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")

def money(value):
    return Decimal(str(value)).quantize(CENT, ROUND_HALF_UP)

def percent(amount, rate):
    return money(amount * Decimal(rate))

subtotal = money(8.5)
tip = percent(subtotal, "0.15")
total = subtotal + tip
print("Subtotal", subtotal)
print("Tip", tip)
print("Total", total)

def split(total, parts):
    cents = int(total * 100)
    base, extra = divmod(cents, parts)
    shares = []
    for i in range(parts):
        shares.append(Decimal(base + (1 if i < extra else 0)) / 100)
    return shares

shares = split(Decimal("100"), 3)
print(shares)
print(sum(shares))
