import os
import tomllib
from dataclasses import dataclass
from pathlib import Path

DEFAULTS = {"currency": "USD", "budget": 2000.0}


@dataclass(frozen=True)
class Settings:
    currency: str
    budget: float
    api_key: str | None


def load_settings(path="config.toml"):
    values = dict(DEFAULTS)
    file = Path(path)
    if file.exists():
        with file.open("rb") as f:
            values.update(tomllib.load(f).get("ledger", {}))
    if "LEDGER_CURRENCY" in os.environ:
        values["currency"] = os.environ["LEDGER_CURRENCY"]
    if "LEDGER_BUDGET" in os.environ:
        values["budget"] = float(os.environ["LEDGER_BUDGET"])
    return Settings(values["currency"], values["budget"], os.environ.get("LEDGER_API_KEY"))


settings = load_settings()
print(settings.currency, settings.budget)
print("key set:", settings.api_key is not None)
if settings.api_key:
    print("starts with:", settings.api_key[:3] + "...")
