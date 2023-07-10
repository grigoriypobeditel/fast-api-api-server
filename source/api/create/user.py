from pydantic import BaseModel, EmailStr

from source.databse.models.user_model import Role



class CreateUser(BaseModel):
    email: EmailStr
    password: str
    role: Role


def route(data: CreateUser) -> dict:
    return {}
