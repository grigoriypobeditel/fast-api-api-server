from pydantic import BaseModel, EmailStr

from source.databse.models.user_model import Role



class AuthUser(BaseModel):
    email: EmailStr
    password: str


def route(data: AuthUser) -> dict:
    return {}
