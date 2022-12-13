import tkinter as tk
import numpy as np

from Tile import Tile


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

        print(self.mines_coords)

    def createMines(self):
        rng = np.random.default_rng()
        self.mines_coords = np.array([
            rng.integers(low=0, high=self.x, size=self.mines), 
            rng.integers(low=0, high=self.x, size=self.mines)
        ])

        self.mines_coords = self.mines_coords.T

        for mine in self.mines_coords:
            self.board_logic[mine[0]][mine[1]] = 9

    def createBoardTk(self):
        self.board = tk.Frame(self.container)
        self.buttons = []

        for i in range(self.x):
            self.board.columnconfigure(i, weight=1)

        for y in range(self.y):
            for x in range(self.x):
                self.buttons.append(Tile(self.board, self.board_logic[x][y],  x, y, self.callback))

        self.board.pack(fill="both")

    def callback(self, x, y):
        print(x, y)


if __name__ == "__main__":
    print("This is not a main module")
