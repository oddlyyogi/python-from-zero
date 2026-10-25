# /// script
# dependencies = ["httpx"]
# ///
import httpx

URL = "http://localhost:8765/rates.json"


def get_rates():
    try:
        response = httpx.get(URL, timeout=5)
        response.raise_for_status()
        return response.json()["rates"]
    except httpx.HTTPError as error:
        print("could not fetch rates:", error)
        return {}


def convert(amount, source, target, rates):
    return amount / rates[source] * rates[target]


rates = get_rates()
print(convert(100, "USD", "EUR", rates))
print(convert(100, "EUR", "JPY", rates))
