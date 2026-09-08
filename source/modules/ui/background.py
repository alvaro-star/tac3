import pygame
from ..constants import WIDTH, HEIGHT, COLOR_BG, LAYER_BACKGROUND


class Background(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(COLOR_BG) 
        
        self.rect = self.image.get_rect()
        self.dirty = 1 # Draw once initially
        self._layer = LAYER_BACKGROUND

        
bg = Background()