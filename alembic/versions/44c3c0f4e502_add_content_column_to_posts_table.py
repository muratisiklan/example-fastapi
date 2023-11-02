"""add content column to posts table

Revision ID: 44c3c0f4e502
Revises: a23bcf9eb691
Create Date: 2023-11-01 21:37:33.623857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44c3c0f4e502'
down_revision: Union[str, None] = 'a23bcf9eb691'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(
        "content", sa.String(100), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
