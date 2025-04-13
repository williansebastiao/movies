from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from app.database import db_session
from app.exceptions import RepositoryException
from app.schemas import MovieSchema
from app.services import MovieService

router = APIRouter(prefix="/movie", tags=["Movie"])


@router.get(
    "",
    response_model=List[MovieSchema],
    status_code=status.HTTP_200_OK,
)
async def find_all(db=Depends(db_session)):
    try:
        movie_service = MovieService()
        response = await movie_service.find_all(db=db)
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


@router.post(
    "/{movie_uuid}/rate",
    status_code=status.HTTP_200_OK,
)
async def rate(movie_uuid: UUID):
    print(movie_uuid)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Ok"},
    )


@router.post(
    "/{user_uuid}/recomendation",
    status_code=status.HTTP_200_OK,
)
async def recomendation(user_uuid: UUID):
    print(user_uuid)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Ok"},
    )
