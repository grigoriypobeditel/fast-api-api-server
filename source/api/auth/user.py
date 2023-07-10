from pydantic import BaseModel, EmailStr

from source.databse.base import User


class AuthUser(BaseModel):
    email: EmailStr
    password: str


def route(data: AuthUser) -> dict:
    return {}
