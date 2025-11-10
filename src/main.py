from fastapi import FastAPI
from src.api.routes import router

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title="Alo AI API",
    version="1.0.0",
    description="Open API sederhana yang menghubungkan ke Google Gemini."
)

# Tambahkan route utama
app.include_router(router)

@app.get("/")
def home():
    """
    Root endpoint untuk mengecek apakah API berjalan.
    """
    return {"message": "Welcome to Alo AI API — powered by Gemini 2.5 Pro!"}
