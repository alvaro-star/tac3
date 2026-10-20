import pygame

TITLE = "Game TAC3"
FPS = 60
SCALE = 2
GRAVITY = 1200

COLOR_TEXT = pygame.Color("#087204")
COLOR_BG = pygame.Color("#5C94FC")
COLOR_SCROLL = pygame.Color("#0E6303")

SIZE_PLAYER = (60*SCALE, 100*SCALE)
SIZE_ICON = (40,40)
SIZE_SCROLL = 30

TILE_CROP = 16  # pixels
TILE_SIZE = 32*SCALE  # pixels
TILE_MAP_LEVEL1 = (300,50)
TILE_MAP_LEVEL2 = (200,700)
TILE_MAP_PALLET = 50

FILE_LV1 = "source/data/lv1.npz"
FILE_LV1_JSON = 'source/data/level1.json'
FILE_MAP_1 = "assets/image/bg-1-1.png"
FILE_MAP_2 = "assets/image/bg-1-1-cutout.png"
FILE_PLAYER_1 = "assets/image/player.png"
FILE_SPRITES_PLAYER = "assets/image/sprites3.png"

ICON_LOAD = "assets/image/load.png"
ICON_SAVE = "assets/image/save.png"
ICON_ARROW_BLACK = "assets/image/seta1.png"
ICON_ARROW_GRAY = "assets/image/seta2.png"
ICON_ARROW_GREEN = "assets/image/seta3.png"


EVENT_ANCHOR_VERTICAL:int = 0
EVENT_ANCHOR_HORIZONTAL:int = 1

EVENT_GRID_FILL:int = 100

EVENT_PALLET_SELECT:int = 200

EVENT_BUTTON_SAVE:int = 300
EVENT_BUTTON_MESSAGE:int = 301
EVENT_BUTTON_OVER:int = 302
#EVENT_BUTTON_CLICKED:int = 303


