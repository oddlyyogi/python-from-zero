import uvicorn
from fastapi import FastAPI

from . import store

app = FastAPI(title="Pocket Ledger")


@app.get("/totals")
def totals() -> dict[str, str]:
    return {
        name: str(total)
        for name, total in store.totals_by_category(store.connect()).items()
    }


def serve() -> None:
    uvicorn.run(app, port=8000)
