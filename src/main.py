from game import Game
from scoreboard import Scoreboard
from tkinter import *

# Create main GUI window
root = Tk()
root.title("Yatzy")
root.geometry("350x200")

btnStart = Button(root, text = "Start a new game",
             command = Game.beginGame)

btnSwitch = Button(root, text = "End turn", 
            command = Game.turnSwitch(Game.getPlayer))


root.mainloop()
