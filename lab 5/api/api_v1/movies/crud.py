from .dependencies import Movie, MovieCreate, MovieUpdate, MoviePartialUpdate
from typing import Optional
from pydantic import BaseModel


class StorageMovie(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def get_all(self) -> list[Movie]:
        return list(self.slug_to_movie.values())

    def get_by_slug(self, slug: str) -> Optional[Movie]:
        return self.slug_to_movie.get(slug)

    def create(self, movie_in: MovieCreate) -> Movie:
        if movie_in.slug not in self.slug_to_movie:
            movie = Movie(**movie_in.model_dump())
            self.slug_to_movie[movie.slug] = movie
            return movie
        return False

    def update(self, movie: Movie, movie_in: MovieUpdate) -> Movie:
        updated_movie = movie.model_copy(update=movie_in.model_dump())
        self.slug_to_movie[updated_movie.slug] = updated_movie
        if movie.slug != updated_movie.slug:
            del self.slug_to_movie[movie.slug]
        return updated_movie

    def partial_update(self, movie: Movie, movie_in: MoviePartialUpdate) -> Movie:
        update_data = {k: v for k, v in movie_in.model_dump().items() if v is not None}
        updated_movie = movie.model_copy(update=update_data)
        self.slug_to_movie[updated_movie.slug] = updated_movie
        if movie.slug != updated_movie.slug:
            del self.slug_to_movie[movie.slug]
        return updated_movie

    def delete_by_slug(self, slug: str) -> bool:
        if slug in self.slug_to_movie:
            del self.slug_to_movie[slug]
            return True
        return False

    def delete(self, movie: Movie) -> bool:
        return self.delete_by_slug(slug=movie.slug)


storage = StorageMovie()

storage.create(
    MovieCreate(
        title="Harry Potter",
        slug="harry",
        description="Some description",
        year=2002,
        duration=150,
    )
)

storage.create(
    MovieCreate(
        title="Lord's of the ring",
        slug="ring",
        description="Some description",
        year=2000,
        duration=200,
    )
)
