
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

# get background function
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    
    return tiles, image

# draw function
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Green.png")

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        # background
        draw(window, background, bg_image)

    pygame.quit()
    quit()



























if __name__ == "__main__":
    main(window)