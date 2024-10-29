import uuid
from datetime import datetime
from typing import Annotated

from sqlalchemy import BigInteger, Identity, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

IntPK = Annotated[int, mapped_column(BigInteger, Identity(), primary_key=True, autoincrement=True)]
UuidPK = Annotated[
    uuid.UUID,
    mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()")),
]


class CreatedAtORMMixin:
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))


class UpdatedAtORMMixin:
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        server_onupdate=text("TIMEZONE('utc', now())"),
    )
