from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import BaseModel


class UserModel(BaseModel):

    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
    )
