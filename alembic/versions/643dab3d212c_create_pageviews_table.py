"""create pageviews table

Revision ID: 643dab3d212c
Revises: b969af6a3cc0
Create Date: 2021-05-01 09:46:26.008542

"""
from alembic import op
import sqlalchemy as sa
from app.utils.set_schema import set_schema


# revision identifiers, used by Alembic.
revision = '643dab3d212c'
down_revision = 'b969af6a3cc0'
branch_labels = None
depends_on = None


@set_schema('sor')
def upgrade():
    op.create_table(
        'pageviews',
        sa.Column('referer', sa.String(50)),
        sa.Column('device_id', sa.String(256)),
        sa.Column('campaign_id', sa.BIGINT),
        sa.Column('ad_creative_id', sa.BIGINT),
        sa.Column('date', sa.Date),
        sa.Column('url', sa.String(256)),
        sa.Column('IP', sa.String(15))
    )


@set_schema('sor')
def downgrade():
    op.drop_table('pageviews')
