import tkinter as tk

from Board import Board

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x520")
        self.title("Minesweeper")
        self.resizable(False, False)

        self.board = Board(self, 20, 20, 40)


if __name__ == "__main__":
    app = App()
    app.mainloop()
