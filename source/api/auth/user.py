from pydantic import BaseModel, EmailStr

from source.databse.base import session, select, User, UserRole



class AuthUser(BaseModel):
    email: EmailStr
    password: str


def route(data: AuthUser) -> dict:
    stmt = select(User).where(User.email ==  data.email)
    result = session.scalars(statement=stmt).first()
    if not result:
        return {"status": "error", "msg": "user not found"}
    if result.password != data.password:
        return {"status": "error", "msg": "wrong password"}
    return {"status": "succsess", "msg": "authorization succsess"}
