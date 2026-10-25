# /// script
# dependencies = ["fastapi", "uvicorn"]
# ///
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="Pocket Ledger API")
TRANSACTIONS = [
    {"id": 1, "description": "Coffee", "amount": -4.5, "category": "food"},
    {"id": 2, "description": "Rent", "amount": -900.0, "category": "housing"},
]



@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/transactions")
def list_transactions(category: str | None = None):
    if category is None:
        return TRANSACTIONS
    return [t for t in TRANSACTIONS if t["category"] == category]


@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: int):
    for t in TRANSACTIONS:
        if t["id"] == transaction_id:
            return t
    raise HTTPException(status_code=404, detail="transaction not found")


@app.post("/transactions", status_code=201)
def add_transaction(item: dict):
    item["id"] = len(TRANSACTIONS) + 1
    TRANSACTIONS.append(item)
    return item


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
