from sqlalchemy.ext.asyncio import AsyncSession


class AutoCloseAsyncSession(AsyncSession):
    async def refresh(self, *args, **kwargs):
        result = await super().refresh(*args, **kwargs)
        await self.close()
        return result

    async def execute(self, *args, **kwargs):  # type: ignore
        result = await super().execute(*args, **kwargs)
        await self.close()
        return result

    async def scalar(self, *args, **kwargs):
        result = await super().scalar(*args, **kwargs)
        await self.close()
        return result

    async def scalars(self, *args, **kwargs):
        result = await super().scalars(*args, **kwargs)
        await self.close()
        return result

    async def get(self, *args, **kwargs):
        result = await super().get(*args, **kwargs)
        await self.close()
        return result

    async def get_one(self, *args, **kwargs):
        result = await super().get_one(*args, **kwargs)
        await self.close()
        return result

    async def delete(self, *args, **kwargs):
        result = await super().delete(*args, **kwargs)
        await self.close()
        return result

    async def merge(self, *args, **kwargs):
        result = await super().merge(*args, **kwargs)
        await self.close()
        return result

    async def flush(self, *args, **kwargs):
        await super().flush(*args, **kwargs)
        await self.close()
