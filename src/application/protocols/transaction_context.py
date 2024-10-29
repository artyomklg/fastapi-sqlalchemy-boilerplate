from typing import Protocol, runtime_checkable


@runtime_checkable
class ITransactionContext(Protocol):
    async def commit(self): ...

    async def rollback(self): ...
