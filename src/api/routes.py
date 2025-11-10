from fastapi import APIRouter
from pydantic import BaseModel
from src.services.gemini_client import get_gemini_response

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/chat")
def chat_with_gemini(request: PromptRequest):
    """
    Endpoint utama untuk mengirim prompt ke Gemini.
    """
    response = get_gemini_response(request.prompt)
    return {"response": response}
