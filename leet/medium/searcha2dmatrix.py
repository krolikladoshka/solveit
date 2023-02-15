# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        def n_to_ij(n):
            return n // cols, n % cols

        start = 0
        end = rows * cols - 1

        while start <= end:
            mid = (start + end) // 2
            i, j = n_to_ij(mid)
            if target < matrix[i][j]:
                end = mid - 1
            elif target > matrix[i][j]:
                start = mid + 1
            else:
                return True
        return False
