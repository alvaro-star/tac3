import pygame
from ..utils import utils
from ..constants import LAYER_OBJECTS, TILE_SIZE, TILE_CROP, FILE_MAP_1


class Floor(pygame.sprite.DirtySprite):
    def __init__(self, w=TILE_SIZE, h=TILE_SIZE, type=1):
        super().__init__()
        if type == 1 : self.image = tiles.floor1
        elif type == 2 : self.image = tiles.floor2
        else: raise "Invalid type of Floor"
        
        if w != TILE_CROP or h != TILE_CROP:
            self.image = pygame.transform.smoothscale(self.image, (w,h))
        self.rect = self.image.get_rect()

        self.dirty = 1 # Draw once initially
        self._layer = LAYER_OBJECTS


class Brick(pygame.sprite.DirtySprite):
    def __init__(self, w=TILE_SIZE, h=TILE_SIZE, type=1):
        super().__init__()
        if type == 1 : self.image = tiles.brick1
        elif type == 2 : self.image = tiles.brick2
        else: raise "Invalid type of Brick"
        
        if w != TILE_CROP or h != TILE_CROP:
            self.image = pygame.transform.smoothscale(self.image, (w,h))
        self.rect = self.image.get_rect()

        self.dirty = 1 # Draw once initially
        self._layer = LAYER_OBJECTS


class Tiles():
    def load_sprite_maps(self):
        self.map_items = utils.load_image(FILE_MAP_1)

        # items
        self.floor1 = self.map_items.subsurface((0,208,TILE_CROP,TILE_CROP))
        self.floor2 = self.map_items.subsurface((768,448,TILE_CROP,TILE_CROP))
        self.brick1 = self.map_items.subsurface((320,144,TILE_CROP,TILE_CROP))
        self.brick2 = self.map_items.subsurface((832,400,TILE_CROP,TILE_CROP))

        #pygame.image.save(self.floor1,"1.png")
        #pygame.image.save(self.floor2,"2.png")
        #pygame.image.save(self.brick1,"3.png")
        #pygame.image.save(self.brick2,"4.png")

        # object codes
        self.codes = [
            (None, None),   # code by index - 0 draw nothing
            (Floor, 1),     # Class, type
            (Floor, 2),     # code 2
            (Brick, 1),     # code 3
            (Brick, 2),     # code 4
        ]

tiles = Tiles()