import sys
lazy import statistics
from money import format_money, add_tax

print(format_money(add_tax(50)))

amounts = [4.5, 3.25, 12]
print("loaded at start:", "statistics" in sys.modules)
print(statistics.mean(amounts))
print("loaded after use:", "statistics" in sys.modules)
