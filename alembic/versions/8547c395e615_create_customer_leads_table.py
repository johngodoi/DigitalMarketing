"""create customer_leads table

Revision ID: 8547c395e615
Revises: 643dab3d212c
Create Date: 2021-05-01 09:51:54.189232

"""
from alembic import op
import sqlalchemy as sa
from app.utils.set_schema import set_schema


# revision identifiers, used by Alembic.
revision = '8547c395e615'
down_revision = '643dab3d212c'
branch_labels = None
depends_on = None


@set_schema('sor')
def upgrade():
    op.create_table(
        'customer_leads',
        sa.Column('device_id', sa.String(256)),
        sa.Column('lead_id', sa.BIGINT),
        sa.Column('registered_at', sa.Date),
        sa.Column('credit_decision', sa.String(1)),
        sa.Column('credit_decision_at', sa.Date),
        sa.Column('signed_at', sa.Date),
        sa.Column('revenue', sa.Float)
    )


@set_schema('sor')
def downgrade():
    op.drop_table('customer_leads')
