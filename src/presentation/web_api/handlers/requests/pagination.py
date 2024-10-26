from typing import Annotated

from fastapi import Query
from pydantic import BaseModel


class PaginationQuery(BaseModel):
    page: Annotated[int, Query(default=1)]
    per_page: Annotated[int | None, Query(default=None, le=1000)]
