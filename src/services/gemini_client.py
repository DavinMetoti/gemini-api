import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Konfigurasi API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt: str, model_name="models/gemini-2.5-pro") -> str:
    """
    Fungsi untuk mengirim prompt ke Google Gemini API
    dan mengembalikan hasil respons teks.
    """
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Terjadi error: {e}"
