"""rename field specialty -> speciality

Revision ID: f78692c04243
Revises: 020d780f9e23
Create Date: 2025-06-11 20:54:58.049951

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f78692c04243"
down_revision: str | None = "020d780f9e23"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema: rename column 'specialty_id' to 'speciality_id in semesters."""
    op.alter_column(table_name="semesters", column_name="specialty_id", new_column_name="speciality_id")


def downgrade() -> None:
    """Downgrade schema: revert column name from 'speciality_id' to 'specialty_id."""
    op.alter_column(table_name="semesters", column_name="speciality_id", new_column_name="specialty_id")
