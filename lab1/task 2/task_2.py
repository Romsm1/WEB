from fastapi import FastAPI
from fastapi.responses import FileResponse  # Для возврата файлов как HTTP ответ
import os  # Для работы с файловой системой (пути к файлам)

app = FastAPI()

# Определяем маршрут для корневого URL (/)
@app.get("/")
async def root():
    # Получаем путь к текущей директории, где находится этот файл Python
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Формируем полный путь к файлу index.html / os.path.join() корректно соединяет пути для текущей ОС
    file_path = os.path.join(current_dir, "index.html")
    # Возвращаем файл как HTTP-ответ / FileResponse автоматически определяет тип, заголовки и читает файл
    return FileResponse(file_path)


# uvicorn task_2:app --reload