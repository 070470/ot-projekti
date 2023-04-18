from tkinter import *
import pygame

# Create game window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("YATZY!")
font = pygame.font.Font("Kanit-Regular.ttf", 20)
screen.fill((109, 164, 247))

# Create buttons for the main screen
startBtn = pygame.Rect(350, 250, 140, 55)

# Define game state
state = "menu"

pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if startBtn.collidepoint(event.pos):
                    state = "game"

    # Draw the menu screen
    if state == "menu":
        pygame.draw.rect(screen, (245, 211, 39), startBtn)
        btnText = font.render("Start a game", True, (31, 45, 94))
        screen.blit(btnText, (365, 263))

    pygame.display.flip()

pygame.quit()