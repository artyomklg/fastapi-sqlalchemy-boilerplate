from dataclasses import dataclass, field

from sqlalchemy.ext.asyncio import AsyncSession

from src.application.protocols.transaction_context import ITransactionContext
from src.infra.database.core.connections_manager import DatabaseConnectionsManager


@dataclass
class DBSessionMixin:
    _tc: ITransactionContext | None = field(kw_only=True)
    _db_conn_manager: DatabaseConnectionsManager

    @property
    def _session(self) -> AsyncSession:
        if self._tc is None:
            return self._db_conn_manager.get_read_only_session()
        else:
            return self._tc.get_session()
