import pygame
import sys
#import gc
from .entities.player import Player
from .ui.background import Background
from .display import display
from .entities.tiles import TileMap
from .ui.level1 import Level1
from .ui.panel import Panel


class Game():
    def __init__(self):
        self.running = False

    def init_assets(self):       
        # Create Group Managed via LayeredDirty for automated optimization
        #self.all_sprites = pygame.sprite.LayeredDirty()
        #self.all_sprites.set_timing_threshold(10000)
        #self.all_sprites.clear(display.off_screen, bg.image)
        #platforms = pygame.sprite.Group()

        self.bg = Background()
        self.player = Player()
        self.panel = Panel()
        '''self.all_sprites.add(self.player)
        panel.create()
        self.all_sprites.add(panel)'''

        # load tiles
        self.tile_map = TileMap()        
        self.tile_map.load_sprite_maps()
        self.level1 = Level1()
        if not self.level1.load(self.tile_map):
            self.level1.load(self.tile_map)

        '''for line in level1.tiles:
            for obj in line:
                if obj: self.all_sprites.add(obj)'''
                
       

    def start(self):
        self.running = True   


    def stop(self):
        self.running = False
        #gc.enable()
        pygame.quit()
        sys.exit()



game = Game() 