from pydantic import BaseModel, Field, field_validator
import re


class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def validate_message(cls, message: str) -> str:
        forbidden_bases = ["редиск", "бяк", "козявк"]
        message_lower = message.lower()

        for base in forbidden_bases:
            if re.search(rf'\b{base}[\w]*\b', message_lower):
                raise ValueError("Использование недопустимых слов")

        return message