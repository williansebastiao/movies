"""remove column user_uiid

Revision ID: bf640f3f16c1
Revises: 04c9824c6e39
Create Date: 2025-04-13 16:26:48.183432

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "bf640f3f16c1"
down_revision: Union[str, None] = "04c9824c6e39"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_ratings_user_uuid", table_name="ratings")
    op.drop_constraint("ratings_user_uuid_fkey", "ratings", type_="foreignkey")
    op.drop_column("ratings", "user_uuid")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "ratings",
        sa.Column("user_uuid", sa.UUID(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "ratings_user_uuid_fkey", "ratings", "users", ["user_uuid"], ["uuid"]
    )
    op.create_index(
        "ix_ratings_user_uuid", "ratings", ["user_uuid"], unique=False
    )
    # ### end Alembic commands ###
