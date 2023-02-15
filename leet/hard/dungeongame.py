# https://leetcode.com/problems/dungeon-game
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        columns = len(dungeon[0])
        dp = [[float('inf')] * columns for _ in range(rows)]

        def get_required_health(next_i, next_j, current_cell):
            if next_i >= rows or next_j >= columns:
                return float('inf')
            next_cell_heath = dp[next_i][next_j]

            if current_cell < 0:
                return next_cell_heath + abs(current_cell)
            if current_cell >= next_cell_heath:
                return 1
            return next_cell_heath - current_cell

        for i in range(rows - 1, -1, -1):
            for j in range(columns - 1, -1, -1):
                cell = dungeon[i][j]
                right_required_health = get_required_health(i, j + 1, cell)
                down_required_health = get_required_health(i + 1, j, cell)
                required_health = min(right_required_health, down_required_health)

                if required_health == float('inf'):
                    if cell >= 0:
                        required_health = 1
                    else:
                        required_health = 1 + abs(cell)
                dp[i][j] = required_health

        return dp[0][0]
