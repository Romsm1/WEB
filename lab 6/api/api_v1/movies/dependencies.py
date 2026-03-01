from fastapi import HTTPException, status, Depends, Request, Header
from core import API_TOKENS
from typing import Annotated
from .crud import storage
from schemas import Movie

UNSAFE_METHODS = frozenset({
    "PATCH",
    "POST",
    "PUT",
    "DELETE"
})


def prefetch_movie(slug: str) -> Movie:
    movie = storage.get_by_slug(slug)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Фильм с slug '{slug}' не найден",
    )


def api_token_required(
        request: Request,
        api_token: Annotated[
            str,
            Header(alias="x-auth-token")
        ] = "",
):
    if request.method not in UNSAFE_METHODS:
        return

    if api_token not in API_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token"
        )


MovieDep = Annotated[Movie, Depends(prefetch_movie)]