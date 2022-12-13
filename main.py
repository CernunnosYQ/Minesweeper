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
                btn = tk.Button(self.board)
                btn.grid(row=y, column=x, sticky="ew")

                self.buttons.append(btn)

        self.board.pack(fill="both")

    def callback(self, x, y):
        print(x, y)

    def getButton(self, x, y):
        pass

    def getBoard(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
