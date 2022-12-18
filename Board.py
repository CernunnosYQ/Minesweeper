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
        self.createHints()

    def createMines(self):
        self.mines_coords = getMines(self.mines, self.x, self.y)
        print(self.mines_coords)

        for mine in self.mines_coords:
            self.board_logic[mine[0]][mine[1]] = 9

    def createHints(self):
        for mine in self.mines_coords:
            if mine[1] > 0:
                self.board_logic[mine[0]][mine[1] - 1] += 1
            if mine[1] < self.y-1:
                self.board_logic[mine[0]][mine[1] + 1] += 1

            if mine[0] > 0:
                self.board_logic[mine[0]-1][mine[1]] += 1
                if mine[1] > 0:
                    self.board_logic[mine[0]-1][mine[1] - 1] += 1
                if mine[1] < self.y-1:
                    self.board_logic[mine[0]-1][mine[1] + 1] += 1

            if mine[0] < self.x-1:
                self.board_logic[mine[0]+1][mine[1]] += 1
                if mine[1] > 0:
                    self.board_logic[mine[0]+1][mine[1] - 1] += 1
                if mine[1] < self.y-1:
                    self.board_logic[mine[0]+1][mine[1] + 1] += 1

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

def getMines(quantity, max_x, max_y):
    if quantity > max_x * max_y:
        return []
    
    max_index = max_x * max_y
    rng = np.random.default_rng()
    
    numbers = rng.integers(low=0, high=max_index, size=quantity*2)

    existent = set()
    uniques = [n for n in numbers if n not in existent or (existent.add(n) or False)]
    uniques = uniques[:quantity]

    return list(map(lambda c: [c % max_x, c // max_x], uniques))


if __name__ == "__main__":
    print("This is not a main module")
