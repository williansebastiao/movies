from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.enums import CategoryType


class MovieSchema(BaseModel):
    uuid: Optional[UUID] = None
    name: str
    synopsis: str
    slug: str
    category: CategoryType
