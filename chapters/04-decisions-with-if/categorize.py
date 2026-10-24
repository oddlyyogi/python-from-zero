description = "gym membership"
amount = 30

if "coffee" in description or "cafe" in description:
    category = "Food & Drink"
elif "rent" in description:
    category = "Housing"
elif amount > 100:
    category = "Large purchase"
else:
    category = "Other"

print(f"{description}: {category}")
