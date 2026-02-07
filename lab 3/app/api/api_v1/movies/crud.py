from typing import List
from schemas.movie import Movie, MovieCreate
MOVIES = [
    Movie(
        slug="Harry",
        title="Harry Potter",
        description="Some description",
        year=2002,
        duration=150,
    ),
    Movie(
        slug="Ring",
        title="Lord's of the ring",
        description="Some description",
        year=2000,
        duration=200,
    ),
]

def get_movies() -> List[Movie]:
    return MOVIES

def get_movie_by_slug(slug: str) -> Movie | None:
    return next((movie for movie in MOVIES if movie.slug == slug), None)

def create_movie(movie_in: MovieCreate) -> Movie:
    movie = Movie(**movie_in.model_dump())
    MOVIES.append(movie)
    return movie