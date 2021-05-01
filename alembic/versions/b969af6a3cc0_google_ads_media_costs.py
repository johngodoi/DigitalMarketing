"""google_ads_media_costs

Revision ID: b969af6a3cc0
Revises: 2cccdcd85ca6
Create Date: 2021-05-01 09:39:03.069818

"""
from alembic import op
import sqlalchemy as sa
from app.utils.set_schema import set_schema


# revision identifiers, used by Alembic.

revision = 'b969af6a3cc0'
down_revision = '2cccdcd85ca6'
branch_labels = None
depends_on = None


@set_schema('sor')
def upgrade():
    op.create_table(
        'google_ads_media_costs',
        sa.Column('date', sa.Date),
        sa.Column('campaign_id', sa.BIGINT),
        sa.Column('campaign_name', sa.String(256)),
        sa.Column('ad_creative_id', sa.BIGINT),
        sa.Column('ad_creative_name', sa.String(256)),
        sa.Column('clicks', sa.BIGINT),
        sa.Column('impressions', sa.BIGINT),
        sa.Column('cost', sa.Float)
    )


@set_schema('sor')
def downgrade():
    op.drop_table('google_ads_media_costs')
