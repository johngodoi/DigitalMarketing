"""convert pageviews campaign_id and ad_creative_id types for string

Revision ID: 28f698dcce3c
Revises: 996010f8f5b1
Create Date: 2021-05-01 18:27:40.635288

"""
from alembic import op
import sqlalchemy as sa
from app.utils.set_schema import set_schema


# revision identifiers, used by Alembic.
revision = '28f698dcce3c'
down_revision = '996010f8f5b1'
branch_labels = None
depends_on = None


@set_schema('sor')
def upgrade():
    op.alter_column(
        'pageviews',
        'date',
        new_column_name='datetime',
        type_=sa.String(28)
    )
    op.alter_column(
        'pageviews',
        'IP',
        new_column_name='ip_address'
    )
    op.alter_column(
        'pageviews',
        'campaign_id',
        type_=sa.String(20)
    )
    op.alter_column(
        'pageviews',
        'ad_creative_id',
        type_=sa.String(20)
    )


@set_schema('sor')
def downgrade():
    op.alter_column(
        'pageviews',
        'datetime',
        new_column_name='date',
        type_=sa.String(10)
    )
    op.alter_column(
        'pageviews',
        'ip_address',
        new_column_name='IP'
    )
    op.alter_column(
        'pageviews',
        'campaign_id',
        type_=sa.BIGINT,
        postgresql_using="campaign_id::bigint"
    )
    op.alter_column(
        'pageviews',
        'ad_creative_id',
        type_=sa.BIGINT,
        postgresql_using="ad_creative_id::bigint"
    )
