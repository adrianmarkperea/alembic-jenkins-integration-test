"""empty message

Revision ID: 2418e8672d8f
Revises:
Create Date: 2022-07-16 14:27:33.337271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2418e8672d8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    pass
