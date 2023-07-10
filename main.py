from fastapi import FastAPI
from uvicorn import run as uvicorn_run

from source.api.create import user as c_user_api
from source.api.update import user as u_user_api
from source.api.auth import user as auth_user_api

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.post("/create/user/")
async def create_user(data: c_user_api.CreateUser) -> dict:
    return c_user_api.route(data)


@app.post("/update/user/")
async def update_user(data: u_user_api.UpdateUser) -> dict:
    return u_user_api.route(data)


@app.post("/auth")
async def auth(data: auth_user_api.AuthUser) -> dict:
    return auth_user_api.route(data)


if __name__ == "__main__":
    uvicorn_run("main:app", host="127.0.0.1", port=8000)
