from typing import Annotated
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
