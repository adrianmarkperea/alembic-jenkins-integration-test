"""Remove accounts table

Revision ID: 0cc8c07ccded
Revises: 2418e8672d8f
Create Date: 2022-07-16 14:30:26.347940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cc8c07ccded'
down_revision = '2418e8672d8f'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('account')


def downgrade():
    pass
