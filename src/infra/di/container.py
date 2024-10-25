from functools import lru_cache

from dishka import make_async_container

from src.infra.di.providers.config import ConfigProvider


@lru_cache(1)
def get_container():
    return make_async_container(
        ConfigProvider(),
    )
