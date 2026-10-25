# /// script
# dependencies = ["fastapi", "uvicorn", "pydantic"]
# ///
import uvicorn
from fastapi import FastAPI
from models import Transaction

app = FastAPI()
LEDGER = []


@app.post("/transactions", status_code=201)
def add(transaction: Transaction):
    LEDGER.append(transaction)
    return transaction


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
