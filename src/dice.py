import pygame
from game import Game
from scoreboard import Scoreboard
import random as ran

class Dice(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        self.toss = toss

    def keepDice(self, toss):
        pass

    def throwAll():
        result = []
        counter = 0
        while counter < 6:
            result.append(ran.randint(1, 6))
            counter += 1
        return result
    
    def throwSome(keptDice):
        result = keptDice
        counter = 0
        while counter < (6 - len(keptDice)):
            result.append(ran.randint(1, 6))
            counter += 1

    
