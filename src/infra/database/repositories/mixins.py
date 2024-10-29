from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.core.protocols import AsyncSessionFactory


@dataclass
class SqlalchemySessionMixin:
    _session_factory: AsyncSessionFactory

    @property
    def _session(self) -> AsyncSession:
        session = self._session_factory()
        return session
