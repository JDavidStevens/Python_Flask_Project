"""empty message

Revision ID: 78565b4cafd1
Revises: 63a64d5e90ff
Create Date: 2024-10-03 08:53:21.776652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78565b4cafd1'
down_revision = '63a64d5e90ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
