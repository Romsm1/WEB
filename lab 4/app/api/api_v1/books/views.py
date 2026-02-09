from typing import List
from fastapi import APIRouter, Depends
from schemas.book import Book, BookCreate
from . import crud
from .dependencies import get_book_by_slug_dependency

router = APIRouter()

@router.get("/", response_model=List[Book])
def get_books():
    return crud.get_books()

@router.post("/", response_model=Book)
def create_book(book_in: BookCreate):
    return crud.create_book(book_in)

@router.get("/{slug}", response_model=Book)
def get_book_details(book: Book = Depends(get_book_by_slug_dependency)):
    return book