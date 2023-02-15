# https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s
from typing import List


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        columns = len(grid[0])
        if (rows + columns) % 2 == 0:
            return False

        dp_min = [[0] * columns for _ in range(rows)]
        dp_max = [[0] * columns for _ in range(rows)]
        dp_min[0][0] = dp_max[0][0] = grid[0][0]

        for i in range(1, rows):
            dp_min[i][0] = dp_max[i][0] = grid[i][0] + dp_min[i - 1][0]
        for i in range(1, columns):
            dp_min[0][i] = dp_max[0][i - 1] = grid[0][i] + dp_min[0][i - 1]

        for i in range(1, rows):
            for j in range(1, columns):
                dp_min[i][j] = grid[i][j] + min(dp_min[i - 1][j], dp_min[i][j - 1])
                dp_max[i][j] = grid[i][j] + max(dp_max[i - 1][j], dp_max[i][j - 1])

        return dp_min[-1][-1] <= ((rows + columns) // 2) <= dp_max[-1][-1]
