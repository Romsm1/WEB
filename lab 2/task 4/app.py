from fastapi import FastAPI
from models import User, Feedback

app = FastAPI()
feedbacks = []

user = User(name="John Doe", age=9)
users_list = [user]


@app.get("/users")
def get_users():
    return {
        "users": users_list,
        "count": len(users_list)
    }


@app.post("/user")
def check_user_age(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.age >= 18
    }


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
