import pygame
from colorama import just_fix_windows_console
from pygame.time import Clock

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


def next_state_tile(board: Board):
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
            if cell_i < 0:
                cell_i = rows - 1
            elif cell_i >= rows:
                cell_i = 0
            if cell_j < 0:
                cell_j = columns - 1
            elif cell_j >= columns:
                cell_j = 0

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


class BoardRenderer:
    def __init__(self, board, tile_size=5):
        self.board = board
        self.tile_size = tile_size
    def render_board(self, screen: pygame.Surface):
        dy = 0
        for row in self.board:
            dx = 0
            for column in row:
                if column == 1:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(dx, dy, self.tile_size, self.tile_size))
                else:
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(dx, dy, self.tile_size, self.tile_size))
                dx += self.tile_size
            dy += self.tile_size
    def update(self):
        next_state_tile(self.board)

    def spawn(self, x, y):
        row = int(round(y / self.tile_size)) % len(self.board)
        column = int(round(x / self.tile_size) % len(self.board[0]))
        self.board[row][column] = 1

    def kill(self, x, y):
        row = int(round(y / self.tile_size)) % len(self.board)
        column = int(round(x / self.tile_size) % len(self.board[0]))
        self.board[row][column] = 0


def main_pygame(r=10, c=20):
    global rows
    global columns
    clock = Clock()
    pygame.init()
    screensize = (320, 320)
    screen: pygame.Surface = pygame.display.set_mode(screensize)
    tile_size = 1
    rows = round(screensize[1] / tile_size)
    columns = round(screensize[0] / tile_size)
    board = create_board()
    renderer = BoardRenderer(board)

    while True:
        renderer.render_board(screen)
        renderer.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sleep(5)
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sleep(5)
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 5:
                    renderer.spawn(*event.pos)
                elif event.button == 3:
                    renderer.kill(*event.pos)

        clock.tick(30)
