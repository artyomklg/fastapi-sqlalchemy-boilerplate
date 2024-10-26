from abc import ABC
from dataclasses import dataclass, field

from src.domain.common.events import Event


class Entity(ABC):
    pass


@dataclass
class AggregateRoot(Entity, ABC):
    _events: list[Event] = field(
        default_factory=list, init=False, repr=False, hash=False, compare=False
    )

    def record_event(self, event: Event) -> None:
        self._events.append(event)

    def pull_events(self) -> list[Event]:
        events = self._get_events().copy()
        self._clear_events()
        return events

    def _get_events(self) -> list[Event]:
        return self._events

    def _clear_events(self) -> None:
        self._events.clear()
