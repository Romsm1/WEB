from fastapi import FastAPI, HTTPException
from models import Feedback

app = FastAPI()
feedbacks = []

@app.post("/feedback")
def create_feedback(feedback: Feedback):
    feedbacks.append({
        "name": feedback.name,
        "message": feedback.message
    })
    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }

@app.get("/feedbacks")
def get_feedbacks():
    return {
        "feedbacks": feedbacks,
        "count": len(feedbacks)
    }