import pygame as pg
import os

class Utils():
    def __init__(self):        
        self.path = ''          
        
    def set_path(self, path:str):
        self.path = path

    def load_font(self, file, size):
        return pg.font.Font(os.path.join(self.path, file), size)
    
    def load_image(self, file):
        return pg.image.load(os.path.join(self.path, file)).convert_alpha()
    
    def create_sprite_update_list(self, 
                           screen:pg.Surface, 
                           back_surf:pg.Surface):
        self.sprites = pg.sprite.LayeredDirty() 
        self.sprites.set_timing_threshold(10000)
        self.sprites.clear(screen, back_surf)
      

utils = Utils()