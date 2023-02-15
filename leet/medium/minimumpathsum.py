# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        dp = [[0] * columns for _ in range(rows)]

        dp[0][0] = grid[0][0]
        for i in range(1, columns):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, rows):
            for j in range(1, columns):
                current_value = grid[i][j]
                dp[i][j] = min(dp[i - 1][j] + current_value, dp[i][j - 1] + current_value)
        return dp[rows - 1][columns - 1]
