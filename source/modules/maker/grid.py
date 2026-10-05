import pygame
from ..display import display
from ..constants import TILE_SIZE, COLOR_BG
from ..utils import utils
from ..ui.levels import Level1

class Grid():
    def __init__(self):  
        self.size = (display.size[0]*0.7, display.size[1]*0.8)
        self.image = pygame.Surface(self.size).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect_orig = self.image.get_rect()
        
        self.anchor = [0,0]
                
        self.x_tiles = int(self.size[0]//TILE_SIZE)
        self.y_tiles = int(self.size[1]//TILE_SIZE)
        
        self.clear()
        self.rect.topleft = (display.size[0]*0.1, display.size[1]*0.1)         
        
        # Converte e guarda o ID da GPU
        self.texture_id = utils.surface_to_texture(self.image)


    def clear(self):
        self.image.fill(COLOR_BG)
        for linha in range(self.y_tiles):
            pygame.draw.line(self.image, "white", (0,linha * TILE_SIZE), (self.size[0], linha * TILE_SIZE))
        for col in range(self.x_tiles):
            pygame.draw.line(self.image, "white", (col * TILE_SIZE, 0), (col * TILE_SIZE, self.size[1]))
        pygame.draw.rect(self.image, "green", self.rect_orig, 5)

     
    def update(self, dt):   
        self.clear()             
        for lin in range(self.y_tiles):                       
            for col in range(self.x_tiles):
                c = self.anchor[0] + col
                l = self.anchor[1] + lin                
                tile = self.level.tiles[l][c]
                if tile:                    
                    l = tile.rect.left - (self.anchor[0]*TILE_SIZE)
                    t = tile.rect.top - (self.anchor[1]*TILE_SIZE)
                    rect = (l, t, tile.rect.w, tile.rect.h)                    
                    self.image.blit(tile.image, rect)
        self.texture_id = utils.update_texture(self.texture_id, self.image)


    def load_level(self, level:Level1):
        self.level = level

    def draw(self):
        x,y,w,h = self.rect.x, self.rect.y, self.rect.w, self.rect.h        
        utils.draw_textured_quad(self.texture_id, x,y,w,h) 
       

