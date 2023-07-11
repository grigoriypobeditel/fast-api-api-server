from fastapi import FastAPI
from uvicorn import run as uvicorn_run

from source.api.create import user as c_user_api
from source.api.auth import user as auth_user_api
from source.api.update import password as u_password_api
from source.api.create import service as c_service_api

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"status": "error/succsess",
            "msg": "this small message",
            "list": ["This", "list", "with", "elements"]}


@app.post("/create/user/")
async def create_user(data: c_user_api.CreateUser) -> dict:
    return c_user_api.route(data)


@app.post("/update/password/")
async def update_password(data: u_password_api.UpdatePassword) -> dict:
    return u_password_api.route(data)


@app.post("/auth")
async def auth(data: auth_user_api.AuthUser) -> dict:
    return auth_user_api.route(data)


@app.post("/create/service/")
async def create_service(data: c_service_api.CreateService) -> dict:
    return c_service_api.route(data)


if __name__ == "__main__":
    uvicorn_run("main:app", host="127.0.0.1", port=8000)
