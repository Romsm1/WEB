from fastapi import FastAPI
from models import User

app = FastAPI()

user = User(name="John Doe", id=1)

user_list = [user]

@app.get("/users")
def get_users():
    return {
        "users": user_list,
        "count": len(user_list)
    }