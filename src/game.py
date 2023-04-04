from scoreboard import Scoreboard
from tkinter import *
from dice import Dice

class Game:
    def __init__(self, player1, player2, currentPlayer):
        self.player1 = player1
        self.player2 = player2
        self.currentPlayer = currentPlayer
        

    def beginGame(self, player1, player2):
        pass

    def turn(player):
        counter = 1
        result = []
        continues = True
        keepsDice = False
        while counter <= 3 and Game.getPlayer == player:
            if counter == 1:
                result = Dice.throwAll()
                counter += 1
            if counter == 2:
                if keepsDice:
                    result = Dice.throwSome(result)
                    counter += 1
                else:
                    result = Dice.throwAll()
                    counter += 1

    def turnSwitch(self, player):
        if self.currentPlayer == self.player1:
            self.currentPlayer == self.player2
        else:
            self.currentPlayer == self.player1     

    def getPlayer(self):
        return self.currentPlayer


