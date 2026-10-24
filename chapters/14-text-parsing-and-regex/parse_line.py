import re

lines = [
    "03/10/2026  POS PURCHASE  STARBUCKS #1234        -4.50",
    "05/10/2026  ACH CREDIT    ACME PAYROLL        3,200.00",
    "06/10/2026  CHECK 1042    LANDLORD LLC         -900.00",
    "TOTAL FOR PERIOD",
]

PATTERN = re.compile(
    r"^(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})"
    r"\s+(?P<text>.+?)"
    r"\s+(?P<amount>-?[\d,]+\.\d{2})$"
)

for line in lines:
    m = PATTERN.match(line)
    if m is None:
        print(f"skipped: {line}")
        continue
    description = " ".join(m["text"].split())
    amount = float(m["amount"].replace(",", ""))
    date = f"{m['year']}-{m['month']}-{m['day']}"
    print((date, description, amount))
