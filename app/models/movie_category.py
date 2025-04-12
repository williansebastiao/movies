from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models import BaseModel


class MovieCategoryModel(BaseModel):

    __tablename__ = "movie_categories"

    movie_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("movies.uuid"),
        nullable=False,
        index=True,
    )
    category_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("categories.uuid"),
        nullable=False,
        index=True,
    )
