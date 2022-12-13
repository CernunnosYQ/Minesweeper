import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("960x540")
        self.title("Minesweeper")
        self.resizable(False, False)

        self.board = Board(self, 20, 20)


class Board:
    def __init__(self, container, x, y):
        self.container = container
        self.x = x
        self.y = y

        self.createBoard()

    def createBoard(self):
        self.board = tk.Frame(self.container)
        self.buttons = []

        for i in range(self.x):
            self.board.columnconfigure(i, weight=1)

        for y in range(self.y):
            for x in range(self.x):
                self.buttons.append(Tile(self.board, x, y, self.callback))

        self.board.pack(fill="both")

    def callback(self, x, y):
        print(x, y)


class Tile:
    def __init__(self, container, x, y, action):
        self.container = container
        self.x, self.y = x, y
        self.action = action

        self.btn = tk.Button(container, command=self.callback)
        self.btn.grid(row=y, column=x, sticky="news")

    def callback(self):
        self.btn["state"] = "disabled"
        self.btn["relief"] = "groove"
        self.action(self.x, self.y)


if __name__ == "__main__":
    app = App()
    app.mainloop()
