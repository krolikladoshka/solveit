# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        width = len(grid)
        height = len(grid[0])

        for i in range(width):
            for j in range(height):
                if grid[i][j] == '1':
                    self.erase_island(grid, i, j, width, height)
                    counter += 1

        return counter

    def erase_island(self, grid: List[List[str]], row: int, col: int, width: int, height: int):
        if col >= height or col < 0:
            return
        if row >= width or row < 0:
            return
        if grid[row][col] == '0':
            return
        grid[row][col] = '0'
        self.erase_island(grid, row - 1, col, width, height)
        self.erase_island(grid, row + 1, col, width, height)
        self.erase_island(grid, row, col - 1, width, height)
        self.erase_island(grid, row, col + 1, width, height)
