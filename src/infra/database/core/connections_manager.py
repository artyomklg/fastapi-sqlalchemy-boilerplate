from dataclasses import dataclass

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.infra.database.config import DatabaseConfig


@dataclass
class DatabaseConnectionsManager:
    _db_config: DatabaseConfig
    _engine: AsyncEngine | None = None
    _ro_engine: AsyncEngine | None = None
    _session_factory: async_sessionmaker[AsyncSession] | None = None
    _ro_session_factory: async_sessionmaker[AsyncSession] | None = None

    def _get_engine(self) -> AsyncEngine:
        if self._engine is None:
            self._engine = create_async_engine(
                self._db_config.db_uri,
                pool_size=self._db_config.db_pool_size,
            )
        return self._engine

    def _get_ro_engine(self) -> AsyncEngine:
        if self._ro_engine is None:
            self._ro_engine = create_async_engine(
                self._db_config.db_uri,
                pool_size=self._db_config.db_ro_pool_size,
            )
        return self._ro_engine

    def _get_session_factory(self) -> async_sessionmaker[AsyncSession]:
        if self._session_factory is None:
            self._session_factory = async_sessionmaker(
                autocommit=False,
                autoflush=False,
                expire_on_commit=True,
                bind=self._get_engine(),
            )
        return self._session_factory

    def _get_ro_session_factory(self) -> async_sessionmaker[AsyncSession]:
        if self._ro_session_factory is None:
            self._ro_session_factory = async_sessionmaker(
                isolation_level="AUTOCOMMIT",
                bind=self._get_ro_engine(),
            )
        return self._ro_session_factory

    def start_transaction(self):
        return self._get_session_factory()()

    def get_read_only_session(self):
        return self._get_ro_session_factory()()
