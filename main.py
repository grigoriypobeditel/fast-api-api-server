from fastapi import FastAPI
from uvicorn import run as uvicorn_run

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn_run("main:app", host="127.0.0.1", port=8000)
