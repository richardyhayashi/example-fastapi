"""add content column to post table

Revision ID: c4dc2a3beec7
Revises: d6d4978ff7f1
Create Date: 2025-10-02 20:48:20.203492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4dc2a3beec7'
down_revision: Union[str, Sequence[str], None] = 'd6d4978ff7f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
