from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base_model import Model


class Role(Enum):
    admin = "admin"
    user = "user"


class User(Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(32))
    balance: Mapped[int] = mapped_column(default=0)
    role: Mapped[Role] = mapped_column(default=Role.user)
