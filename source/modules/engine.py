import pygame
from .display import display
from .game import game
#from .ui.panel import Panel
from .events.io import io_events
from .events.actions import game_events
#from .ui.level1 import level1
#from .constants import 
#from .utils import utils

from OpenGL.GL import *
from OpenGL.GLU import *

#import gc


class GameEngine:
    """A Engine Pura: Controla o ciclo de vida, janelas, eventos e loops."""
    def __init__(self):
        # Pre-initialize mixer with a 512 or 1024 buffer to minimize CPU timing interruptions
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
        #pygame.init() # load all modules
        pygame.display.init()
        pygame.font.init()
        #pygame.joystick.init()
        pygame.mixer.init()
        #...

        display.create_display()
        #panel.create()
        game.init_assets()
        #menu.create()        
        #options.create()
        

    def run(self):
        # main menu - editor or game
         
        game.start()
        """O Game Loop Principal"""
        try:           
            while game.running:
                dt = display.game_tick()
                
                self.handle_events()
                self.update(dt)
                self.draw()
        except Exception as e:
            print(e)
            # log here
            game.stop()

    def handle_events(self):
        """Loop de Eventos: Inputs globais do sistema e interrupções"""
        io_events()
        game_events()


    def update(self, dt):
        """Loop de Atualização: Onde a lógica matemática acontece"""
        # new thread!        
        #game.all_sprites.update(dt)
        # check_collisions()
        game.player.update(dt)
        game.panel.update(dt)
            

    def draw(self):
        """Loop de Renderização: Onde desenhamos na tela""" 
                
        # Render Phase
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # ordem importa - cada layer por vez - pode organizar
        game.bg.draw()

        #for line in game.level1.tiles:
        #    for tile in line:
        #        if tile and tile.id != 0: tile.draw()                

        game.panel.draw()
        game.player.draw()

        # Desenha todas as entidades registradas no grupo de sprites
        # Render Phase - DirtyRect updating saves CPU/GPU time by partial clearing
        #rects = game.all_sprites.draw(display.off_screen)  
        #pygame.display.update(rects)

        # Converte e guarda o ID da GPU
        #texture_id = utils.surface_to_texture(display.off_screen)        
        #utils.draw_textured_quad(texture_id, 0,0,*display.size)

        #scaled_canvas = pygame.transform.scale(display.screen, display.size)
        #display.screen.blit(scaled_canvas, (0, 0))
        pygame.display.flip()
        # forçar sincronização de hardware CPU e GPU - chamadas assincronas
        #glFinish()
        


engine = GameEngine() # singleton 