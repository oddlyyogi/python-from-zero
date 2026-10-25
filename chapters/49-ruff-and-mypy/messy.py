def add_entry(
    entries: list[dict[str, object]] | None = None,
    amount: float = 0,
    note: str | None = None,
) -> list[dict[str, object]]:
    if entries is None:
        entries = []
    if note is None:
        note = ""
    try:
        entries.append({"amount": amount, "note": note})
    except AttributeError:
        print("failed")
    return entries
