"""init

Revision ID: 6383ce1120c9
Revises: 
Create Date: 2021-09-18 13:40:24.159745

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '6383ce1120c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'task',
        sa.Column('task_uuid', UUID(as_uuid=True), primary_key=True),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('params', sa.JSON, nullable=False),
    )


def downgrade():
    op.drop_table('task')
