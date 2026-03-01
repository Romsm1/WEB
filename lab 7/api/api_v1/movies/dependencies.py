from fastapi import HTTPException, status, Depends, Request
from fastapi.security import HTTPBearer, HTTPBasic, HTTPBasicCredentials
from core import API_TOKENS, USERS
from typing import Annotated
from .crud import storage
from schemas import Movie

UNSAFE_METHODS = frozenset({
    "PATCH",
    "POST",
    "PUT",
    "DELETE"
})

http_bearer = HTTPBearer(
    scheme_name="API Token Bearer",
    description="Введите API токен для доступа к небезопасным методам",
    auto_error=False
)

http_basic = HTTPBasic(
    scheme_name="Basic Authentication",
    description="Введите имя пользователя и пароль",
    auto_error=False
)


def prefetch_movie(slug: str) -> Movie:
    movie = storage.get_by_slug(slug)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Фильм с slug '{slug}' не найден",
    )


def api_token_required_bearer(
        request: Request,
        token: Annotated[HTTPBasicCredentials, Depends(http_bearer)] = None
):
    if request.method not in UNSAFE_METHODS:
        return

    if token is None or token.credentials not in API_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token",
            headers={"WWW-Authenticate": "Bearer"}
        )


def basic_auth_required(
        request: Request,
        credentials: Annotated[HTTPBasicCredentials, Depends(http_basic)] = None
):
    if request.method not in UNSAFE_METHODS:
        return

    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Basic authentication required",
            headers={"WWW-Authenticate": "Basic"}
        )

    if credentials.username not in USERS or USERS[credentials.username] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"}
        )


auth_dependency = basic_auth_required

MovieDep = Annotated[Movie, Depends(prefetch_movie)]