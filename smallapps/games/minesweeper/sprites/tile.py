from enum import Enum
from os.path import join, dirname
from typing import List, Dict, Set

from pygame import image, Surface, Rect
from pygame.draw_py import Point


class FieldSprites(Enum):
    closed = 'closed'
    empty = 'empty'
    flagged = 'flagged'
    question_mark = 'question_mark'
    question_mark_pressed = 'question_mark_pressed'
    mine = 'mine'
    clicked_mine = 'clicked_mine'
    crossed_mine = 'crossed_mine'
    digit = 'digit'

    @staticmethod
    def digits() -> Set['FieldSprites']:
        return {FieldSprites.digit, FieldSprites.empty}


class MainTile:
    tile = None

    def __init__(self):
        self.tile_path: str = join(join(dirname(dirname(__file__)), 'assets'), '2000.png')
        self.sprite_size: int = 15
        self.margin_right = 1
        self.starting_point: Point = Point(x=0, y=0)
        self.tile: Surface = image.load(self.tile_path).convert()
        self.rect: Rect = self.tile.get_rect()
        self.fields: Dict[str, Surface] = {}
        self.digits: List[Surface] = []

        dx = self.sprite_size + self.margin_right
        for x, field in zip(range(0, self.rect.size[0], dx), FieldSprites):
            field_surface = Surface((self.sprite_size, self.sprite_size))
            field_surface.blit(self.tile, (0, 0), (x, 0, self.sprite_size, self.sprite_size))
            self.fields[field.value] = field_surface

            digit_surface = Surface((self.sprite_size, self.sprite_size))
            digit_surface.blit(self.tile, (0, 0), (x, self.sprite_size, self.sprite_size, self.sprite_size))
            self.digits.append(digit_surface)

        self.digits = [self.fields['empty']] + self.digits

    @property
    def rows(self) -> int:
        return self.tile.get_size()[1] // self.sprite_size

    @property
    def columns(self) -> int:
        return (self.tile.get_size()[0] + self.margin_right) // (self.sprite_size + self.margin_right)


def init_main_tile():
    if not MainTile.tile:
        MainTile.tile = MainTile()
