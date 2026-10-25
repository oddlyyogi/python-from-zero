import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def count_primes(limit):
    count = 0
    for n in range(2, limit):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            count += 1
    return count


def timed(label, pool_class):
    start = time.perf_counter()
    with pool_class(max_workers=4) as pool:
        results = list(pool.map(count_primes, [400_000] * 4))
    print(f"{label}: {time.perf_counter() - start:.2f}s  {results[0]}")


if __name__ == "__main__":
    start = time.perf_counter()
    [count_primes(400_000) for _ in range(4)]
    print(f"one at a time: {time.perf_counter() - start:.2f}s")
    timed("four threads", ThreadPoolExecutor)
    timed("four processes", ProcessPoolExecutor)
