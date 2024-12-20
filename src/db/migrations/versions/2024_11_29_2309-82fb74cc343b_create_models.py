"""create models

Revision ID: 82fb74cc343b
Revises: 
Create Date: 2024-11-29 23:09:27.148325

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "82fb74cc343b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "categorys",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("obj_state", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("uuid", name=op.f("pk_categorys")),
    )
    op.create_table(
        "orders",
        sa.Column("product", sa.String(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("user", sa.String(), nullable=False),
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("obj_state", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("uuid", name=op.f("pk_orders")),
    )
    op.create_table(
        "users",
        sa.Column("full_name", sa.String(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("password", sa.LargeBinary(), nullable=False),
        sa.Column("role", sa.String(), nullable=False),
        sa.Column("verification_code", sa.String(), nullable=True),
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("obj_state", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("uuid", name=op.f("pk_users")),
        sa.UniqueConstraint("username", name=op.f("uq_users_username")),
    )
    op.create_table(
        "products",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("price", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("image", sa.String(), nullable=True),
        sa.Column("category_id", sa.String(length=36), nullable=False),
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("obj_state", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["categorys.uuid"],
            name=op.f("fk_products_category_id_categorys"),
        ),
        sa.PrimaryKeyConstraint("uuid", name=op.f("pk_products")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("products")
    op.drop_table("users")
    op.drop_table("orders")
    op.drop_table("categorys")
    # ### end Alembic commands ###
