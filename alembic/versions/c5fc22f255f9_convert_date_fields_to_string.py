"""convert date fields to string

Revision ID: c5fc22f255f9
Revises: 8547c395e615
Create Date: 2021-05-01 10:44:55.171503

"""
from alembic import op
import sqlalchemy as sa
from app.utils.set_schema import set_schema


# revision identifiers, used by Alembic.
revision = 'c5fc22f255f9'
down_revision = '8547c395e615'
branch_labels = None
depends_on = None


@set_schema('sor')
def upgrade():
    op.alter_column(
        'facebook_ads_media_costs',
        'date',
        type_=sa.String(10)
    )
    op.alter_column(
        'google_ads_media_costs',
        'date',
        type_=sa.String(10)
    )
    op.alter_column(
        'pageviews',
        'date',
        type_=sa.String(10)
    )
    op.alter_column(
        'customer_leads',
        'signed_at',
        type_=sa.String(10)
    )
    op.alter_column(
        'customer_leads',
        'credit_decision_at',
        type_=sa.String(10)
    )
    op.alter_column(
        'customer_leads',
        'registered_at',
        type_=sa.String(10)
    )


@set_schema('sor')
def downgrade():
    op.alter_column(
        'facebook_ads_media_costs',
        'date',
        type_=sa.types.Date,
        postgresql_using='date::date'
    )
    op.alter_column(
        'google_ads_media_costs',
        'date',
        type_=sa.types.Date,
        postgresql_using='date::date'
    )
    op.alter_column(
        'pageviews',
        'date',
        type_=sa.types.Date,
        postgresql_using='date::date'
    )
    op.alter_column(
        'customer_leads',
        'signed_at',
        type_=sa.types.Date,
        postgresql_using='date::date'
    )
    op.alter_column(
        'customer_leads',
        'credit_decision_at',
        type_=sa.types.Date,
        postgresql_using='date::date'
    )
    op.alter_column(
        'customer_leads',
        'registered_at',
        type_=sa.types.Date,
        postgresql_using='date::date'
    )
