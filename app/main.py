from fastapi import FastAPI
from app.model import predict_email_category, load_model
from app.schemas import EmailRequest, EmailResponse
import asyncio

app = FastAPI(title="Email Classification API", version="1.0.0")

@app.on_event("startup")
def startup_event():
    load_model()

@app.get("/")
async def root():
    return {"message": "Email Classification API"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/classify", response_model=EmailResponse)
async def classify_email(request: EmailRequest):
    predicted_category, confidence = await asyncio.to_thread(
        predict_email_category, request.email_text
    )
    return EmailResponse(predicted_category=predicted_category, confidence=float(confidence))
