import time

from tkinter import *
from tkinter import ttk

from utils import readJson


root = Tk()
root.geometry("500x500")
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

class Roommate():
    def __init__(self, name: str, column: int, row: int):
        self.name: str = name
        self.column: int = column
        self.row: int = row
        
        self.frame = ttk.Frame(root,
                               height=200,
                               width=200,
                               relief="groove",
                               borderwidth=5
                               )
        self.nameLabel = ttk.Label(self.frame,
                                   text=self.name,
                                   font=("Helvetica", 16),
                                   justify="center"
                                   )

        choreLabels: list = []
        for i in readJson(self.name)["Chores"]:
            choreLabels.append(ttk.Label(
                self.frame,
                text=i,
                font=("Helvetica"),
                justify="center"
                ))
        
        # Rendering all elements
        self.frame.grid(column=column, row=row, sticky="nsew")
        self.frame.grid_propagate(False)
        
        self.nameLabel.pack(anchor="n")
        
        for i in choreLabels:
            i.pack(anchor="n")

def screenUpdate():
    Ace = Roommate("Ace", 0, 0)
    Ben = Roommate("Ben", 0, 1)
    Cassandra = Roommate("Cassandra", 0, 2)
    Jamie = Roommate("Jamie", 1, 0)
    Jax = Roommate("Jax", 1, 2)
    Jay = Roommate("Jay", 2, 0)
    Melanie = Roommate("Melanie", 2, 1)
    Yenna = Roommate("Yenna", 2, 2)

    centerFrame = ttk.Frame(root,
                            height=200,
                            width=200,
                            relief="groove",
                            borderwidth=5
                            )
    centerLabel = ttk.Label(centerFrame,
                                text="Center",
                                font=("Helvetica", 16),
                                justify="center"
                                )

    centerFrame.grid(column=1, row=1, sticky="nsew")
    centerLabel.pack(anchor="n")

    root.update()