from fastapi import FastAPI
import crud

app = FastAPI()


@app.get("/transactions/")
def read_transactions():
    return crud.get_transactions()