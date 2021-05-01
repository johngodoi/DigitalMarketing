"""create facebook_ads_media_costs table

Revision ID: 2cccdcd85ca6
Revises: 35f4d3715f57
Create Date: 2021-04-30 22:55:16.769059

"""
from alembic import op
import sqlalchemy as sa
from app.utils.set_schema import set_schema


# revision identifiers, used by Alembic.

revision = '2cccdcd85ca6'
down_revision = '35f4d3715f57'
branch_labels = None
depends_on = None


@set_schema('sor')
def upgrade():
    op.create_table(
        'facebook_ads_media_costs',
        sa.Column('date', sa.Date),
        sa.Column('campaign_id', sa.BIGINT),
        sa.Column('campaign_name', sa.String(256)),
        sa.Column('impression', sa.BIGINT),
        sa.Column('clicks', sa.BIGINT),
        sa.Column('cost', sa.Float)
    )


@set_schema('sor')
def downgrade():
    op.drop_table('acebook_ads_media_costs')
