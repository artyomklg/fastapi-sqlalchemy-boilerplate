from dataclasses import dataclass


@dataclass(eq=False)
class AppError(Exception):
    """Base Error"""

    @property
    def message(self) -> str:
        return "An app error occurred"


class DomainError(AppError):
    """Base Domain Error"""

    @property
    def message(self) -> str:
        return "A domain error occurred"
