from fastapi import FastAPI, HTTPException
import crud
from models import Transaction

app = FastAPI()


@app.get("/transactions/")
def read_transactions():
    return crud.get_transactions()

@app.get("/transactions/{transaction_id}")
def read_transaction(transaction_id: str):
    transaction = crud.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.post("/transactions/")
def create_transaction(transaction: Transaction):
    transaction_id = crud.add_transaction(transaction.dict())
    return {"id": transaction_id}

@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: str):
    if not crud.get_transaction(transaction_id):
        raise HTTPException(status_code=404, detail="Transaction not found")
    crud.delete_transaction(transaction_id)
    return {"message": "Transaction deleted"}