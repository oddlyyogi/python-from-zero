import json
from abc import ABC, abstractmethod
from typing import Protocol

class Importer(ABC):
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} importer"

    @abstractmethod
    def parse(self, text):
        raise NotImplementedError


class Parser(Protocol):
    def parse(self, text): ...


class CsvImporter(Importer):
    def __init__(self):
        super().__init__("CSV")

    def parse(self, text):
        rows = []
        for line in text.splitlines():
            date, description, amount = line.split(",")
            rows.append((date, description, float(amount)))
        return rows


class JsonImporter(Importer):
    def __init__(self):
        super().__init__("JSON")

    def parse(self, text):
        items = json.loads(text)
        return [(i["date"], i["description"], i["amount"]) for i in items]


class LinesImporter:
    def parse(self, text):
        return [("?", line, 0.0) for line in text.splitlines() if line]


CSV_TEXT = "2026-10-01,Coffee,-4.50\n2026-10-02,Salary,3200.00"
JSON_TEXT = '[{"date": "2026-10-03", "description": "Rent", "amount": -900.0}]'
pairs = [(CsvImporter(), CSV_TEXT), (JsonImporter(), JSON_TEXT), (LinesImporter(), "Coffee\n\nRent")]
for importer, sample in pairs:
    print(type(importer).__name__, importer.parse(sample))
