RULES = [
    ("food", ("coffee", "cafe", "lunch", "grocer")),
    ("housing", ("rent",)),
    ("health", ("gym", "pharmacy")),
    ("income", ("salary",)),
]


def categorize(description: str) -> str:
    text = description.lower()
    for category, words in RULES:
        if any(word in text for word in words):
            return category
    return "other"
