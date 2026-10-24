from contextlib import contextmanager, suppress
from pathlib import Path
from tempfile import TemporaryDirectory

class Announce:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"start {self.name}")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"end {self.name}")
        return False


with Announce("import"):
    print("working")


@contextmanager
def announce(name):
    print(f"start {name}")
    try:
        yield
    finally:
        print(f"end {name}")


with announce("report"):
    print("working")


@contextmanager
def atomic_write(path):
    tmp = Path(str(path) + ".tmp")
    try:
        with tmp.open("w", encoding="utf-8") as f:
            yield f
        tmp.replace(path)
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise


Path("ledger.txt").write_text("old data\n")
try:
    with atomic_write(Path("ledger.txt")) as f:
        f.write("new line one\n")
except RuntimeError:
    print("crashed")
print(Path("ledger.txt").read_text())


with suppress(FileNotFoundError):
    Path("missing.txt").unlink()


with TemporaryDirectory() as d:
    p = Path(d) / "a.txt"
    p.write_text("x")
    print(p.exists())
print(p.exists())
