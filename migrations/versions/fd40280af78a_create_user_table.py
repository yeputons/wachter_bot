"""create user table

Revision ID: fd40280af78a
Revises: d3a10581c664
Create Date: 2018-06-10 16:43:36.824598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd40280af78a'
down_revision = 'd3a10581c664'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('whois', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('user_id', 'chat_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
