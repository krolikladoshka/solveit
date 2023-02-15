# https://leetcode.com/problems/set-matrix-zeroes
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        first_row = False
        first_column = False

        for i in range(rows):
            if matrix[i][0] == 0:
                first_column = True

            for j in range(columns):
                if matrix[0][j] == 0:
                    first_row = True

                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, rows):
            for j in range(1, columns):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for i in range(columns):
                matrix[0][i] = 0
        if first_column:
            for i in range(rows):
                matrix[i][0] = 0

    def setZeroes_dirty(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
        i = j = 0
        while i < rows:
            j = 0
            while j < columns:
                if matrix[i][j] is None:
                    for k in range(columns):
                        if matrix[i][k] is not None:
                            matrix[i][k] = 0
                    for k in range(rows):
                        if matrix[k][j] is not None:
                            matrix[k][j] = 0
                    matrix[i][j] = 0
                j += 1
            i += 1
