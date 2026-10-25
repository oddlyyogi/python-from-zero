import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def count_primes(limit):
    count = 0
    for n in range(2, limit):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            count += 1
    return count


def timed(label, workers):
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(count_primes, [400_000] * 4))
    print(f"{label}: {time.perf_counter() - start:.2f}s")


print("GIL enabled:", sys._is_gil_enabled())
timed("one thread ", 1)
timed("four threads", 4)

counter = 0


def bump():
    global counter
    for _ in range(500_000):
        counter += 1

threads = [threading.Thread(target=bump) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("expected 2000000, got", counter)
