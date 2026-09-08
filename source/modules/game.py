import pygame
import sys
import gc
from .entities.player import Player
from .ui.background import bg
from .display import display
from .entities.tiles import tiles
from .ui.level1 import level1


class Game():
    def __init__(self):
        self.running = False

    def init_assets(self):       
        # Create Group Managed via LayeredDirty for automated optimization
        self.all_sprites = pygame.sprite.LayeredDirty()
        self.all_sprites.set_timing_threshold(10000)
        self.all_sprites.clear(display.screen, bg.image)
        platforms = pygame.sprite.Group()

        self.player = Player(100, 100)
        self.all_sprites.add(self.player)

        # load assets
        tiles.load_sprite_maps()
        if not level1.load():
            level1.load()

        for line in level1.tiles:
            for obj in line:
                if obj: self.all_sprites.add(obj)
                
       

    def start(self):
        self.running = True   


    def stop(self):
        self.running = False
        gc.enable()
        pygame.quit()
        sys.exit()



game = Game() 