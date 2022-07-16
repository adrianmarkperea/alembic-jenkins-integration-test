"""Add account table again

Revision ID: 3371f058ebb6
Revises: 0cc8c07ccded
Create Date: 2022-07-16 14:52:35.806446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3371f058ebb6'
down_revision = '0cc8c07ccded'
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
