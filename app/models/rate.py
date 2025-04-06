from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import BaseModel, MovieModel, UserModel


class RateModel(BaseModel):

    __tablename__ = "ratings"

    movie_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("movies.uuid"),
        nullable=False,
        index=True,
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.uuid"),
        nullable=False,
        index=True,
    )
    user: Mapped[MovieModel] = relationship(
        back_populates="users",
        foreign_keys=[movie_uuid],
    )
    movie: Mapped[UserModel] = relationship(
        back_populates="movies",
        foreign_keys=[user_id],
    )
