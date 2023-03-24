import sys
from os.path import dirname, join
from typing import Optional

import pygame
from pygame.time import Clock

from smallapps.games.core.entity import Entity, PositionComponent, TransformComponent
from smallapps.games.core.events import EventEmitter
from smallapps.games.core.singleton import singleton
from smallapps.games.zuma.gameplay.leguha import Leguha
from smallapps.games.zuma.gameplay.path import NotSoRandomPath
from smallapps.games.core.gameobjectsmanager import GameObjectsManager
from smallapps.games.core.inputmanager import InputManager, GameQuitEvent
from smallapps.games.zuma.managers.tilemanager import MainTile

ASSETS_PATH = join(dirname(__file__), 'assets')

WINSIZE = (1280, 800)


class Rectangle(Entity):
    def __init__(self, w, h, name: str = '', parent: Optional['Entity'] = None):
        super().__init__(name, parent)
        self.width = w
        self.height = h
        self.transform: TransformComponent = self.add_component(TransformComponent)
        self.rect = (
            (-self.width / 2, -self.height / 2),
            (-self.width / 2, self.height / 2),
            (self.width / 2, self.height / 2),
            (self.width / 2, -self.height / 2)
        )

    def draw(self, screen):
        new_rect = [
            self.transform.apply(point)
            for point in self.rect
        ]
        pygame.draw.polygon(screen, (255, 255, 255), new_rect, 2)


@singleton
class Zuma(Entity):
    def __init__(self, frame_rate: int = 60):
        super().__init__()

        assets_path: str = join(dirname(__file__), 'assets/')
        self.tile_manager: MainTile = MainTile(assets_path)
        self.event_emitter: EventEmitter = EventEmitter()
        self.input_manager: InputManager = InputManager()
        self.stopped: bool = False
        self.frame_rate: int = frame_rate
        self.clock: Clock = Clock()
        self.screen: Optional[pygame.Surface] = None
        self.objects_manager: GameObjectsManager = GameObjectsManager()
        self.leguha: Leguha = None
        self.path = None

    def run(self):
        self.event_emitter.subscribe(GameQuitEvent.event_type, self.stop_game)

        pygame.init()
        self.screen = pygame.display.set_mode(WINSIZE, pygame.DOUBLEBUF)
        self.tile_manager.load()

        self.leguha = Leguha()
        leguha_position: PositionComponent = self.leguha.get_component(PositionComponent)
        leguha_position.position = leguha_position.position + pygame.Vector2(1280 / 2, 800 / 2)
        size = 10
        width, height = WINSIZE[0] / size, WINSIZE[1] / size
        self.path = NotSoRandomPath(size, size, width, height, [self.leguha])

        self.objects_manager.instantiate(self.leguha, 'main')
        self.objects_manager.instantiate(self.path, 'main')

        while not self.stopped:
            self.screen.fill((255, 255, 255))

            delta_time = self.clock.tick(self.frame_rate)
            self.update(delta_time)
            self.draw(self.screen)

            pygame.display.flip()

    def stop_game(self, event: GameQuitEvent):
        self.stopped = True

    def update(self, delta_time: int):
        self.input_manager.update(delta_time)

        self.objects_manager.update(delta_time)
        # self.leguha.update(delta_time)
        # self.path.update(delta_time)

        super().update(delta_time)

    def draw(self, screen: pygame.Surface):
        super().draw(screen)

        self.objects_manager.draw(screen)
        # self.leguha.draw(screen)

        # self.path.draw(screen)

        # pygame.draw.line(screen, (255, 0, 0), (0, 800 / 2), (1280, 800 / 2))
        # pygame.draw.line(screen, (255, 0, 0), (1280 / 2, 0), (1280 / 2, 800))


def main():
    # TODO: bezier derivatives are wrong (edgy bezier movement)
    # TODO: alpha masks for sprites (black/white background is drawn)
    # TODO: zuma algorithm is wrong for edge cases
    sys.setrecursionlimit(2500)
    zuma = Zuma()

    zuma.run()
