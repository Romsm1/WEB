from fastapi import FastAPI
from models import Feedback

app = FastAPI()
feedback_list = []

@app.post("/feedback")
def add_feedback(feedback: Feedback):
    feedback_list.append({
        "name": feedback.name,
        "message": feedback.message
    })
    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }

@app.get("/feedbacks")
def get_feedbacks():
    return {
        "feedbacks": feedback_list,
        "count": len(feedback_list)
    }