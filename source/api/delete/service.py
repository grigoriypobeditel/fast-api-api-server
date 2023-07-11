from pydantic import BaseModel

from source.databse.base import session, select, Server, delete


class DeleteService(BaseModel):
    id: int


def route(data: DeleteService) -> dict:
    stmt = select(Server).where(Server.id == data.id)
    result = session.scalars(statement=stmt).first()
    if not result:
        return {"status": "error", "msg": "server not found"}
    
    stmt = delete(Server).where(Server.id == data.id)
    session.execute(stmt)
    session.commit()
    return {"status": "succsess", "msg": "service removed"}
