"""convert customer_leads fields to string

Revision ID: 996010f8f5b1
Revises: 85be756a0d5b
Create Date: 2021-05-01 13:54:34.470856

"""
from alembic import op
import sqlalchemy as sa
from app.utils.set_schema import set_schema


# revision identifiers, used by Alembic.
revision = '996010f8f5b1'
down_revision = '85be756a0d5b'
branch_labels = None
depends_on = None


@set_schema('sor')
def upgrade():
    op.alter_column(
        'customer_leads',
        'lead_id',
        type_=sa.String(256)
    )
    op.alter_column(
        'customer_leads',
        'revenue',
        type_=sa.String(256)
    )
    op.alter_column(
        'customer_leads',
        'registered_at',
        type_=sa.String(28)
    )
    op.alter_column(
        'customer_leads',
        'credit_decision_at',
        type_=sa.String(28)
    )
    op.alter_column(
        'customer_leads',
        'signed_at',
        type_=sa.String(28)
    )


@set_schema('sor')
def downgrade():
    op.alter_column(
        'customer_leads',
        'lead_id',
        type_=sa.BIGINT,
        postgresql_using="lead_id::bigint"
    )
    op.alter_column(
        'customer_leads',
        'revenue',
        type_=sa.Float,
        postgresql_using="revenue::double precision"
    )
    op.alter_column(
        'customer_leads',
        'registered_at',
        type_=sa.String(10)
    )
    op.alter_column(
        'customer_leads',
        'credit_decision_at',
        type_=sa.String(10)
    )
    op.alter_column(
        'customer_leads',
        'signed_at',
        type_=sa.String(10)
    )
