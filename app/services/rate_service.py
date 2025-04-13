from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories import RateRepository
from app.schemas import MovieSchema, RateCreateSchema


class RateService:

    async def rate(
        self,
        db: Session,
        payload: RateCreateSchema,
    ):
        rate_repository = RateRepository()
        response = await rate_repository.rate(
            db=db,
            payload=payload,
        )

        response_movies = []
        response_movies.append(
            MovieSchema(
                uuid=response.uuid,
                name=response.name,
                synopsis=response.synopsis,
                slug=response.slug,
                category=response.movie_categories.categories.category,
            )
        )

        return response_movies

    async def find_recomendation_by_user_uuid(
        self, db: Session, user_uuid: UUID
    ):
        rate_repository = RateRepository()
        response = await rate_repository.find_recomendation_by_user_uuid(
            db=db,
            user_uuid=user_uuid,
        )

        if len(response) == 0:
            return []

        response_movies = []
        for movie in response:
            response_movies.append(
                MovieSchema(
                    uuid=movie.uuid,
                    name=movie.name,
                    synopsis=movie.synopsis,
                    slug=movie.slug,
                    category=movie.movie_categories.categories.category,
                )
            )

        return response_movies
