"""added subcategory to products

Revision ID: 4a68f1941bf7
Revises: 85a31ab95e83
Create Date: 2022-10-28 16:08:07.698457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a68f1941bf7'
down_revision = '85a31ab95e83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('subcategory', sa.String(), nullable=False))
    op.drop_column('products', 'sybcategory')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('sybcategory', sa.VARCHAR(), nullable=False))
    op.drop_column('products', 'subcategory')
    # ### end Alembic commands ###