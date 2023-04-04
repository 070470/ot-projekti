from player import Player
from scoreboard import Scoreboard
from tkinter import *

# Create main GUI window
root = Tk()
root.title("Yatzy")
root.geometry("350x200")

btn = Button(root, text = "Start a new game")

root.mainloop()

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def begin