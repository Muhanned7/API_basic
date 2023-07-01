"""change posts table

Revision ID: da33bfa344bd
Revises: e8d46d9ffd1e
Create Date: 2023-06-24 19:26:36.210784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da33bfa344bd'
down_revision = 'be3d8fc0dc3b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('posts', 'users')
    op.drop_column("users", "content")
    op.drop_column("users", "title")

    pass


def downgrade() -> None:
    op.rename_table('users', 'posts')
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    op.add_column("posts", sa.Column('title', sa.String(), nullable=False))

    pass
