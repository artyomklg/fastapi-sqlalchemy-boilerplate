from typing import Callable, NewType, TypeAlias

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

ROAsyncEngine = NewType("ROAsyncEngine", AsyncEngine)
ROasync_sessionmaker = NewType("ROasync_sessionmaker", async_sessionmaker[AsyncSession])
ROAsyncSession = NewType("ROAsyncSession", AsyncSession)
AsyncSessionFactory: TypeAlias = Callable[[], AsyncSession]
ROAsyncSessionFactory: TypeAlias = Callable[[], ROAsyncSession]

__all__ = [
    "ROAsyncEngine",
    "ROasync_sessionmaker",
    "AsyncSessionFactory",
    "ROAsyncSessionFactory",
]
