# https://leetcode.com/problems/game-of-life/description/
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])

        adjacent_cells = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (-1, -1), (-1, 1),
            (1, -1), (1, 1),
        ]

        def count_alive(i, j):
            live = 0
            for direction in adjacent_cells:
                cell_i, cell_j = i + direction[0], j + direction[1]
                if cell_i < 0 or cell_i >= rows:
                    continue
                if cell_j < 0 or cell_j >= columns:
                    continue

                cell_value = board[cell_i][cell_j]
                if cell_value == 1 or cell_value == -1:
                    live += 1

            return live

        for i in range(rows):
            for j in range(columns):
                live = count_alive(i, j)
                if board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 2
                else:
                    if live < 2 or live > 3:
                        board[i][j] = -1

        for i in range(rows):
            for j in range(columns):
                if board[i][j] >= 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
