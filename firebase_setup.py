import firebase_admin
from firebase_admin import credentials, firestore
import os

# ✅ Build absolute path safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(BASE_DIR, "serviceAccountKey.json")

if not os.path.exists(cred_path):
    raise FileNotFoundError(f"Firebase credentials not found at: {cred_path}")

cred = credentials.Certificate(cred_path)

# ✅ Initialize Firebase only once
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# ✅ Create Firestore client
db = firestore.client()
