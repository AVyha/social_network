"""add author_od column in post table

Revision ID: c5be75b8e1c2
Revises: d9c95a0a3c22
Create Date: 2023-05-05 10:30:49.866429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5be75b8e1c2'
down_revision = 'd9c95a0a3c22'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_followers_id'), 'followers', ['id'], unique=False)
    op.add_column('post', sa.Column('author_id', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'author_id')
    op.drop_index(op.f('ix_followers_id'), table_name='followers')
    # ### end Alembic commands ###