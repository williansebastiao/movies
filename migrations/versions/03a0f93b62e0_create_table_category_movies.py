"""create table category movies

Revision ID: 03a0f93b62e0
Revises: 8c65e9b3dc61
Create Date: 2025-04-10 08:07:33.379833

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "03a0f93b62e0"
down_revision: Union[str, None] = "8c65e9b3dc61"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "movie_categories",
        sa.Column("movie_uuid", sa.UUID(), nullable=False),
        sa.Column("category_uuid", sa.UUID(), nullable=False),
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["category_uuid"],
            ["categories.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["movie_uuid"],
            ["movies.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_movie_categories_category_uuid"),
        "movie_categories",
        ["category_uuid"],
        unique=False,
    )
    op.create_index(
        op.f("ix_movie_categories_movie_uuid"),
        "movie_categories",
        ["movie_uuid"],
        unique=False,
    )
    op.create_index(
        op.f("ix_movie_categories_uuid"),
        "movie_categories",
        ["uuid"],
        unique=False,
    )
    op.add_column("movies", sa.Column("synopsis", sa.Text(), nullable=False))
    op.add_column(
        "movies", sa.Column("movie_category_uuid", sa.UUID(), nullable=False)
    )
    op.drop_index("ix_movies_category_uuid", table_name="movies")
    op.create_index(
        op.f("ix_movies_movie_category_uuid"),
        "movies",
        ["movie_category_uuid"],
        unique=False,
    )
    op.drop_constraint(
        "movies_category_uuid_fkey", "movies", type_="foreignkey"
    )
    op.create_foreign_key(
        None, "movies", "movie_categories", ["movie_category_uuid"], ["uuid"]
    )
    op.drop_column("movies", "description")
    op.drop_column("movies", "category_uuid")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "movies",
        sa.Column(
            "category_uuid", sa.UUID(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "movies",
        sa.Column(
            "description", sa.TEXT(), autoincrement=False, nullable=False
        ),
    )
    op.drop_constraint(None, "movies", type_="foreignkey")
    op.create_foreign_key(
        "movies_category_uuid_fkey",
        "movies",
        "categories",
        ["category_uuid"],
        ["uuid"],
    )
    op.drop_index(op.f("ix_movies_movie_category_uuid"), table_name="movies")
    op.create_index(
        "ix_movies_category_uuid", "movies", ["category_uuid"], unique=False
    )
    op.drop_column("movies", "movie_category_uuid")
    op.drop_column("movies", "synopsis")
    op.drop_index(
        op.f("ix_movie_categories_uuid"), table_name="movie_categories"
    )
    op.drop_index(
        op.f("ix_movie_categories_movie_uuid"), table_name="movie_categories"
    )
    op.drop_index(
        op.f("ix_movie_categories_category_uuid"),
        table_name="movie_categories",
    )
    op.drop_table("movie_categories")
    # ### end Alembic commands ###
