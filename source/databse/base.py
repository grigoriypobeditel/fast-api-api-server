from enum import Enum

from sqlalchemy.orm import (
    Session,
    Mapped,
    DeclarativeBase,
    mapped_column
)
from sqlalchemy import (
    String,
    create_engine,
    select,
    update,
    delete
)


__all__ = [
    "engine",
    "session",
    "select"
]

engine = create_engine("sqlite:///file.db", echo=True)


class UserRole(Enum):
    admin = "admin"
    user = "user"


class TypeServer(Enum):
    vps = "vps"
    vds = "vds"


class TypeDisk(Enum):
    ssd = "ssd"
    hdd = "hdd"


class Model(DeclarativeBase):
    ...


class User(Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(32))
    balance: Mapped[int] = mapped_column(default=0)
    role: Mapped[UserRole] = mapped_column(default=UserRole.user)


class Server(Model):
    __tablename__ = "servers"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str]
    type_server: Mapped[TypeServer]
    
    memory_cap: Mapped[str] = mapped_column(String(16))
    disk_cap: Mapped[str] = mapped_column(String(16))
    type_disk: Mapped[TypeDisk]

    price: Mapped[int]


Model.metadata.create_all(engine)

session = Session(engine)
