from fastapi import APIRouter, HTTPException, status, Depends
from schemas import Movie, MovieCreate
from ..crud import storage
from ..dependencies import api_token_required

COMMON_401_RESPONSE = {
    status.HTTP_401_UNAUTHORIZED: {
        "description": "Invalid API token",
        "content": {
            "application/json": {
                "example": {
                    "detail": "API токен не действителен"
                }
            }
        },
    }
}

router = APIRouter(tags=["movies"],
                   dependencies=[Depends(api_token_required)],
                   responses=COMMON_401_RESPONSE)


@router.get(
    "/",
    response_model=list[Movie],
    summary="Получить все фильмы",
    description="Возвращает список всех фильмов в каталоге"
)
def get_list_movies():
    return storage.get_all()


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
    summary="Создать фильм",
    description="Создает новый фильм в каталоге"
)
def create_movie(movie_in: MovieCreate) -> Movie:
    movie = storage.create(movie_in)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"Фильм с slug ({movie_in.slug}) уже существует"
    )