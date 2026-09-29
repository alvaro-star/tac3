import pygame
from ..display import display
from ..constants import TILE_SIZE, COLOR_BG
from ..utils import utils

class Grid():
    def __init__(self):  
        self.size = (display.size[0]*0.7, display.size[1]*0.8)
        self.image = pygame.Surface(self.size).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(COLOR_BG)
        pygame.draw.rect(self.image, "green", self.rect, 5)
        
        x_tiles = int(self.size[0]//TILE_SIZE)
        y_tiles = int(self.size[1]//TILE_SIZE)
        tile_rect = pygame.rect.Rect(0,0,TILE_SIZE,TILE_SIZE)
        for linha in range(y_tiles):
            for col in range(x_tiles):
                tile_rect.topleft = (col * TILE_SIZE, linha * TILE_SIZE)
                pygame.draw.rect(self.image, "green", tile_rect, 1)

        self.rect.topleft = (display.size[0]*0.1, display.size[1]*0.1)         
        
        # Converte e guarda o ID da GPU
        self.texture_id = utils.surface_to_texture(self.image)
        
     
    def update(self, dt):        
        pass
           

    def draw(self):
        x,y,w,h = self.rect.x, self.rect.y, self.rect.w, self.rect.h        
        utils.draw_textured_quad(self.texture_id, x,y,w,h) 
       

