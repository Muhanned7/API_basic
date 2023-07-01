"""create posts table

Revision ID: c26a90115612
Revises: 68167de19f92
Create Date: 2023-06-29 11:13:53.542399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c26a90115612'
down_revision = '68167de19f92'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column(
        'id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('published', sa.Boolean(), server_default="TRUE",
                  default=True, nullable=False),
        sa.Column('content', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")
                  ),
        sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('fk_model_other_table', source_table='posts',
                          referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
