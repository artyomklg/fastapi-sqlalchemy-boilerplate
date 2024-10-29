from functools import lru_cache

from dishka import make_async_container

from src.infra.di.providers import ConfigProvider, SqlAlchemySessionProvider
from src.infra.main_config import MainConfig, get_main_config


@lru_cache(1)
def get_container():
    return make_async_container(
        ConfigProvider(),
        SqlAlchemySessionProvider(),
        context={
            MainConfig: get_main_config(),
        },
    )


def init_container():
    return get_container()
