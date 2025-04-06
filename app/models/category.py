from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.enums import CategoryType
from app.models import BaseModel


class CategoryModel(BaseModel):

    __tablename__ = "categories"

    category: Mapped[Enum] = mapped_column(
        Enum(CategoryType),
        nullable=False,
    )
