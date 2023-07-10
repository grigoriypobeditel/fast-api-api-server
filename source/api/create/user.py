from pydantic import BaseModel, EmailStr

from source.databse.base import session, select, User, UserRole


class CreateUser(BaseModel):
    email: EmailStr
    password: str
    role: UserRole


def route(data: CreateUser) -> dict:
    stmt = select(User).where(User.email ==  data.email)
    if len(data.password) < 8:
        return {"status": "error", "msg": "password have small lenght"}
    if session.scalars(statement=stmt).first():
        return {"status": "error", "msg": "user exists"}
    return {"status": "succsess", "msg": "user created"}
