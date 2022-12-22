import tkinter as tk

# Mine candidates: nf-fa-certificate, nf-fa-asterisk, nf-fa-bomb, nf-fa-ge, nf-fae-virus
# Flag candidates: nf-fa-bookmark, nf-fa-map_marker, nf-fa-map_pin, nf-mdi-alert_outline, nf-mdi-flag, nf-mdi-flag_variant
# Dubt candidates: nf-fa-question

COLORS = ["#2F2F2F", "#00BF96", "#4FBF2A", "#BFA300", "#BF7000", "#BF1C13"]
STATES = ["  ", "", "", "x"]
BACKGROUNDS = ["SystemButtonFace", "#BF7000", "#4FBF2A"]

class Tile:
    def __init__(self, container, value, x, y, callback):
        self.container = container
        self.state = 0
        self.value = int(value)
        self.x, self.y = x, y
        self.callback = callback

        self.btn = tk.Button(container, text="  ",
                             command=self.click, width=10)
        self.btn.bind("<Button-3>", self.rClick)
        self.btn.grid(row=y, column=x, sticky="news")

    def click(self):
        if self.state == 0:
            self.state = 3

            self.btn["state"] = "disabled"
            self.btn["relief"] = "groove"
            self.btn["text"] = self.value

            if self.value > 4:
                self.btn.configure(disabledforeground=COLORS[5])
            else:
                self.btn.configure(disabledforeground=COLORS[self.value])

            if self.value == 9:
                self.btn["text"] = " "
                self.callback('boom', self.x, self.y)

            if self.value == 0:
                self.btn["text"] = "  "
                self.callback('wave', self.x, self.y)

    def rClick(self, event):
        if self.state == 3:
            self.callback('wave', self.x, self.y)
        else:
            self.state = (self.state+1) % 3
            self.btn["text"] = STATES[self.state]
            self.btn["background"] = BACKGROUNDS[self.state]
            if self.state == 1: self.btn["foreground"] = "white"
        
if __name__ == "__main__":
    print("This is not a main module")