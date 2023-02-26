# https://leetcode.com/problems/minesweeper
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        digits = 'B12345678'
        adjacents = [
            (0, -1), (0, 1), (-1, 0), (1, 0),
            (-1, -1), (-1, 1), (1, -1), (1, 1),
        ]

        def get_cell(row, column):
            if row >= m or column >= n or row < 0 or column < 0:
                return
            return board[row][column]

        def count_mines(row, column):
            counter = 0
            for adjacent in adjacents:
                cell = get_cell(row + adjacent[0], column + adjacent[1])
                if cell is not None:
                    if cell == 'M':
                        counter += 1
            return counter

        def reveal(row, column):
            cell = get_cell(row, column)
            if cell is None:
                return
            if cell in digits:
                return
            if cell == 'M':
                return

            board[row][column] = digits[count_mines(row, column)]
            if board[row][column] != 'B':
                return

            for direction in adjacents:
                reveal(row + direction[0], column + direction[1])

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'

            return board

        reveal(click[0], click[1])

        return board
