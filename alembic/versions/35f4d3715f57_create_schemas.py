"""create schemas

Revision ID: 35f4d3715f57
Revises: 
Create Date: 2021-04-30 21:51:30.184519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35f4d3715f57'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("create schema sor")
    op.execute("create schema sot")
    op.execute("create schema espec")


def downgrade():
    op.execute("drop schema sor")
    op.execute("drop schema sot")
    op.execute("drop schema espec")
