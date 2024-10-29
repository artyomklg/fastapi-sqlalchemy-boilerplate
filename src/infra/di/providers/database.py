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


#!
#! Пример создания обычных и ReadOnly репозиториев .
#! Тут насрано жидко пока. Но я думаю как без этого автоматом закрывать сессии на каждом запросе
#!

# class SomeReader(Protocol):
#     async def get_one(self) -> int: ...

# class SomeRepo(SomeReader, Protocol): ...

# @dataclass
# class SqlalchemySomeRepository(SqlalchemySessionMixin):
#     g_repo: SqlalchemyGenericRepository[SomeORM]

#     async def get_one(self) -> int:
#         res = await self._session.execute(text("select 1")) # ну допустим
#         return res.scalar_one()

# class SomeProvider(Provider):
#     scope = Scope.REQUEST

#     @provide(provides=SomeReader)
#     async def some_reader(self, session_factory: ROAsyncSessionFactory):
#         reader = SqlalchemySomeRepository(
#             session_factory, SqlalchemyGenericRepository(session_factory, SomeORM)
#         )
#         yield reader
#         await (  #? мдаааааа, а по другому не работает нихуя. gb сессии не чистит
#             reader._close_sessions()
#         )

# @provide(provides=SomeRepo)
# async def some_repo(self, session_factory: AsyncSessionFactory):
#     repo = SqlalchemySomeRepository(
#         session_factory, SqlalchemyGenericRepository(session_factory, SomeORM)
#     )
#     yield repo
#     await reader._close_sessions()
