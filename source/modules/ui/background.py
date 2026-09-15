import pygame
from ..constants import WIDTH, HEIGHT, COLOR_BG
from ..utils import utils

class Background():
    def __init__(self):
        #super().__init__()
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(COLOR_BG) 
        
        self.rect = self.image.get_rect()

        # Converte e guarda o ID da GPU
        self.texture_id = utils.surface_to_texture(self.image)
        
        #self.dirty = 1 # Draw once initially
        #self._layer = LAYER_BACKGROUND

    def draw(self):
        x,y,w,h = self.rect.x, self.rect.y, self.rect.w, self.rect.h        
        utils.draw_textured_quad(self.texture_id, x,y,w,h)
        
#bg = Background()