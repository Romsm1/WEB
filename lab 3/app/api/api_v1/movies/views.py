from typing import List
from fastapi import APIRouter, Depends
from schemas.movie import Movie, MovieCreate
from . import crud
from .dependencies import get_movie_by_slug_dependency

router = APIRouter()

@router.get("/", response_model=List[Movie])
def get_movies():
    return crud.get_movies()

@router.post("/", response_model=Movie)
def create_movie(movie_in: MovieCreate):
    return crud.create_movie(movie_in)

@router.get("/{slug}", response_model=Movie)
def get_movie_details(movie: Movie = Depends(get_movie_by_slug_dependency)):
    return movie