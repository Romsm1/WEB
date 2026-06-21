from fastapi import FastAPI, HTTPException, Query
import uvicorn
from typing import Optional, List

from models import Book, BookCreate

app = FastAPI(
    title="Library of Books",
    description="REST API for Books",
    version="1.0.0",
)

books_db: dict[str, Book] = {}  # Аннотация типа: ключ (slug) -> значение (Book)


def create_books():
    book1 = Book(
        slug="мод",
        title="Модели",
        author="Герман Найт",
        isbn="йцфыячсвукаи1",
        year=2020,
        genre="Наука"
    )

    book2 = Book(
        slug="тяж",
        title="Тяжесть",
        author="Джимми Уайт",
        isbn="1234567890йцу",
        year=1978,
        genre="Триллер"
    )

    # Сохраняем в словаре, используя slug как ключ
    books_db[book1.slug] = book1
    books_db[book2.slug] = book2


create_books()  # Вызываем функцию предзаполнения


# Получение списка ВСЕХ книг
@app.get("/books/", response_model=List[Book], tags=["Books"])
async def get_books():
    return list(books_db.values())


# Получение книги по фильтру (автор или жанр)
@app.get("/books/filter/", response_model=List[Book], tags=["Books"])
async def filter_books(
        author: Optional[str] = Query(None),
        genre: Optional[str] = Query(None)
):
    # Если оба параметра не переданы, то возвращаем все книги
    if author is None and genre is None:
        return list(books_db.values())

    # Начинаем со всех книг
    result = list(books_db.values())

    # Фильтруем по автору (если параметр передан)
    if author is not None:
        author_lower = author.lower()  # Приводим запрос к нижнему регистру
        result = [
            book for book in result
            if author_lower in book.author.lower()  # Частичное совпадение
        ]

    # Фильтруем по жанру (если параметр передан)
    if genre is not None:
        genre_lower = genre.lower()  # Приводим запрос к нижнему регистру
        result = [
            book for book in result
            if genre_lower in book.genre.lower()  # Частичное совпадение
        ]
    return result


# Получение книги по идентификатору (slug)
@app.get("/books/{slug}", response_model=Book, summary="Get book by slug", tags=["Books"])
async def get_book_by_slug(slug: str):
    book = books_db[slug]
    if book is None:
        raise HTTPException(status_code=404, detail=f"Book with slug '{slug}' not found!")
    return book


@app.post("/books/", response_model=Book, status_code=201, tags=["Books"])
async def create_book(new_book_data: BookCreate):
    if new_book_data.slug in books_db:
        raise HTTPException(status_code=400, detail="Book with slug '{new_book_data.slug}' already exists!")

    for existing_book in books_db.values():
        if existing_book.isbn == new_book_data.isbn:
            raise HTTPException(status_code=400, detail="Book with isbn '{new_book_data.isbn}' already exists!")

    new_book = Book(**new_book_data.model_dump())

    books_db[new_book.slug] = new_book

    return new_book


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
