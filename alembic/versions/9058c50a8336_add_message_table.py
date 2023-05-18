"""add message table

Revision ID: 9058c50a8336
Revises: 155b7248e15c
Create Date: 2023-05-08 13:08:59.317532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9058c50a8336'
down_revision = '155b7248e15c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=255), nullable=False),
    sa.Column('from_user', sa.UUID(), nullable=True),
    sa.Column('to_user', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['from_user'], ['user.id'], ),
    sa.ForeignKeyConstraint(['to_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###