from dataclasses import dataclass
from typing import Any, Generic

from sqlalchemy import ColumnExpressionArgument, UnaryExpression, select

from src.infra.database.models import ORMModelT
from src.infra.database.repositories.mixins import SqlalchemySessionMixin


@dataclass
class SqlalchemyGenericRepository(SqlalchemySessionMixin, Generic[ORMModelT]):
    orm_model: type[ORMModelT]

    async def get_all(self):
        query = select(self.orm_model)
        result = await self._session.execute(query)
        return result.scalars().all()

    def _get_filtered_query(
        self,
        filters: tuple[ColumnExpressionArgument] = tuple(),
        order_by: tuple[UnaryExpression] = tuple(),
        limit: int | None = None,
        offset: int | None = None,
    ):
        query = select(self.orm_model).filter(*filters).order_by(*order_by)
        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)
        return query

    async def get_filtered(
        self,
        filters: tuple[ColumnExpressionArgument] = tuple(),
        order_by: tuple[UnaryExpression] = tuple(),
        limit: int | None = None,
        offset: int | None = None,
    ):
        query = self._get_filtered_query(filters, order_by, limit, offset)
        result = await self._session.execute(query)
        return result.scalars().all()

    async def get_one_filtered(
        self,
        filters: tuple[ColumnExpressionArgument] = tuple(),
        order_by: tuple[UnaryExpression] = tuple(),
        limit: int | None = None,
    ):
        query = self._get_filtered_query(filters, order_by, limit)
        result = await self._session.execute(query)
        return result.scalar_one()

    async def lock_by_id(self, id_: Any):
        if not hasattr(self.orm_model, "id"):
            raise
        query = select(self.orm_model).with_for_update().filter_by(id=id_)
        result = await self._session.execute(query)
        return result.scalar_one()

    async def add(self, instance: ORMModelT):
        self._session.add(instance)
        await self._session.flush()
        return await self._session.merge(instance)
