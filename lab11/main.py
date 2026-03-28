import uvicorn
from api import router as api_router
from fastapi import FastAPI

app = FastAPI(title='Books')

app.include_router(api_router)


@app.get('/')
def read_root():
    return {
        'message': '/docs',
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

# docker run -d --name redis-lab11 -p 6379:6379 redis:alpine
