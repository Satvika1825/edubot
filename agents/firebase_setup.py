import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize the Firebase app (only once)
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
