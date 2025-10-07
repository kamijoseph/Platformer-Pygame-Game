
# platformer game
import pygame
import os
import random
import math
from os import listdir
from os.path import isfile, join

# initializing the pygame
pygame.init()

# caption
pygame.display.set_caption("Platformer Game")

# global var
BG_COLOR = (255, 255, 255)
FPS = 60
WIDTH, HEIGHT = 1000, 600
PLAYER_VEL = 5

# window
window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()
    quit()



























if __name__ == "__main__":
    main(window)