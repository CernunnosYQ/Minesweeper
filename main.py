import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("960x540")
        self.title("Minesweeper")
        self.resizable(False, False)


class Board:
    def __init__(self, container, x, y):
        self.container = container
        self.x = x
        self.y = y

        self.createBoard(container)

    def createBoard(self, container):
        self.board = tk.Frame(container)

        self.board.pack(fill="both")

    def getBoard(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
