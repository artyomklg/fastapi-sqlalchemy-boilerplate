from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    db_user: str = "postgres"
    db_password: str = "postgres"
    db_host: str = "127.0.0.1"
    db_port: int = 5432
    db_name: str = "postgres"

    db_pool_size: int = 5
    db_ro_pool_size: int = 20

    @cached_property
    def db_uri(self) -> str:
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database_name}".format(
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database_name=self.db_name,
        )
