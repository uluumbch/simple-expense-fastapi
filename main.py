from fastapi import FastAPI, HTTPException
import crud
from models import Transaction

app = FastAPI(
    title="Transactions API",
    description="A simple API to manage transactions",
    version="0.1"
)


@app.get("/transactions/", summary="Read all Transactions")
def read_transactions():
    return crud.get_transactions()

@app.get("/transactions/{transaction_id}", summary="Read Transaction by ID")
def read_transaction(transaction_id: str):
    transaction = crud.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.post("/transactions/", summary="Create a Transaction")
def create_transaction(transaction: Transaction):
    transaction_id = crud.add_transaction(transaction.dict())
    return {"id": transaction_id}

@app.put("/transactions/{transaction_id}", summary="Update a Transaction")
def update_transaction(transaction_id: str, transaction: Transaction):
    if not crud.get_transaction(transaction_id):
        raise HTTPException(status_code=404, detail="Transaction not found")
    crud.update_transaction(transaction_id, transaction.dict())
    return {"message": "Transaction updated"}


@app.delete("/transactions/{transaction_id}", summary="Delete a Transaction")
def delete_transaction(transaction_id: str):
    if not crud.get_transaction(transaction_id):
        raise HTTPException(status_code=404, detail="Transaction not found")
    crud.delete_transaction(transaction_id)
    return {"message": "Transaction deleted"}

@app.get("/balance/", summary="Get Balance")
def get_balance():
    return {"balance": crud.get_balance()}
