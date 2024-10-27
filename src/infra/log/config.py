from typing import Final, Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

LOG_DEFAULT_FORMAT: Final[str] = (
    "%(asctime)s [%(process)d] %(module)15s:%(lineno)-4d %(levelname)s - %(message)s"
)
LOG_DEFAULT_DATEFMT: Final[str] = "[%Y-%m-%d %H:%M:%S %z]"


class LogConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_prefix="LOG_")

    level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"] = "INFO"
    format: str = LOG_DEFAULT_FORMAT
    datefmt: str = LOG_DEFAULT_DATEFMT
    use_colors: bool = True
