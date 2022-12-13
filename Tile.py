import tkinter as tk

class Tile:
    def __init__(self, container, value, x, y, action):
        self.container = container
        self.value = int(value)
        self.x, self.y = x, y
        self.action = action

        self.btn = tk.Button(container, text="  ", command=self.click)
        self.btn.grid(row=y, column=x, sticky="news")

    def click(self):
        self.btn["state"] = "disabled"
        self.btn["relief"] = "groove"
        self.btn["text"] = self.value
        self.action(self.x, self.y)
        
if __name__ == "__main__":
    print("This is not a main module")