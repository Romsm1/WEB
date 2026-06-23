from fastapi import FastAPI
from storage.books import BooksStorage
from schemas.book import BookCreate
from core import config
from redis import Redis


async def lifespan(app: FastAPI):
    app.state.books_storage = BooksStorage()  # Создаем и сохраняем хранилища
    storage = app.state.books_storage

    # Создаем начальные книги если хранилище пустое
    if not storage.get():
        books = [
            BookCreate(
                slug="the-stand",
                title="The Stand",
                description="Постапокалиптический роман Стивена Кинга о противостоянии добра и зла",
                pages=1152
            ),
            BookCreate(
                slug="dune",
                title="Dune",
                description="Фантастический роман Фрэнка Герберта о планете Арракис и борьбе за власть",
                pages=896
            ),
        ]
        for book in books:
            storage.create(book)

    redis_users = Redis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=config.REDIS_DB_USERS,
        decode_responses=True,
    )
    redis_users.set("Roman", "228")

    yield

    # При остановке сервера очищаем книги
    redis_books = Redis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=config.REDIS_DB_BOOKS,
    )
    redis_books.flushdb()
