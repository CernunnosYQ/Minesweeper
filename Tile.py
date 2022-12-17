import tkinter as tk

class Tile:
    def __init__(self, container, value, x, y, action):
        self.colors = ["#2F2F2F", "#00BF96", "#4FBF2A", "#BFA300", "#BF7000", "#BF1C13"]
        self.container = container
        self.value = int(value)
        self.x, self.y = x, y
        self.action = action
        self.state = 0
        self.states = ['  ', '!', '?']
        self.bg_colors = ['SystemButtonFace', '#BFA300', '#4FBF2A']

        self.btn = tk.Button(container, text="  ", command=self.click)
        self.btn.bind("<Button-3>", self.rClick)
        self.btn.grid(row=y, column=x, sticky="news")

    def click(self):
        if self.state == 0:
            self.btn["state"] = "disabled"
            self.btn["relief"] = "groove"
            self.btn["text"] = self.value

            if self.value > 4:
                self.btn.configure(disabledforeground=self.colors[5])
            else:
                self.btn.configure(disabledforeground=self.colors[self.value])

            self.action(self.x, self.y)

    def rClick(self, event):
        self.state = (self.state+1) % 3
        self.btn["text"] = self.states[self.state]
        self.btn["background"] = self.bg_colors[self.state]
        
if __name__ == "__main__":
    print("This is not a main module")