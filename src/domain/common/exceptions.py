from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class AppError(Exception):
    """Base Error"""

    status: ClassVar[int] = 500

    @property
    def message(self) -> str:
        return "An app error occurred"


class DomainError(AppError):
    """Base Domain Error"""

    @property
    def message(self) -> str:
        return "A domain error occurred"
