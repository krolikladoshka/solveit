# https://leetcode.com/problems/line-reflection/
from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        leftmost_point_x = min(
            x
            for x, y in points
        )
        rightmost_point_x = max(
            x
            for x, y in points
        )
        middle = (rightmost_point_x + leftmost_point_x) / 2
        points = set(
            map(tuple, points)
        )
        for x, y in points:
            if x == middle:
                continue
            if (middle + middle - x, y) not in points:
                return False

        return True

