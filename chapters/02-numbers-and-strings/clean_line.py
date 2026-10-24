raw = "  MONTHLY RENT   $900.00 "
text = raw.strip()
parts = text.split()
amount = float(parts[-1].replace("$", ""))
name = " ".join(parts[:-1]).title()
print(f"{name}: ${amount:.2f}")
