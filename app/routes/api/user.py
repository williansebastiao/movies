from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.database import db_session
from app.exceptions import RepositoryException
from app.schemas import UserSchema
from app.services import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.get(
    "",
    response_model=List[UserSchema],
    status_code=status.HTTP_200_OK,
)
async def find_all(db=Depends(db_session)):
    try:
        user_service = UserService()
        response = await user_service.find_all(db=db)
        return response
    except RepositoryException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e
