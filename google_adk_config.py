import google.generativeai as genai
import os

def get_ai_model():
    # Set up your API key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    return genai.GenerativeModel("gemini-1.5-flash")
