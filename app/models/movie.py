from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models import BaseModel


class MovieModel(BaseModel):

    __tablename__ = "movies"

    name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    synopsis: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    slug: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        unique=True,
    )
