# https://leetcode.com/problems/check-knight-tour-configuration
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        if grid[0][0] != 0:
            return False

        directions = (
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1),
        )

        def can_visit(i, j) -> bool:
            if i < 0 or i >= n or j < 0 or j >= n:
                return False
            return grid[i][j] >= 0

        i, j = 0, 0
        step = 0
        while step < (n * n - 1):
            found = False

            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if can_visit(next_i, next_j) and grid[next_i][next_j] == step + 1:
                    i, j = next_i, next_j
                    grid[i][j] = -1
                    found = True

                    break
            if not found:
                return False
            step += 1
        return True
