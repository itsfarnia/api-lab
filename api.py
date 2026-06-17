from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title = 'API LAB')

class TextRequest(BaseModel):
    text : str

class QuestionRequest(BaseModel):
    question: str

class FeedbackRequest(BaseModel):
    name : str
    message : str
    rating : str

@app.get("/health")
def health():
    return {
        "status" : "ok",
        "message" : "API is running."
    }

@app.post("/summarize")
def summarize(request:TextRequest):
    text = request.text.lower().strip()

    if not text:
        raise HTTPException(status_code = 400, detail="Text cannot be empty.")
    
    if "refund" in text or "payment" in text or "invoice" in text:
        category = "billing"
    elif "password" in text or "login" in text or "account" in text:
        category = "account"
    elif "shipping" in text or "delivery" in text or "order" in text:
        category = "shipping"
    else:
        category = "general"  

    return {
        "text" : request.text,
        "category" : category
    }

@app.post("/ask")
def ask(request:QuestionRequest):
    question = request.question.lower().strip()

    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    if "refund" in question:
        answer = "Customers can request a refund within 30 days of purchase."
    elif "shipping" in question or "delivery" in question:
        answer = "Standard shipping usually takes 3 to 5 business days."
    elif "password" in question:
        answer = "Users can reset their password from the login page."
    else:
        answer = "I do not have enough information to answer this question."

    return {
        "question": request.question,
        "answer": answer
    }
@app.post("/feedback")
def feedback(request : FeedbackRequest):
    if request.rating < 1 or request.rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")

    return {
        "message" : "Feedback Received.",
        "feedback": {
            "name" : request.name,
            "message" : request.message,
            "rating" : request.rating
        }
    }
