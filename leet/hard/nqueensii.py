# https://leetcode.com/problems/n-queens-ii/
from typing import List


class Solution:
    def solveNQueens2(self, n: int) -> List[List[str]]:
        def backtrack_queens(row, solutions, columns, diagonals, antidiagonals):
            if row == n:
                return solutions + 1

            def can_place(row, column) -> bool:
                if column in columns:
                    return False
                if (row - column) in diagonals:
                    return False
                if (row + column) in antidiagonals:
                    return False
                return True

            for column in range(n):
                if can_place(row, column):
                    columns.add(column)
                    diagonals.add(row - column)
                    antidiagonals.add(row + column)

                    solutions = backtrack_queens(row + 1, solutions, columns, diagonals, antidiagonals)

                    columns.remove(column)
                    diagonals.remove(row - column)
                    antidiagonals.remove(row + column)
            return solutions
        return backtrack_queens(0, 0, set(), set(), set())
