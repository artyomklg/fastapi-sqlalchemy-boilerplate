from dataclasses import dataclass, field
from functools import lru_cache

from src.infra.database.config import DatabaseConfig


@dataclass
class MainConfig:
    db: DatabaseConfig = field(default_factory=DatabaseConfig)


@lru_cache(1)
def get_main_config():
    return MainConfig()


def init_main_config():
    return get_main_config()
