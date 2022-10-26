"""add content column to posts table

Revision ID: 3a5775e0099c
Revises: d49631000367
Create Date: 2022-10-26 10:58:15.660055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a5775e0099c'
down_revision = 'd49631000367'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", 'content')
    pass
