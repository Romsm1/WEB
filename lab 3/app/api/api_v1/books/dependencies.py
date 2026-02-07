from fastapi import HTTPException, status
from schemas.book import Book
from . import crud

def get_book_by_slug_dependency(slug: str) -> Book:
    book = crud.get_book_by_slug(slug)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with slug '{slug}' not found"
        )
    return book