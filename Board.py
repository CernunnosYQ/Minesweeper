import tkinter as tk
import numpy as np

from Tile import Tile
from Utilities import *


class Board:
    def __init__(self, container, x, y, mines, scoreCallback):
        self.container = container
        self.max_x = x
        self.max_y = y
        self.mines = mines
        self.scoreCallback = scoreCallback

        self.createBoardLogic()
        self.createBoardTk()

    def createBoardLogic(self):
        self.board_logic = np.zeros((self.max_x, self.max_y))

        self.createMines()
        self.createHints()

    def createMines(self):
        self.mines_coords = getRandom(self.mines, self.max_x, self.max_y)

        for mine in self.mines_coords:
            self.board_logic[mine[0]][mine[1]] = 9

    def createHints(self):
        for mine in self.mines_coords:
            neighbors = getNeighbors(mine, self.max_x, self.max_y)
            for n in neighbors: 
                self.board_logic[n[0]][n[1]] += 1

    def createBoardTk(self):
        self.board = tk.Frame(self.container)
        self.buttons = []

        for i in range(self.max_x):
            self.board.columnconfigure(i, weight=1)

        for y in range(self.max_y):
            for x in range(self.max_x):
                self.buttons.append(
                    Tile(
                        self.board,
                        self.board_logic[x][y] if self.board_logic[x][y] < 9 else 9,
                        x, y, self.callback))

        self.board.pack(fill="both")

    def callback(self, action, x, y):
        if action == 'wave':
            for n in getNeighbors([x, y], self.max_x, self.max_y):
                self.buttons[n[1] * self.max_x + n[0]].btn.invoke()
        if action == 'boom':
            for m in self.mines_coords:
                self.buttons[m[1] * self.max_x + m[0]].btn.invoke()
        if action == 'flag':
            self.scoreCallback("decrease")


if __name__ == "__main__":
    print("This is not a main module")
