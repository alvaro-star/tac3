import pygame
import sys
import gc
from .entities.player import Player


class Game():
    def __init__(self):
        self.running = False

    def init_assets(self):
        # Inicialização de entidades usando os Grupos do Pygame (Otimização nativa)
        self.player = Player(100, 100)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)


    def start(self):
        self.running = True   

    def stop(self):
        self.running = False
        gc.enable()
        pygame.quit()
        sys.exit()



game = Game() 