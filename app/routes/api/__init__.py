from fastapi import APIRouter

from . import health, movie, user

router = APIRouter()

router.include_router(health.router)
router.include_router(user.router)
router.include_router(movie.router)
