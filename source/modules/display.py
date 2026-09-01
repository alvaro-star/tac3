import pygame
from .constants import WIDTH, HEIGHT, TITLE, FPS

class Display():
    def __init__(self):
        pass

    def create_display(self):        
        self.clock = pygame.time.Clock()  
        self.size = (WIDTH, HEIGHT)
        #self.info = pygame.display.Info()
        #self.size = (self.info.current_w, self.info.current_h)
       
        pygame.display.set_caption(TITLE)         
        #flags = 0       
        flags = pygame.SCALED | pygame.FULLSCREEN         
        self.screen = pygame.display.set_mode(self.size, flags, display=0, vsync=1)
                    
        
    def reload(self):
        pass

    def game_tick(self):
        # Captura o tempo decorrido desde o último quadro em segundos (Delta Time)
        # Limita o FPS máximo para não estressar o processador desnecessariamente
        delta_time = self.clock.tick_busy_loop(FPS) / 1000.0 
        return delta_time


display = Display()