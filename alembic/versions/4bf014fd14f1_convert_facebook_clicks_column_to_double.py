"""convert facebook clicks column to double

Revision ID: 4bf014fd14f1
Revises: c5fc22f255f9
Create Date: 2021-05-01 11:04:59.521307

"""
from alembic import op
import sqlalchemy as sa
from app.utils.set_schema import set_schema


# revision identifiers, used by Alembic.
revision = '4bf014fd14f1'
down_revision = 'c5fc22f255f9'
branch_labels = None
depends_on = None


@set_schema('sor')
def upgrade():
    op.alter_column(
        'facebook_ads_media_costs',
        'clicks',
        type_=sa.Float
    )


@set_schema('sor')
def downgrade():
    op.alter_column(
        'facebook_ads_media_costs',
        'clicks',
        type_=sa.BIGINT
    )
