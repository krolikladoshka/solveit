import os
from typing import List, Dict

from pygame import image, Surface, Rect
from pygame.draw_py import Point


class MainTile:
    def __init__(self, assets_path: str):
        self.tile_path: str = os.path.join(assets_path, '2000.png')
        self.sprite_size: int = 15
        self.margin_right = 1
        self.starting_point: Point = Point(x=0, y=0)
        self.tile: Surface = image.load(self.tile_path).convert()
        self.rect: Rect = self.tile.get_rect()
        self.fields: Dict[str, Surface] = {}
        self.digits: List[Surface] = []

        self.fields_names = (
            'closed', 'empty',
            'flagged', 'question_mark',
            'question_mark_pressed', 'mine',
            'clicked_mine', 'crossed_mine',
        )
        dx = self.sprite_size + self.margin_right
        for x, name in zip(range(self.rect.size[0], dx), self.fields_names):
            field_surface = Surface((self.sprite_size, self.sprite_size))
            field_surface.blit(self.tile, (0, 0), (x, 0, self.sprite_size, self.sprite_size))
            self.fields[name] = field_surface

            digit_surface = Surface((self.sprite_size, self.sprite_size))
            digit_surface.blit(self.tile, (0, 0), (x, self.sprite_size, self.sprite_size, self.sprite_size))
            self.digits.append(digit_surface)

    @property
    def rows(self) -> int:
        return self.tile.get_size()[1] // self.sprite_size

    @property
    def columns(self) -> int:
        return (self.tile.get_size()[0] + self.margin_right) // (self.sprite_size + self.margin_right)

