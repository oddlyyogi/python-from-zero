import asyncio
import time


async def greet(name, delay):
    await asyncio.sleep(delay)
    print("hello", name)


async def main():
    await asyncio.gather(greet("a", 1), greet("b", 1))


start = time.perf_counter()
asyncio.run(main())
print(f"total: {time.perf_counter() - start:.1f}s")
