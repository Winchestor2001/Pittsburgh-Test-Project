"""create models

Revision ID: 7fbabd5bb0f9
Revises: 15384aadc627
Create Date: 2024-11-28 17:02:04.721382

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7fbabd5bb0f9"
down_revision: Union[str, None] = "15384aadc627"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("verification_code", sa.String(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "verification_code")
    # ### end Alembic commands ###