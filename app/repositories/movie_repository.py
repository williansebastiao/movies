from sqlalchemy import select
from sqlalchemy.orm import Session

from app.exceptions import RepositoryException
from app.models import CategoryModel, MovieCategoryModel, MovieModel


class MovieRepository:

    async def find_all(self, db: Session):
        try:
            stmt = (
                select(MovieModel)
                .join(MovieModel.movie_categories)
                .join(MovieCategoryModel.categories)
                .order_by(CategoryModel.category.asc())
                .order_by(MovieModel.name.asc())
            )

            response = db.scalars(stmt).all()

            return response
        except Exception as e:
            raise RepositoryException(message=str(e)) from e
