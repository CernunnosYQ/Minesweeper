import tkinter as tk
import tkinter.font as tkfont

from Board import Board

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(family="HeavyData NF", size=10)

        self.geometry("500x580")
        self.title("Minesweeper")
        self.resizable(False, False)

        self.marker = tk.Frame(self)
        self.marker.columnconfigure(0, weight=2)
        self.marker.columnconfigure(1, weight=1)
        self.marker.columnconfigure(2, weight=2)

        mines_label = tk.Label(self.marker, text="000")
        mines_label.configure(font=("HeavyData NF", 24))
        mines_label.grid(column=0, row=0, sticky="ew")

        config_btn = tk.Button(self.marker, text="")
        config_btn.configure(font=("HeavyData NF", 16))
        config_btn.grid(column=1, row=0, sticky="ew")

        timer_label = tk.Label(self.marker, text="000")
        timer_label.configure(font=("HeavyData NF", 24))
        timer_label.grid(column=2, row=0, sticky="ew")

        self.marker.pack(fill="both", pady=8)

        self.board = Board(self, 20, 20, 40)


if __name__ == "__main__":
    app = App()
    app.mainloop()
