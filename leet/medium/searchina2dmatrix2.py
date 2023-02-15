# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0, cols - 1

        i, j = start

        while i < rows and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True
        return False
