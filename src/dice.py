import pygame
from game import Game
from scoreboard import Scoreboard
import random as ran
import images

class Dice(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, targeted=False):
        super().__init__()

        self.targeted = targeted

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
        return result
    
    def diceIntoSprites(dice):
        sprites = []
        for i in (len(dice)-1):
            if i == 1:
                sprites.append(pygame.image.load(images/"dice1.png"))
                i += 1
            if i == 2:
                sprites.append(pygame.image.load(images/"dice2.png"))
                i += 1
            if i == 3:
                sprites.append(pygame.image.load(images/"dice3.png"))
                i += 1
            if i == 4:
                sprites.append(pygame.image.load(images/"dice4.png"))
                i += 1
            if i == 5:
                sprites.append(pygame.image.load(images/"dice5.png"))
                i += 1
            if i == 6:
                sprites.append(pygame.image.load(images/"dice6.png"))
                i += 1
