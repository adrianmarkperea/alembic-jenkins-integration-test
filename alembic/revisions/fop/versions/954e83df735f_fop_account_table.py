"""fop account table

Revision ID: 954e83df735f
Revises: 
Create Date: 2022-04-26 17:57:01.829927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '954e83df735f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'fop_account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200))
    )


def downgrade():
    op.drop_table('fop_account')
