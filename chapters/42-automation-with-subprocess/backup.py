import shutil
import subprocess
from datetime import datetime
from pathlib import Path


def make_backup(source, destination):
    destination = Path(destination)
    destination.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive = shutil.make_archive(str(destination / f"ledger-{stamp}"), "zip", source)
    return Path(archive)


archive = make_backup("data", "backups")
print(archive)
subprocess.run(["unzip", "-l", str(archive)], check=True)

name = "x; echo INJECTED"
subprocess.run(f"echo {name}", shell=True)

subprocess.run(["sleep", "5"], timeout=1)
