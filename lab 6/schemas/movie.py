from typing import Annotated, Optional
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    slug: str
    description: str
    year: int
    duration: int


class MovieCreate(MovieBase):
    """
    Модель для создания фильма
    """
    slug: Annotated[str, MinLen(2), MaxLen(20)]


class Movie(MovieBase):
    """
    Модель самого фильма
    """


class MovieUpdate(MovieBase):
    """
    Модель обновления фильма полностью
    """
    slug: Annotated[str, MinLen(3), MaxLen(30)]


class MoviePartialUpdate(BaseModel):
    """
    Модель частичного редактирования информации фильма
    """
    title: Optional[str] = None
    slug: Optional[Annotated[str, MinLen(3), MaxLen(30)]] = None
    description: Optional[str] = None
    year: Optional[int] = None
    duration: Optional[int] = None
