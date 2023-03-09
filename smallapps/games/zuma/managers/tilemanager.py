from enum import Enum
from os.path import join
from typing import Dict, Optional, List

from pygame import image, Surface, Rect
from pygame.draw_py import Point

from smallapps.games.core.entity import Entity
from smallapps.games.core.singleton import singleton


class Sprites(Enum):
    blue = 'blue'
    yellow = 'yellow'
    green = 'green'
    red = 'red'
    purple = 'purple'
    white = 'white'
    frog = 'frog'
    pit = 'pit'

    @staticmethod
    def colors() -> List['Sprites']:
        return [
            Sprites.blue, Sprites.yellow, Sprites.green,
            Sprites.red, Sprites.purple, Sprites.white,
        ]


@singleton
class MainTile(Entity):
    def __init__(self, assets_path: Optional[str] = None):
        super().__init__()

        self.assets_path: str = assets_path
        self.balls_path: str = join(self.assets_path, 'balls.png')
        self.frog_path: str = join(self.assets_path, 'frog.png')
        self.pit_path: str = join(self.assets_path, 'pit.png')
        self.sprite_size_balls: int = 36
        self.sprite_size_frog: int = 106
        self.sprite_size_pit: int = 86
        self.starting_point: Point = Point(x=0, y=0)
        self.tile_balls: Optional[Surface] = None
        self.tile_frog: Optional[Surface] = None
        self.tile_pit: Optional[Surface] = None
        self.tile_balls_rect: Optional[Rect] = None
        self.sprites: Dict[Sprites, Surface] = {}
        self.colors: Dict[Sprites, Surface] = {}

    def load(self):
        self.tile_balls: Surface = image.load(self.balls_path)
        self.tile_frog: Surface = image.load(self.frog_path)
        self.tile_pit: Surface = image.load(self.pit_path)
        self.tile_balls_rect: Rect = self.tile_balls.get_rect()

        dx = self.sprite_size_balls
        for x, field in zip(range(0, self.tile_balls_rect.size[0], dx), Sprites.colors()):
            sprite_surface_balls = Surface((self.sprite_size_balls, self.sprite_size_balls))
            sprite_surface_balls.blit(self.tile_balls, (0, 0), (x, 0, self.sprite_size_balls, self.sprite_size_balls))
            self.sprites[field] = sprite_surface_balls
            self.colors[field] = sprite_surface_balls

        self.sprites[Sprites.frog] = self.tile_frog
        self.sprites[Sprites.pit] = self.tile_pit
