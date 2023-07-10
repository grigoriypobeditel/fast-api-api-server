from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base_model import Model


class TypeServer(Enum):
    vps = "vps"
    vds = "vds"


class TypeDisk(Enum):
    ssd = "ssd"
    hdd = "hdd"


class Server(Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str]
    type_server: Mapped[TypeServer]
    
    memory_cap: Mapped[str] = mapped_column(String(16))
    disk_cap: Mapped[str] = mapped_column(String(16))
    type_disk: Mapped[TypeDisk]

    price: Mapped[int]
