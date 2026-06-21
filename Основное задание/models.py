from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import Optional


class Book(BaseModel):
    slug: str
    title: str
    author: str
    isbn: str
    year: int
    genre: Optional[str] = Field(default=None)

    @field_validator("isbn")
    @classmethod
    def isbn_validator(cls, value: str) -> str:
        cleaned_isbn = value.replace("-", "")
        if not cleaned_isbn or len(cleaned_isbn) != 13:
            raise ValueError("ISBN должен содержать 13 цифр ^_^")
        return cleaned_isbn

    @field_validator("year")
    @classmethod
    def year_validator(cls, value: int) -> int:
        if not (1800 <= value <= 2026):
            raise ValueError("Год издания должен быть в диапазоне от 1800 до 2026 !!!")
        return value


class BookCreate(Book):
    pass


if __name__ == "__main__":
    print("Демонстрация с корректными данными:")
    try:
        my_book = BookCreate(
            slug="мод",
            title="Модели",
            author="Герман Найт",
            isbn="йцфыячсвукаи1",
            year=2020,
            genre="Наука"
        )
        print(my_book)

    except ValidationError as e:
        print(e)

    print("\n Демонстрация с некорректными данными *_*")
    try:
        my_book = BookCreate(
            slug="мод",
            title="Модели",
            author="Герман Найт",
            isbn="121322313йцфыячсвукаи1",
            year=222220222222220,
            genre="Наука"
        )
        print(my_book)

    except ValidationError as e:
        print(e)
