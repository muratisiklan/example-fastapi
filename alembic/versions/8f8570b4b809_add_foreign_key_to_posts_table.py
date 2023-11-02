"""add foreign key to posts table

Revision ID: 8f8570b4b809
Revises: 9111f7737cad
Create Date: 2023-11-02 13:55:28.699207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f8570b4b809'
down_revision: Union[str, None] = '9111f7737cad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts",
                          referent_table="users",
                          local_cols=["owner_id"],
                          remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts",
                       type_="foreignkey")
    op.drop_column("posts", "owner_id")
    pass
