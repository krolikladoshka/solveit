# https://leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
                    if value in rows[i]:
                        return False
                    rows[i].add(value)
                    if value in cols[j]:
                        return False
                    cols[j].add(value)

                    cell_idx = cell_by_ij(i, j)
                    if value in cells[cell_idx]:
                        return False
                    cells[cell_idx].add(value)
        return True
