"""adding content table

Revision ID: be3d8fc0dc3b
Revises: a9bf0d712c64
Create Date: 2023-06-17 18:42:19.421565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be3d8fc0dc3b'
down_revision = 'a9bf0d712c64'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default="TRUE",
                                     default=True, nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()
                                     ))
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))

    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
