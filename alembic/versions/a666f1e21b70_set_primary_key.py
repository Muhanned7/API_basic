"""set primary key

Revision ID: a666f1e21b70
Revises: be3d8fc0dc3b
Create Date: 2023-06-24 12:11:13.015235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a666f1e21b70'
down_revision = 'be3d8fc0dc3b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('email', sa.String(), nullable=False))
    op.create_unique_constraint("uq_table_column", "posts", ['email'])
    pass


def downgrade() -> None:
    op.drop_column('posts', 'email')
    pass
