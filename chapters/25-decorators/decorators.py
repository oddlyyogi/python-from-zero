import time
from functools import cache, wraps


def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{fn.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


@timed
def slow_sum(n):
    return sum(range(n))


print(slow_sum(5_000_000))
print(slow_sum.__name__)


@cache
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@timed
def run(n):
    return fib(n)


print(run(30))


def retry(times):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return fn(*args, **kwargs)
                except ValueError as error:
                    print(f"attempt {attempt} failed: {error}")
            raise ValueError("all attempts failed")
        return wrapper
    return decorator


calls = {"n": 0}


@retry(3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ValueError("server busy")
    return "success"


print(flaky())
