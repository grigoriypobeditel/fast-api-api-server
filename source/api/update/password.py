from pydantic import BaseModel, EmailStr

from source.databse.base import User, select, session, update



class UpdatePassword(BaseModel):
    email: EmailStr
    old_password: str
    new_password: str


def route(data: UpdatePassword) -> dict:
    stmt = select(User).where(User.email ==  data.email)
    result = session.scalars(statement=stmt).first()
    if not result:
        return {"status": "error", "msg": "email not found"}
    if data.old_password != result.password:
        return {"status": "error", "msg": "wrong old password"}
    if len(data.new_password) < 8:
        return {"status": "error", "msg": "small length password"}
    stmt = update(User).where(User.email == data.email).values(password=data.new_password)
    session.execute(stmt)
    session.commit()
    return {"status": "succsess", "msg": "succsess change password"}
