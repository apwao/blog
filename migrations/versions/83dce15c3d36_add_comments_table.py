"""Add comments table

Revision ID: 83dce15c3d36
Revises: 75844bac4c9d
Create Date: 2019-06-10 15:23:11.647466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83dce15c3d36'
down_revision = '75844bac4c9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('postedAt', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###