from fastapi import FastAPI
from storage.books import BooksStorage
from core import config
from redis import Redis


async def lifespan(app: FastAPI):
    app.state.books_storage = BooksStorage()

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