from dataclasses import dataclass, field

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.session import _SessionCloseState

from src.infra.database.core.protocols import AsyncSessionFactory


@dataclass
class SqlalchemySessionMixin:
    _session_factory: AsyncSessionFactory
    __sessions: set[AsyncSession] = field(init=False, default_factory=set)

    @property
    def _session(self) -> AsyncSession:
        session = self._session_factory()
        self.__sessions.add(session)
        return session

    async def _close_sessions(self):
        for session in self.__sessions:
            if session.sync_session._close_state is not _SessionCloseState.CLOSED:
                await session.close()
        self.__sessions.clear()
