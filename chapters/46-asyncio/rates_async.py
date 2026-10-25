# /// script
# dependencies = ["httpx"]
# ///
import asyncio
import time

import httpx

BASE = "http://127.0.0.1:8766/rate/"
CODES = ["EUR", "GBP", "JPY", "CAD"]


async def fetch(client, code):
    response = await client.get(BASE + code)
    return response.json()["rate"]


async def sequential():
    async with httpx.AsyncClient() as client:
        return [await fetch(client, code) for code in CODES]


async def concurrent():
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(*(fetch(client, code) for code in CODES))


async def with_timeout():
    async with asyncio.timeout(0.2):
        async with httpx.AsyncClient() as client:
            return await fetch(client, "EUR")


for label, make in (("one by one", sequential), ("together", concurrent)):
    start = time.perf_counter()
    rates = asyncio.run(make())
    print(f"{label}: {time.perf_counter() - start:.2f}s {rates}")

try:
    asyncio.run(with_timeout())
except TimeoutError:
    print("too slow")
