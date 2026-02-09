from pydantic import BaseModel
from typing import Optional
from schemas.movie import Movie, MovieCreate


class MovieStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}  # хранилище фильмов в памяти

    def get_all(self) -> list[Movie]:
        return list(self.slug_to_movie.values())  # получить все фильмы

    def get_by_slug(self, slug: str) -> Optional[Movie]:
        return self.slug_to_movie.get(slug)  # получить фильм по slug

    def create(self, movie_in: MovieCreate) -> Movie:
        if movie_in.slug in self.slug_to_movie:
            raise ValueError(f"Movie with slug '{movie_in.slug}' already exists")
            # создание нового фильм
        movie = Movie(**movie_in.dict())
        self.slug_to_movie[movie.slug] = movie
        return movie


movie_storage = MovieStorage()  # создание экземпляра хранилища

movie_storage.slug_to_movie = {
    "Harry": Movie(
        slug="Harry",
        title="Harry Potter",
        description="Some description",
        year=2002,
        duration=150,
    ),
    "Ring": Movie(
        slug="Ring",
        title="Lord's of the ring",
        description="Some description",
        year=2000,
        duration=200,
    ),
}
# инициализация начальными данными
