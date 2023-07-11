from pydantic import BaseModel

from source.databse.base import session, select, Server, TypeDisk, TypeServer

class CreateService(BaseModel):
    title: str
    description: str
    type_server: TypeServer
    memory_cap: str
    disk_cap: str
    type_disk: TypeDisk
    price: int

def route(data: CreateService) -> dict:
    if data.title == "":
        return {"status": "error", "msg": "title have small lenght"}
    if data.description == "":
        return {"status": "error", "msg": "add description"}
    if data.memory_cap == "":
        return {"status": "error", "msg": "add description memory capacity"}
    
    session.add(Server(
        title=data.title.title(),
        description=data.description,
        type_server=data.type_server,
        memory_cap=data.memory_cap,
        disk_cap=data.disk_cap,
        type_disk=data.type_disk,
        price=data.price
    ))
    session.commit()
    return {"status": "succsess", "msg": "service added"}
