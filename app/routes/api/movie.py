from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.database import db_session
from app.exceptions import RepositoryException
from app.schemas import MovieSchema, RateCreateSchema
from app.services import MovieService, RateService

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
    "/rate",
    response_model=MovieSchema,
    status_code=status.HTTP_201_CREATED,
)
async def rate(payload: RateCreateSchema, db=Depends(db_session)):
    try:
        rate_service = RateService()
        response = await rate_service.rate(
            db=db,
            payload=payload,
        )
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


@router.get(
    "/{user_uuid}/recomendation",
    status_code=status.HTTP_200_OK,
)
async def recomendation(user_uuid: UUID, db=Depends(db_session)):
    try:
        rate_service = RateService()
        response = await rate_service.find_recomendation_by_user_uuid(
            db=db,
            user_uuid=user_uuid,
        )
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
