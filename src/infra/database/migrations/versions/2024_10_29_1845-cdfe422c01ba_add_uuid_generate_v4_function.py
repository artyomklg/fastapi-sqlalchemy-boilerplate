"""add uuid_generate_v4 function

Revision ID: cdfe422c01ba
Revises: c81cfc11b8c9
Create Date: 2024-10-29 18:45:12.770166

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "cdfe422c01ba"
down_revision: Union[str, None] = "c81cfc11b8c9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')


def downgrade() -> None:
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp";')
