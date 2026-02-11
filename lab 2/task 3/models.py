from pydantic import BaseModel


class Feedback(BaseModel):
    name: str
    message: str

class User(BaseModel):
    name: str
    age: int
