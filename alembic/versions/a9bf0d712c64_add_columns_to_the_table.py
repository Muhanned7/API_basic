"""add columns to the table

Revision ID: a9bf0d712c64
Revises: 39886c719d53
Create Date: 2023-06-17 18:23:43.598500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9bf0d712c64'
down_revision = '39886c719d53'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
