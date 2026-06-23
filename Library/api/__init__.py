from .api_v1 import router as api_v1_router

from fastapi import APIRouter

router = APIRouter(prefix='/api')  # Создает роутер с префиксом /api

router.include_router(api_v1_router)  # Подключает маршруты версии v1

