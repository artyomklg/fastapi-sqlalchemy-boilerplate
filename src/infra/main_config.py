from dataclasses import dataclass, field
from functools import lru_cache


@dataclass
class MainConfig: ...


@lru_cache(1)
def get_main_config():
    return MainConfig()
