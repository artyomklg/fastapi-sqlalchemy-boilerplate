from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.application.protocols.transaction_context import ITransactionContext
from src.infra.database.config import DatabaseConfig
from src.infra.database.core.protocols import (
    AsyncSessionFactory,
    ROasync_sessionmaker,
    ROAsyncEngine,
    ROAsyncSessionFactory,
)
from src.infra.database.core.transaction_context import DBTransactionContext


class SqlAlchemySessionProvider(Provider):
    @provide(scope=Scope.APP, provides=AsyncEngine)
    def engine(self, db_config: DatabaseConfig):
        return create_async_engine(
            db_config.uri, pool_size=db_config.pool_size, echo=db_config.echo
        )

    @provide(scope=Scope.APP, provides=async_sessionmaker[AsyncSession])
    def async_session_maker(self, engine: AsyncEngine):
        return async_sessionmaker(
            autocommit=False,
            autoflush=False,
            expire_on_commit=True,
            bind=engine,
        )

    @provide(scope=Scope.APP, provides=ROAsyncEngine)
    def ro_engine(self, db_config: DatabaseConfig):
        return create_async_engine(
            db_config.ro_uri,
            pool_size=db_config.ro_pool_size,
            echo=db_config.ro_echo,
        )

    @provide(scope=Scope.APP, provides=ROasync_sessionmaker)
    def ro_async_session_maker(self, engine: ROAsyncEngine):
        return async_sessionmaker(
            isolation_level="AUTOCOMMIT",
            bind=engine,
        )

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def session(self, async_session_maker: async_sessionmaker[AsyncSession]):
        async with async_session_maker() as session:
            yield session

    @provide(scope=Scope.REQUEST, provides=AsyncSessionFactory)
    def async_session_factory(self, session: AsyncSession):
        return lambda: session

    @provide(scope=Scope.REQUEST, provides=ROAsyncSessionFactory)
    def ro_async_session_factory(self, ro_async_session_maker: ROasync_sessionmaker):
        return ro_async_session_maker

    @provide(provides=ITransactionContext, scope=Scope.REQUEST)
    async def transaction_context(self, session: AsyncSession):
        async with DBTransactionContext(session) as tc:
            yield tc
