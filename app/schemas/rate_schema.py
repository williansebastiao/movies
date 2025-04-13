from uuid import UUID

from pydantic import BaseModel


class RateCreateSchema(BaseModel):
    movie_uuid: UUID
    user_uuid: UUID
