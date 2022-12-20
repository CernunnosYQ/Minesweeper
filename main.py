import tkinter as tk

from Board import Board

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x600")
        self.title("Minesweeper")
        self.resizable(False, False)

        self.marker = tk.Frame(self)
        self.marker.columnconfigure(0, weight=2)
        self.marker.columnconfigure(1, weight=1)
        self.marker.columnconfigure(2, weight=2)

        mines_label = tk.Label(self.marker, text="000")
        mines_label.grid(column=0, row=0, sticky="ew", padx=5, pady=5)

        config_btn = tk.Button(self.marker, text="#")
        config_btn.grid(column=1, row=0, sticky="ew", padx=5, pady=5)

        timer_label = tk.Label(self.marker, text="000")
        timer_label.grid(column=2, row=0, sticky="ew", padx=5, pady=5)

        self.marker.pack(fill="both")

        self.board = Board(self, 20, 20, 40)


if __name__ == "__main__":
    app = App()
    app.mainloop()
