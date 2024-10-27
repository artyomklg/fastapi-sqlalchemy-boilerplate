from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_prefix="DB_")

    user: str = "postgres"
    password: str = "postgres"
    host: str = "127.0.0.1"
    port: int = 5432
    name: str = "postgres"

    pool_size: int = 5
    ro_pool_size: int = 20
    echo: bool = False
    ro_echo: bool = False

    @cached_property
    def uri(self) -> str:
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database_name}".format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database_name=self.name,
        )

    @cached_property
    def ro_uri(self) -> str:
        return self.uri
