from fastapi import APIRouter, status, Depends
from schemas import Movie, MovieUpdate, MoviePartialUpdate
from ..crud import storage
from ..dependencies import MovieDep, api_token_required

COMMON_404_RESPONSE = {
    status.HTTP_404_NOT_FOUND: {
        "description": "Фильм не найден",
        "content": {
            "application/json": {
                "example": {"detail": "Фильм с slug (harry) не найден"}
            }
        },
    }
}

COMMON_401_RESPONSE = {
    status.HTTP_401_UNAUTHORIZED: {
        "description": "Invalid API token",
        "content": {
            "application/json": {
                "example": {"detail": "Invalid API token"}
            }
        },
    }
}

router = APIRouter(tags=["movies"],
                   dependencies=[Depends(api_token_required)],
                   responses={**COMMON_404_RESPONSE, **COMMON_401_RESPONSE})


@router.get(
    "/{slug}",
    response_model=Movie,
    summary="Получить фильм по slug",
    description="Возвращает детальную информацию о фильме по его slug",
)
def get_movie_details_by_slug(
        movie: MovieDep,
) -> Movie:
    return movie


@router.put(
    "/{slug}",
    response_model=Movie,
    summary="Полное обновление фильма",
    description="Полностью обновляет информацию о фильме",
)
def update_movie(
        movie: MovieDep,
        movie_in: MovieUpdate,
) -> Movie:
    return storage.update(movie, movie_in)


@router.patch(
    "/{slug}",
    response_model=Movie,
    summary="Частичное обновление фильма",
    description="Частично обновляет информацию о фильме",
)
def partial_update_movie(
        movie: MovieDep,
        movie_in: MoviePartialUpdate,
) -> Movie:
    return storage.partial_update(movie, movie_in)


@router.delete(
    "/{slug}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить фильм",
    description="Удаляет фильм из каталога по его slug",
)
def delete_movie(
        movie: MovieDep,
):
    storage.delete(movie)
    return None