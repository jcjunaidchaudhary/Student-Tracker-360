"""create user

Revision ID: ef267347142c
Revises: 
Create Date: 2023-08-04 10:43:00.271748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef267347142c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(64), nullable=True),
        sa.Column("email", sa.String(64), nullable=True),
        sa.Column("phone1", sa.String(10), nullable=True, default=""),
        sa.Column("_password", sa.String(300), nullable=True),
        sa.Column("last_login", sa.Date(), nullable=True),
        sa.Column(
            "modified_on",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("disabled", sa.Boolean(),default=False, nullable=True),
        sa.Column("modified_user_id", sa.Integer(), nullable=True),
        sa.CheckConstraint(
            "length(name) >= 3 AND length(name) <= 64", name="user_name_check"
        ),
        sa.CheckConstraint(
            "length(email) >= 3 AND length(email) <= 64", name="user_email_check"
        ),
        sa.CheckConstraint("length(phone1)=10 ", name="phone1_check"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("phone1"),
        sa.ForeignKeyConstraint(["modified_user_id"], ["user.id"]),
    )


def downgrade() -> None:
    op.drop_table("user")
