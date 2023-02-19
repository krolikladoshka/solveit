from typing import List, Set

from pygame.draw_py import Point
from pygame.sprite import Sprite

default_size = 10

class Field:
    def __init__(self, is_mine: bool = False):
        self.is_mine: bool = is_mine
        self.tile = None



class Board:
    def __init__(self, width: int = default_size, height: int = default_size):
        self.width = width
        self.height = height
        self.board: List[List[Field]] = [
            [Field() for i in range(self.width)]
            for _ in range(self.height)
        ]
        self.difficulty = 1
        self.mines_count: int = min(round(width * height / (20 // self.difficulty)), 3)
        self.mines: Set[Point] = set()

    def first_click(self):
        pass


