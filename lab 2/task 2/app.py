from fastapi import FastAPI
from models import User

app = FastAPI()

@app.post("/user")
def user_age(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.age >= 18
    }