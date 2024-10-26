from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

LOG_DEFAULT_FORMAT = (
    "%(asctime)s [%(process)d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


class LogConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    log_level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"] = "INFO"
    log_format: str = LOG_DEFAULT_FORMAT
    log_datefmt: str = "[%Y-%m-%d %H:%M:%S %z]"
