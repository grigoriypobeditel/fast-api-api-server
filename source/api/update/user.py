from pydantic import BaseModel, EmailStr

from source.databse.base import UserRole



class UpdateUser(BaseModel):
    email: EmailStr
    password: str
    role: UserRole | None


def route(data: UpdateUser) -> dict:
    return {}
