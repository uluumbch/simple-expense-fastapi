from fastapi import FastAPI
import crud
from models import Transaction

app = FastAPI()


@app.get("/transactions/")
def read_transactions():
    return crud.get_transactions()

@app.post("/transactions/")
def create_transaction(transaction: Transaction):
    transaction_id = crud.add_transaction(transaction.dict())
    return {"id": transaction_id}