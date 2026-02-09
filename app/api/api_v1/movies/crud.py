from typing import List
from .storage import movie_storage
from schemas.movie import Movie, MovieCreate


def get_movies() -> List[Movie]:
    return movie_storage.get_all()


def get_movie_by_slug(slug: str) -> Movie | None:
    return movie_storage.get_by_slug(slug)


def create_movie(movie_in: MovieCreate) -> Movie:
    return movie_storage.create(movie_in)
