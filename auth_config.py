import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- 🔹 Load Environment Variables ---
load_dotenv()

# --- 🔹 Firebase Configuration ---
firebase_config = {
    "apiKey": "AIzaSyDoVzssOtCLr84hXec3zDPK7YJjQNTwxGQ",
    "authDomain": "smart-ai-tutor-158d2.firebaseapp.com",
    "databaseURL": "https://smart-ai-tutor-158d2-default-rtdb.firebaseio.com",
    "projectId": "smart-ai-tutor-158d2",
    "storageBucket": "smart-ai-tutor-158d2.appspot.com",
    "messagingSenderId": "842164354534",
    "appId": "1:842164354534:web:7e7b5b8a2ad36b74aaea27",
    "measurementId": "G-Z85096TNP7"
}

# --- 🔹 Google ADK (Generative AI) Configuration ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # from your .env file

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    print("⚠️ GOOGLE_API_KEY not found in environment variables")

def get_ai_model(model_name="gemini-1.5-pro"):
    """Returns a configured Google Generative AI model"""
    return genai.GenerativeModel(model_name)
