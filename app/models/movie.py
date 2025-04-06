from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import BaseModel, CategoryModel


class MovieModel(BaseModel):

    __tablename__ = "movies"

    name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    poster: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    category_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("categories.uuid"),
        nullable=False,
        index=True,
    )
    category: Mapped[CategoryModel] = relationship(
        back_populates="movies",
        foreign_keys=[category_uuid],
    )
