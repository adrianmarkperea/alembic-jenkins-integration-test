"""Add new column to accounts table

Revision ID: e0ff36470550
Revises: 3371f058ebb6
Create Date: 2022-07-16 16:52:08.371107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0ff36470550'
down_revision = '3371f058ebb6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('new_column', sa.String()))


def downgrade():
    pass
