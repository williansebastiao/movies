from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/user", tags=["User"])


@router.get(
    "",
    status_code=status.HTTP_200_OK,
)
async def find_all():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Ok"},
    )
