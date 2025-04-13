from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import BaseModel


class RateModel(BaseModel):

    __tablename__ = "ratings"

    movie_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("movies.uuid"),
        nullable=False,
        index=True,
    )
    user_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("users.uuid"),
        nullable=False,
        index=True,
    )
    movies: Mapped["MovieModel"] = relationship(
        back_populates="ratings",
        foreign_keys=[movie_uuid],
    )
