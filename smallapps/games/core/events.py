from collections import OrderedDict
from typing import (
    Any,
    Dict,
    OrderedDict as OrderedDictType,
    Callable, List, Iterable,
)

from pygame.event import Event

from smallapps.games.core.entity import Entity
from smallapps.games.core.singleton import singleton


class BaseEvent:
    event_type: str
    sender: Entity
    additional_data: Dict[str, Any]

    def __init__(self, sender: Entity) -> None:
        self.sender = sender


class PygameEvent(BaseEvent):
    event_type = 'PygameEvent'
    raw_event: Event

    def __init__(self, sender: Any, event: Event) -> None:
        super().__init__(sender)

        self.raw_event = event


@singleton
class EventEmitter(Entity):
    def __init__(self):
        super().__init__()

        self.event_listeners: OrderedDictType[str, List[Callable]] = OrderedDict()

    def emit(self, event: BaseEvent):
        listeners = self.event_listeners.get(event.event_type, [])

        for listener in listeners:
            listener(event)

    def subscribe(self, event_type: str, subscriber: Callable):
        if event_type in self.event_listeners:
            if subscriber in self.event_listeners[event_type]:
                return
            self.event_listeners[event_type].append(subscriber)
        else:
            self.event_listeners[event_type] = [subscriber]

    def unsubscribe(self, event_type: str, subscriber: Callable):
        if event_type in self.event_listeners and subscriber in self.event_listeners[event_type]:
            self.event_listeners[event_type].remove(subscriber)

            if not self.event_listeners[event_type]:
                self.event_listeners.pop(event_type)

    def events(self) -> Iterable[str]:
        return self.event_listeners.keys()

    def listeners(self, event: str) -> List[Callable]:
        return self.event_listeners.get(event, [])
