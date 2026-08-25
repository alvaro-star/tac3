import pygame
from ..display import display
#from ..core.game import game
from ..constants import WIDTH, HEIGHT, BG_COLOR

class Level1():

    def scenario(self):
        display.screen.fill(BG_COLOR)  # Limpa a tela com a cor de fundo
                
        # Desenha uma linha simulando o chão da fase
        pygame.draw.line(display.screen, (100, 100, 100), (0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 4)

level1 = Level1()
