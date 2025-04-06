from uuid import UUID

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/movie", tags=["Movie"])


@router.get(
    "",
    status_code=status.HTTP_200_OK,
)
async def find_all():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Ok"},
    )


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
