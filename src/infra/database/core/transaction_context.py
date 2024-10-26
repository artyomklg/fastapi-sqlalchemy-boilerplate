from dataclasses import dataclass
from types import TracebackType

from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.core.connections_manager import DatabaseConnectionsManager


@dataclass
class DBTransactionContext:
    _db_conn_manager: DatabaseConnectionsManager
    _session: AsyncSession | None = None
    _closed: bool = False

    async def __aenter__(self):
        self._session = self.get_session()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        exc_traceback: TracebackType | None,
    ):
        if exc_value:
            await self.get_session().rollback()
        await self._close_transaction()

    def get_session(self):
        if self._closed:
            raise  # TODO ошибка
        if self._session is None:
            self._session = self._db_conn_manager.start_transaction()
        return self._session

    async def commit(self):
        await self.get_session().commit()
        await self._close_transaction()

    async def rollback(self):
        await self.get_session().rollback()

    async def _close_transaction(self):
        await self.get_session().close()
        self._closed = True
