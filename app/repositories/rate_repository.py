from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.exceptions import RepositoryException
from app.models import CategoryModel, MovieCategoryModel, MovieModel, RateModel
from app.schemas import RateCreateSchema


class RateRepository:

    async def rate(
        self,
        db: Session,
        payload: RateCreateSchema,
    ):
        try:

            exists = (
                db.execute(
                    select(RateModel).where(
                        RateModel.user_uuid == payload.user_uuid,
                        RateModel.movie_uuid == payload.movie_uuid,
                    )
                )
                .scalars()
                .first()
            )
            if exists:
                raise RepositoryException(
                    message="User already rated this movie"
                )

            stmt = RateModel(**payload.model_dump())

            db.add(stmt)
            db.commit()
            db.refresh(stmt)

            response = select(MovieModel).where(
                MovieModel.uuid == payload.movie_uuid,
            )
            response = db.scalars(response).first()

            return response
        except Exception as e:
            raise RepositoryException(message=str(e)) from e

    async def find_recomendation_by_user_uuid(
        self, db: Session, user_uuid: UUID
    ):
        try:
            stmt = select(RateModel).where(
                RateModel.user_uuid == user_uuid,
            )
            responses = db.scalars(stmt).all()

            category_list = set()
            user_list = []
            for response in responses:
                user_list.append(response.movie_uuid)
                category_list.add(
                    response.movies.movie_categories.category_uuid
                )

            movies = (
                select(MovieModel)
                .join(MovieCategoryModel)
                .join(CategoryModel)
                .where(
                    MovieModel.uuid.notin_(user_list),
                    MovieCategoryModel.category_uuid.in_(category_list),
                )
                .order_by(CategoryModel.category.asc())
                .order_by(MovieModel.name.asc())
            )
            movies = db.scalars(movies).all()
            if not movies:
                return []

            return movies
        except Exception as e:
            raise RepositoryException(message=str(e)) from e
