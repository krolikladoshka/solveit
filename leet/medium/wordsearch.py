# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def walk_word(start_i, start_j, pos):
            if start_i >= rows or start_i < 0:
                return False
            if start_j < 0 or start_j >= cols:
                return False
            if pos == len(word):
                return True
            if board[start_i][start_j] != word[pos]:
                return False

            directions = [
                (-1, 0), (1, 0), (0, -1), (0, 1),
            ]
            found = True
            board[start_i][start_j] = '.'
            for direction in directions:
                found = walk_word(
                    start_i + direction[0], start_j + direction[1],
                    pos + 1,
                )
                if found:
                    break
            board[start_i][start_j] = word[pos]

            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if len(word) == 1 or walk_word(i, j, 0):
                        return True
        return False
