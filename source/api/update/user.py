from pydantic import BaseModel, EmailStr

from source.databse.models.user_model import Role



class UpdateUser(BaseModel):
    email: EmailStr
    password: str
    role: Role | None


def route(data: UpdateUser) -> dict:
    return {}
