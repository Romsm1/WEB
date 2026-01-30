from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определяем маршрут для корневого URL (/)
@app.get("/")
def read_root():
    # Возвращаем JSON-ответ
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}




# для запуска приложения с помощью uvicorn в режиме разработки (с флагом автоперезагрузки)
# uvicorn app:app --reload