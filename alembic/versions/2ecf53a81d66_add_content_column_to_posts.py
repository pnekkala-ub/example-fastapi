"""add content column to posts

Revision ID: 2ecf53a81d66
Revises: f475d892a9aa
Create Date: 2024-05-11 18:54:42.815501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ecf53a81d66'
down_revision: Union[str, None] = 'f475d892a9aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
