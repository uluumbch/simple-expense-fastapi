import firebase_admin
from firebase_admin import credentials, firestore

# Initiate firebase app
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
transactions_ref = db.collection("transactions")



def get_transactions():
    return [doc.to_dict() for doc in transactions_ref.stream()]

def get_transaction(transaction_id):
    doc = transactions_ref.document(transaction_id).get()
    return doc.to_dict() if doc.exists else None

def add_transaction(transaction_data):
    doc_ref = transactions_ref.document()
    doc_ref.set(transaction_data)
    return doc_ref.id

def delete_transaction(transaction_id):
    transactions_ref.document(transaction_id).delete()
    return True

def update_transaction(transaction_id, transaction_data):
    transactions_ref.document(transaction_id).update(transaction_data)
    return True

def get_balance():
    transactions = get_transactions()
    return sum([transaction["amount"] for transaction in transactions])
