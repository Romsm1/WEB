import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Books and Movies API")


@app.on_event("startup")
def startup_event():
    try:
        from api.api_v1 import api_v1_router
        app.include_router(api_v1_router)
        print("API v1 router loaded successfully")
    except ImportError as e:
        print(f"Error loading API router: {e}")
        print("Creating simple endpoints instead...")

        from typing import List
        from pydantic import BaseModel

        class Book(BaseModel):
            title: str
            slug: str
            description: str
            pages: int

        class Movie(BaseModel):
            title: str
            slug: str
            description: str
            year: int
            duration: int

        BOOKS = [
            Book(title="Harry Potter", slug="harry", description="Some description", pages=400),
            Book(title="Lord's of the ring", slug="ring", description="Some description", pages=800),
        ]

        MOVIES = [
            Movie(slug="Harry", title="Harry Potter", description="Some description", year=2002, duration=150),
            Movie(slug="Ring", title="Lord's of the ring", description="Some description", year=2000, duration=200),
        ]

        @app.get("/api/v1/books", response_model=List[Book])
        def get_books():
            return BOOKS

        @app.get("/api/v1/movies", response_model=List[Movie])
        def get_movies():
            return MOVIES


@app.get("/")
def read_root():
    return {
        "docs": "/docs",
        "api_v1": "/api/v1",
        "books": "/api/v1/books",
        "movies": "/api/v1/movies"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)