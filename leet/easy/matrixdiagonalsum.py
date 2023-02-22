# https://leetcode.com/problems/matrix-diagonal-sum
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sm = 0
        for i in range(len(mat)):
            sm += mat[i][i] + mat[i][len(mat) - 1 - i]

        if len(mat) % 2 == 0:
            return sm
        return sm - mat[len(mat) // 2][len(mat) // 2]
