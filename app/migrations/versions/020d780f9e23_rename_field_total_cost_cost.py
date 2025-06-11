"""rename field total_cost -> cost

Revision ID: 020d780f9e23
Revises: faeea02286e3
Create Date: 2025-06-11 19:41:48.591069

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "020d780f9e23"
down_revision: str | None = "faeea02286e3"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Переименовываем колонку total_cost → cost в таблице specialties
    op.alter_column("specialties", "total_cost", new_column_name="cost")


def downgrade() -> None:
    # Возвращаем обратно: cost → total_cost
    op.alter_column("specialties", "cost", new_column_name="total_cost")
