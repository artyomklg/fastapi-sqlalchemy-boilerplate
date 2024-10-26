from datetime import datetime
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column


class IntIdORMMixin:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class UuidIdORMMixin:
    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=True)


class CreatedAtORMMixin:
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))


class UpdatedAtORMMixin:
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        server_onupdate=text("TIMEZONE('utc', now())"),
    )
