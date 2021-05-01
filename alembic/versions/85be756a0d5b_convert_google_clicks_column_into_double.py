"""convert google clicks column into double

Revision ID: 85be756a0d5b
Revises: 4bf014fd14f1
Create Date: 2021-05-01 13:34:40.208873

"""
from alembic import op
import sqlalchemy as sa
from app.utils.set_schema import set_schema


# revision identifiers, used by Alembic.
revision = '85be756a0d5b'
down_revision = '4bf014fd14f1'
branch_labels = None
depends_on = None


@set_schema('sor')
def upgrade():
    op.alter_column(
        'google_ads_media_costs',
        'clicks',
        type_=sa.Float
    )


@set_schema('sor')
def downgrade():
    op.alter_column(
        'google_ads_media_costs',
        'clicks',
        type_=sa.BIGINT
    )
