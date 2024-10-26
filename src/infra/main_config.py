from dataclasses import dataclass, field
from functools import lru_cache

from src.infra.database.config import DatabaseConfig
from src.infra.log.config import LogConfig


@dataclass
class MainConfig:
    db: DatabaseConfig = field(default_factory=DatabaseConfig)
    log: LogConfig = field(default_factory=LogConfig)

    def __post_init__(self):
        """Validate config values"""


@lru_cache(1)
def get_main_config():
    return MainConfig()


def setup_main_config():
    return get_main_config()
