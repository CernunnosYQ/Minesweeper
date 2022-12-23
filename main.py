import tkinter as tk
import tkinter.font as tkfont

from Board import Board

class Scoreboard:
    def __init__(self, container, mines):
        self.container = container
        self.counter = mines
        self.time = 0

        self.scoreboard = tk.Frame(self.container)
        self.scoreboard.columnconfigure(0, weight=2)
        self.scoreboard.columnconfigure(1, weight=1)
        self.scoreboard.columnconfigure(2, weight=2)

        self.counter_label = tk.Label(self.scoreboard, font=("HeavyData NF", 24),
                                text=f"{self.counter:03d}")
        self.counter_label.grid(column=0, row=0, sticky="ew")

        self.btn = tk.Button(self.scoreboard, font=("HeavyData NF", 16), text="")
        self.btn.grid(column=1, row=0, sticky="ew")

        self.time_label = tk.Label(self.scoreboard, font=("HeavyData NF", 24),
                            text=f"{self.time:03d}")
        self.time_label.grid(column=2, row=0, sticky="ew")

        self.scoreboard.pack(fill="both", pady=8)

    def increaseTime(self):
        self.time_label["text"] = f"{self.time:03d}"
        self.time += 1
        self.time_label.after(1000, self.increaseTime)

    def increaseMineCounter(self):
        self.counter += 1
        self.counter_label["text"] = f"{self.counter:03d}"

    def decreaseMineCounter(self):
        self.counter -= 1
        self.counter_label["text"] = f"{self.counter:03d}"

    def callback(self, action):
        if action == "decrease":
            self.decreaseMineCounter()
        if action == "increase":
            self.increaseMineCounter()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(family="HeavyData NF", size=10)

        self.columns = 20
        self.rows = 20
        self.mines = 40

        self.geometry("500x580")
        self.title("Minesweeper")
        self.resizable(False, False)

        self.score = Scoreboard(self, self.mines)
        self.board = Board(self, self.columns, self.rows, self.mines, self.score.callback)

        self.score.increaseTime()


if __name__ == "__main__":
    app = App()
    app.mainloop()
