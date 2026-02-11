from typing import List
from schemas.book import Book, BookCreate

BOOKS = [
    Book(
        title="Harry Potter",
        slug="harry",
        description="Some description",
        pages=400,
    ),
    Book(
        title="Lord's of the ring",
        slug="ring",
        description="Some description",
        pages=800,
    ),
]

def get_books() -> List[Book]:
    return BOOKS

def get_book_by_slug(slug: str) -> Book | None:
    return next((book for book in BOOKS if book.slug == slug), None)

def create_book(book_in: BookCreate) -> Book:
    book = Book(**book_in.model_dump())
    return book
