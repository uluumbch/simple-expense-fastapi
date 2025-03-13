import firebase_admin
from firebase_admin import credentials, firestore

# Initiate firebase app
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
transactions_ref = db.collection("transactions")



def get_transactions():
    return [doc.to_dict() for doc in transactions_ref.stream()]
