import csv


def parse_amount(text):
    cleaned = text.strip().replace("$", "").replace(",", "")
    return float(cleaned)


def import_csv(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append((row["Date"], row["Description"].strip(), parse_amount(row["Amount"])))
    return rows
