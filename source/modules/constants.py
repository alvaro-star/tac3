import pygame
import math

# Set up window size and title
# nHD - 1/9 of full HD - 360p (height) - pixel art
#WIDTH, HEIGHT = 640, 360    # constant for PC - scales x2, x3, etc. 16x9 ratio
SCALE = 2
WIDTH, HEIGHT = 1920//SCALE, 1080//SCALE   # full HD - precisa usar dirty sprites - vetorial
#LV1_W = WIDTH * 10
#LV1_H = HEIGHT * 1
TITLE = "Game TAC3"
FPS = 0

COLOR_TEXT = pygame.Color("#087204")
COLOR_BG = pygame.Color("#5C94FC")

GRAVITY = 1200
SIZE_PLAYER = (20,40)

# Layer constants for performance rendering
LAYER_BACKGROUND = 0
LAYER_FOREGROUND = LAYER_BACKGROUND + 1
LAYER_CENARIO = LAYER_FOREGROUND + 1
LAYER_OBJECTS = LAYER_CENARIO + 1
LAYER_PLAYER = LAYER_OBJECTS + 1

TILE_CROP = 16  # pixels
TILE_SIZE = 16  # pixels
MAP_W = math.ceil(WIDTH / TILE_SIZE)
MAP_H = math.ceil(HEIGHT / TILE_SIZE)

FILE_LV1 = "source/data/lv1.npz"
FILE_LV1_JSON = 'source/data/level1.json'
FILE_MAP_1 = "assets/image/bg-1-1.png"
FILE_PLAYER_1 = "assets/image/player.png"

