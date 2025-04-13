from sqlalchemy.orm import Session

from app.repositories import MovieRepository
from app.schemas import MovieSchema


class MovieService:

    async def find_all(self, db: Session):
        movie_repository = MovieRepository()
        response = await movie_repository.find_all(db=db)

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
