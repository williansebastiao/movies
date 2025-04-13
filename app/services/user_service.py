from sqlalchemy.orm import Session

from app.repositories import UserRepository


class UserService:

    async def find_all(self, db: Session):
        user_repository = UserRepository()
        response = await user_repository.find_all(db=db)

        return response
