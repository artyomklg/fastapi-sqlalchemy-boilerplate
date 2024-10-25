from dishka import Provider, Scope, provide

from src.infra.main_config import MainConfig, get_main_config


class ConfigProvider(Provider):
    scope = Scope.APP

    main_config = provide(get_main_config, provides=MainConfig)
