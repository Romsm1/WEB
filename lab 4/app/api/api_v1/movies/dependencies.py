from fastapi import HTTPException, status
from schemas.movie import Movie
from . import crud

def get_movie_by_slug_dependency(slug: str) -> Movie:
    movie = crud.get_movie_by_slug(slug)
    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie with slug '{slug}' not found"
        )
    return movie