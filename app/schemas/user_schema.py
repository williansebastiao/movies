from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    uuid: Optional[UUID] = None
    first_name: str
    last_name: str
    email: EmailStr
