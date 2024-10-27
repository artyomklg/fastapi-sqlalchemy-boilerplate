from dishka import Provider, Scope, from_context, provide

from src.infra.database.config import DatabaseConfig
from src.infra.log.config import LogConfig
from src.infra.main_config import MainConfig


class ConfigProvider(Provider):
    scope = Scope.APP

    main_config = from_context(MainConfig)

    @provide(provides=DatabaseConfig)
    def db_config(self, main_config: MainConfig):
        return main_config.db

    @provide(provides=LogConfig)
    def log_config(self, main_config: MainConfig):
        return main_config.log
