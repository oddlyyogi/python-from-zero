def parse_amount(text):
    cleaned = text.strip().replace("$", "").replace(",", "")
    if cleaned == "":
        raise ValueError("empty amount")
    return float(cleaned)

def average(amounts):
    try:
        return sum(amounts) / len(amounts)
    except ZeroDivisionError:
        return 0.0

inputs = ["$4.50", "1,234.50", "-20", "abc", ""]
good = []
for text in inputs:
    try:
        good.append(parse_amount(text))
    except ValueError as error:
        print(f"skipping {text!r}: {error}")
print(good)
print(f"average: {average(good):.2f}")
print(f"average of nothing: {average([]):.2f}")
