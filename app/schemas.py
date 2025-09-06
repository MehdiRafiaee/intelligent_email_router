from pydantic import BaseModel, Field

class EmailRequest(BaseModel):
    email_text: str = Field(..., example="Hello, I'd like help with billing...")

class EmailResponse(BaseModel):
    predicted_category: str
    confidence: float = Field(..., ge=0.0, le=1.0)
