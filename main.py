
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

# fliiping character helper function
def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

# loading sprite sheets
def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}
    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))
        
        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites
    
    return all_sprites

# player class
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets(
        "MainCharacters",
        "NinjaFrog",
        32, 32,
        True
    )
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
    
    # players movement
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    # move left
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    # move right
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    
    def loop(self, fps):
        # self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)
        self.fall_count += 1
        self.update_sprite()

    def update_sprite(self):
        sprite_sheet = "idle"

        if self.x_vel != 0:
            sprite_sheet = "run"
        
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
    
    def draw(self, win):
        win.blit(self.sprite, (self.rect.x, self.rect.y))

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
def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)
    
    # drawing the player
    player.draw(window)

    pygame.display.update()

# handle movements function
def handle_movement(player):
    player.x_vel = 0
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)


def main(window):
    # clock
    clock = pygame.time.Clock()

    # background
    background, bg_image = get_background("Green.png")

    # player
    player = Player(100, 100, 50, 50)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        # players movement
        player.loop(FPS)
        handle_movement(player)

        # draw stuff
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()



























if __name__ == "__main__":
    main(window)