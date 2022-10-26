"""add new columns to posts table

Revision ID: 5b48c6457799
Revises: 584d10fa8a92
Create Date: 2022-10-26 11:17:57.462265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b48c6457799'
down_revision = '584d10fa8a92'
branch_labels = None
depends_on = None



def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass