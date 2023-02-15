# https://leetcode.com/problems/n-queens/
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        qboard = [['.'] * n for _ in range(n)]

        def get_solution(board):
            solution = []
            for row in board:
                solution.append(''.join(row))
            return solution

        def backtrack_queens(row, columns, diagonals, antidiagonals, board):
            if row == n:
                yield get_solution(board)
                return

            def can_place(row, column) -> bool:
                if column in columns:
                    return False
                if (row - column) in diagonals:
                    return False
                if (row + column) in antidiagonals:
                    return False
                return True

            for column in range(n):
                if not can_place(row, column):
                    continue
                board[row][column] = 'Q'
                columns.add(column)
                diagonals.add(row - column)
                antidiagonals.add(row + column)

                yield from backtrack_queens(row + 1, columns, diagonals, antidiagonals, board)

                columns.remove(column)
                diagonals.remove(row - column)
                antidiagonals.remove(row + column)
                board[row][column] = '.'

        return list(backtrack_queens(0, set(), set(), set(), qboard))




    def solveNQueens1(self, n):
        # Making use of a helper function to get the
        # solutions in the correct output format
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            ans.append(board)
            return board

        def backtrack(row, diagonals, anti_diagonals, cols, state):
            # Base case - N queens have been placed
            if row == n:
                yield create_board(state)
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if (col in cols
                        or curr_diagonal in diagonals
                        or curr_anti_diagonal in anti_diagonals):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"

                # Move on to the next row with the updated board state
                yield from backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."

        ans = []
        empty_board =[['.'] * n for _ in range(n)]
        t = list(backtrack(0, set(), set(), set(), empty_board))
        return t
        return ans
