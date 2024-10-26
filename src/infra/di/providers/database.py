from dishka import Provider, Scope, provide

from src.application.protocols.transaction_context import ITransactionContext
from src.infra.database.core.connections_manager import DatabaseConnectionsManager
from src.infra.database.core.transaction_context import DBTransactionContext


class DatabaseProvider(Provider):
    db_conn_manager = provide(DatabaseConnectionsManager, scope=Scope.APP)

    @provide(provides=ITransactionContext, scope=Scope.REQUEST)
    async def transaction_context(self, db_conn_manager: DatabaseConnectionsManager):
        async with DBTransactionContext(db_conn_manager) as tc:
            yield tc
