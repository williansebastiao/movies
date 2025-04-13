from sqlalchemy import select
from sqlalchemy.orm import Session

from app.exceptions import RepositoryException
from app.models import UserModel


class UserRepository:

    async def find_all(self, db: Session):
        try:
            stmt = select(UserModel).order_by(UserModel.created_at.desc())
            response = db.scalars(stmt).all()

            return response
        except Exception as e:
            raise RepositoryException(message=str(e)) from e
