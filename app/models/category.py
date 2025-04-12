from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.enums import CategoryType
from app.models import BaseModel


class CategoryModel(BaseModel):

    __tablename__ = "categories"

    category: Mapped[Enum] = mapped_column(
        Enum(CategoryType),
        nullable=False,
    )
    slug: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        unique=True,
    )
