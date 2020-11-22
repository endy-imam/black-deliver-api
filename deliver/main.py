import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI Mangum Example", version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)


@app.get('/', name='Hello World', tags=['Hello'])
def hello_world():
    return {"Hello": "Python"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app)
