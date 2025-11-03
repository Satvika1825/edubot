import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Google Generative AI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    print("⚠️ GOOGLE_API_KEY not found in .env file")

class GoogleADKAgent:
    """Unified Google ADK Agent to generate AI responses using Gemini."""
    def __init__(self, model_name="gemini-1.5-pro"):
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str) -> str:
        """Generate text using the Gemini model."""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"⚠️ Error generating response: {e}"
