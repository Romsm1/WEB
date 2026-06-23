from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from templating.jinja_template import templates
from dependencies.books import GetBooksStorage

router = APIRouter(prefix='/books')


@router.get(
    '/',
    name='books:list',
    response_class=HTMLResponse,
)
def list_view(
        request: Request,
        storage: GetBooksStorage,  # Внедряем зависимость хранилища
) -> HTMLResponse:
    books = storage.get()  # Получаем все книги из хранилища
    return templates.TemplateResponse(
        request=request,
        name='books/list.html',  # Шаблон для списка книг
        context={'books': books}  # Передаем книги в шаблон
    )
