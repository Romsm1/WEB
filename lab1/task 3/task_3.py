from fastapi import FastAPI
app = FastAPI()

@app.post("/calculate")
def calculate(num1: float, num2: float):
    return {"result": num1 + num2}

@app.get("/")
def home():
    return "Откройте http://127.0.0.1:8000/docs для теста POST /calculate и нажмите Try it out"

@app.get("/calculate")
def calculate_get(num1: float, num2: float):
    return {"result": num1 + num2}



# uvicorn task_3:app --reload
# http://127.0.0.1:8000/calculate?num1=50&num2=200 пример результата