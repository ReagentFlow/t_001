import firebase_admin
from firebase_admin import credentials, db, firestore
from firebase_admin.db import Reference
from uuid import uuid4

cred = credentials.Certificate('private.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc = db.collection("reagents").document("H20")
doc.set({'name': 'H20', 'weight': 43, 'value': 430, 'status': 'GREEN'})
'''

cred = credentials.Certificate("private_key.json")
firebase_admin.initialize_app(cred, {
    'dadtabaseURL': 'https://rf-db-5d5f4-default-rtdb.europe-west1.firebasedatabase.app/'
})


def get_ref(path: int = None) -> Reference:
    if path:
        return db.reference(f"/{path}", url="https://rf-db-5d5f4-default-rtdb.europe-west1.firebasedatabase.app/")
    return db.reference("/", url="https://rf-db-5d5f4-default-rtdb.europe-west1.firebasedatabase.app/")
'''