LABEL = 20
NUMW = 10
WIDTH = LABEL + NUMW
shop = "Corner Cafe"
latte = 5.25
muffin = 3.25
tip_rate = 0.15

subtotal = latte + muffin
tip = subtotal * tip_rate
total = subtotal + tip

print(f"{shop:^{WIDTH}}")
print("-" * WIDTH)
print(f"{'Latte':<{LABEL}}{latte:>{NUMW}.2f}")
print(f"{'Muffin':<{LABEL}}{muffin:>{NUMW}.2f}")
print("-" * WIDTH)
print(f"{'Subtotal':<{LABEL}}{subtotal:>{NUMW}.2f}")
print(f"{'Tip (15%)':<{LABEL}}{tip:>{NUMW}.2f}")
print(f"{'Total':<{LABEL}}{total:>{NUMW}.2f}")
