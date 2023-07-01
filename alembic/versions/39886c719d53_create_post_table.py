"""create post table

Revision ID: 39886c719d53
Revises: 
Create Date: 2023-06-17 18:03:51.583215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39886c719d53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column(
        'id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
