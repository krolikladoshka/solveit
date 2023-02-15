# https://leetcode.com/problems/detect-squares
from typing import Dict, Tuple, List


class Solution:
    def __init__(self):
        self.squares: Dict[Tuple, int] = {}

    def add(self, point: List[int]) -> None:
        self.squares[tuple(point)] = self.squares.setdefault(tuple(point), 0) + 1

    def on_same_diagonal(self, p1, p2) -> bool:
        return abs(p1[0] - p2[0]) == abs(p1[1] - p2[1])

    def count(self, point: List[int]) -> int:
        counter = 0
        point = tuple(point)
        for saved_point, count in self.squares.items():
            if saved_point != point and self.on_same_diagonal(point, saved_point):
                p1 = (saved_point[0], point[1])
                p2 = (point[0], saved_point[1])
                if p1 in self.squares and p2 in self.squares:
                    counter += 1
                    if self.squares[p1] > 1:
                        counter += self.squares[p1] - 1
                    if self.squares[p2] > 1:
                        counter += self.squares[p2] - 1
                    if count > 1:
                        counter += count - 1
        return counter


