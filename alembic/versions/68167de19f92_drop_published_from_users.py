"""drop published from users

Revision ID: 68167de19f92
Revises: da33bfa344bd
Create Date: 2023-06-24 20:08:13.219262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68167de19f92'
down_revision = 'da33bfa344bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('users', 'published')
    op.drop_column('users', 'created_at')
    pass


def downgrade() -> None:
    op.add_column('users', sa.Column('published', sa.Boolean(), server_default="TRUE",
                                     default=True, nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.now()
                                     ))
    pass
