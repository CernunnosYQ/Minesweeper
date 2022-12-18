import tkinter as tk
import numpy as np

from Tile import Tile
from Utilities import *


class Board:
    def __init__(self, container, x, y, mines):
        self.container = container
        self.x = x
        self.y = y
        self.mines = mines

        self.createBoardLogic()
        self.createBoardTk()

    def createBoardLogic(self):
        self.board_logic = np.zeros((self.x, self.y))

        self.createMines()
        self.createHints()

    def createMines(self):
        self.mines_coords = getMines(self.mines, self.x, self.y)
        print(self.mines_coords)

        for mine in self.mines_coords:
            self.board_logic[mine[0]][mine[1]] = 9

    def createHints(self):
        for mine in self.mines_coords:
            neighbors = getNeighbors(mine, self.x, self.y)
            print(neighbors)
            for n in neighbors: 
                self.board_logic[n[0]][n[1]] += 1

    def createBoardTk(self):
        self.board = tk.Frame(self.container)
        self.buttons = []

        for i in range(self.x):
            self.board.columnconfigure(i, weight=1)

        for y in range(self.y):
            for x in range(self.x):
                self.buttons.append(
                    Tile(
                        self.board,
                        self.board_logic[x][y] if self.board_logic[x][y] < 9 else 9,
                        x, y, self.callback))

        self.board.pack(fill="both")

    def callback(self, x, y):
        for coord in self.mines_coords:
            c = np.array([x, y])
            if (c == coord).all():
                print("Boom!")

        if self.board_logic[x][y] == 0:
            self.board_logic[x][y] -= 1
            for n in getNeighbors([x, y], self.x, self.y):
                self.buttons[n[1] * self.x + n[0]].btn.invoke()


if __name__ == "__main__":
    print("This is not a main module")
