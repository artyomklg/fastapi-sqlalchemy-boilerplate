from typing import Protocol, runtime_checkable

from sqlalchemy.ext.asyncio import AsyncSession


@runtime_checkable
class ITransactionContext(Protocol):
    def get_session(self) -> AsyncSession: ...

    async def commit(self): ...

    async def rollback(self): ...
