from dataclasses import dataclass
from types import TracebackType

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class DBTransactionContext:
    _session: AsyncSession

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        exc_traceback: TracebackType | None,
    ):
        if exc_value:
            await self._session.rollback()
        else:
            await self._close_transaction()

    async def commit(self):
        await self._session.commit()
        await self._close_transaction()

    async def rollback(self):
        await self._session.rollback()
        await self._close_transaction()

    async def _close_transaction(self):
        await self._session.close()
