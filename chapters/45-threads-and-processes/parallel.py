import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def read_file(name):
    time.sleep(0.5)
    return f"{name}: 120 rows"

names = ["jan.csv", "feb.csv", "mar.csv", "apr.csv", "may.csv"]

start = time.perf_counter()
results = [read_file(n) for n in names]
print(f"one at a time: {time.perf_counter() - start:.2f}s")

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(read_file, names))
print(f"five threads:  {time.perf_counter() - start:.2f}s")
print(results[0])

with ThreadPoolExecutor(max_workers=5) as pool:
    futures = {pool.submit(read_file, n): n for n in names}
    for future in as_completed(futures):
        print("done:", futures[future], future.result())
