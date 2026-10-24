# ledger_hello.py: the first piece of Pocket Ledger
app = "Pocket Ledger"
opening = 1250.00
rent = 900.00
coffee = 4.50

print(f"Welcome to {app}")
print("Opening balance:", opening)
print("After rent and coffee:", opening - rent - coffee)
