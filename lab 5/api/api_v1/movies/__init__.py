from fastapi import APIRouter
from .details_views import router as details_router
from .list_views import router as list_router


router = APIRouter(prefix="/movies", tags=["movies"])
router.include_router(details_router)
router.include_router(list_router)
