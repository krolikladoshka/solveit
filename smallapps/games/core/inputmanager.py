from typing import Any

import pygame
from pygame.event import Event

from smallapps.games.core.entity import Entity
from smallapps.games.core.events import BaseEvent, PygameEvent, EventEmitter
from smallapps.games.core.singleton import singleton


class MouseButtonUpEvent(PygameEvent):
    event_type: str = 'MouseButtonUpEvent'

    button: int

    def __init__(self, sender: Any, event: Event) -> None:
        super().__init__(sender, event)

        self.button = event.button


class GameQuitEvent(BaseEvent):
    event_type: str = 'GameQuitEvent'

    def __init__(self, sender: 'InputManager'):
        super().__init__(sender)


class MouseMotionEvent(PygameEvent):
    event_type: str = 'MouseMotionEvent'

    def __init__(self, sender: Any, event: Event) -> None:
        super().__init__(sender, event)
        self.position = event.pos


@singleton
class InputManager(Entity):
    def __init__(self):
        super().__init__()

        self.event_emitter: EventEmitter = EventEmitter()

    def update(self, delta_time: int):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.event_emitter.emit(GameQuitEvent(self))
            elif event.type == pygame.MOUSEMOTION:
                self.event_emitter.emit(MouseMotionEvent(self, event))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                self.event_emitter.emit(MouseButtonUpEvent(self, event))
            elif event.type == pygame.MOUSEMOTION:
                pass
