from fastapi import APIRouter
import os

api_v1_router = APIRouter(prefix="/api/v1")

print("DEBUG INFO")
print(f"Current dir: {os.path.dirname(__file__)}")
print(f"Movies views path: {os.path.join(os.path.dirname(__file__), 'movies', 'views.py')}")
print(f"File exists: {os.path.exists(os.path.join(os.path.dirname(__file__), 'movies', 'views.py'))}")

try:
    from .books.views import router as books_router
    print("Books router imported successfully")
    api_v1_router.include_router(books_router, prefix="/books", tags=["books"])
except ImportError as e:
    print(f"Books error: {e}")

try:
    from .movies.views import router as movies_router
    print("Movies router imported successfully")
    api_v1_router.include_router(movies_router, prefix="/movies", tags=["movies"])
except ImportError as e:
    print(f"Movies error: {e}")

print("==================")