from fastapi import APIRouter, HTTPException, status
from .dependencies import Book, BookCreate
from .crud import storage

router = APIRouter(tags=["books"])


@router.get(
    "/",
    response_model=list[Book],
    summary="Получить список всех книг",
    description="Возвращает список всех книг"
)
def get_books():
    return storage.get_all()


@router.post(
    "/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
    summary="Создать новую книгу",
    description="Создает новую книгу"
)
def create_book(book_in: BookCreate) -> Book:
    book = storage.create(book_in)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"Книга с slug ({book_in.slug}) уже существует!"
    )