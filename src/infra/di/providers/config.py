from dishka import Provider, Scope, provide

from src.infra.main_config import MainConfig


class ConfigProvider(Provider):
    scope = Scope.APP

    main_config = provide(MainConfig)
