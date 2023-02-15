# https://leetcode.com/problems/sudoku-solver/
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        size = 9
        cell_size = 3
        rows = [
            set() for _ in range(size)
        ]
        cols = [
            set() for _ in range(size)
        ]

        def cell_by_ij(i, j):
            return (i // cell_size) * cell_size + j // cell_size

        cells = [set() for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if board[i][j] != '.':
                    value = int(board[i][j])
                    rows[i].add(value)
                    cols[j].add(value)
                    cells[cell_by_ij(i, j)].add(value)

        def can_place(value, i, j) -> bool:
            if value in rows[i]:
                return False
            if value in cols[j]:
                return False
            if value in cells[cell_by_ij(i, j)]:
                return False
            return True

        def solve(row, col):
            if row == size - 1 and col > size - 1:
                return True
            elif col > size - 1:
                row += 1
                col = 0
            if board[row][col] != '.':
                return solve(row, col + 1)
            for value in range(1, 10):
                if can_place(value, row, col):
                    board[row][col] = str(value)
                    rows[row].add(value)
                    cols[col].add(value)
                    cells[cell_by_ij(row, col)].add(value)

                    if solve(row, col + 1):
                        return True

                    board[row][col] = '.'
                    rows[row].remove(value)
                    cols[col].remove(value)
                    cells[cell_by_ij(row, col)].remove(value)
            return False
        solve(0, 0)
        return board
