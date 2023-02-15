from colorama import just_fix_windows_console

just_fix_windows_console()

import os
import random
import re
import sys
from os.path import split
from time import sleep
from typing import List


rows = 10
columns = 20

Board = List[list[int]]


def next_state(board: Board):
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


def create_board() -> Board:
    board = []
    for i in range(rows):
        board.append([])
        for j in range(columns):
            board[i].append(random.choice([0, 1]))

    return board


def enrich_board(board: Board):
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 0:
                board[i][j] = random.choice([0, 1])


def convert_board(board: Board) -> str:
    lines = []
    for i in range(rows):
        line = []
        for j in range(columns):
            line.append(' ' if board[i][j] == 0 else 'X')
        lines.append(''.join(line))
    return '\n'.join(lines)


class Reprinter:
    def __init__(self):
        self.text = ''

    def moveup(self, lines):
        for _ in range(lines):
            sys.stdout.write("\033[F")
            # sys.stdout.write('\r')

    def reprint(self, text):
        self.moveup(self.text.count("\n"))
        sys.stdout.write(re.sub(r"[^\s]", " ", self.text))

        lines = min(self.text.count("\n"), text.count("\n"))
        self.moveup(lines)
        sys.stdout.write(text)
        self.text = text


def restart(delay=0.5):
    reprinter = Reprinter()
    global rows
    global columns
    board = []
    with open(os.path.join(split(__file__)[0], 'board.txt'), 'r') as fin:
        for i, line in enumerate(fin.readlines()):
            line = line.strip('\n')
            board.append([
                0 if ch == ' ' else 1
                for ch in line
            ])
    rows = len(board)
    columns = len(board[0])

    try:
        reprinter.reprint(convert_board(board))
        sleep(2)
        enrich_board(board)
        reprinter.reprint(convert_board(board))
        sleep(2)

        while True:
            sleep(delay)
            next_state(board)
            reprinter.reprint(convert_board(board))
    except KeyboardInterrupt:
        with open(os.path.join(split(__file__)[0], 'board.txt'), 'w+') as fout:
            fout.write(convert_board(board))


def start(delay=0.5, r=10, c=20):
    reprinter = Reprinter()
    global rows
    global columns
    rows = r
    columns = c
    board = create_board()

    try:
        while True:
            reprinter.reprint(convert_board(board))
            sleep(delay)
            next_state(board)

    except KeyboardInterrupt:
        with open(os.path.join(split(__file__)[0], 'board.txt'), 'w+') as fout:
            fout.write(convert_board(board))
