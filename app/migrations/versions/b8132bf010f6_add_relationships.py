"""add relationships

Revision ID: b8132bf010f6
Revises: 4d641c65d09d
Create Date: 2023-06-28 10:41:18.836258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8132bf010f6'
down_revision = '4d641c65d09d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('gardens', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'plants', ['plant_id'], ['id'])
        batch_op.create_foreign_key(None, 'gardeners', ['gardener_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('gardens', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###