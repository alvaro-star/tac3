import pygame
from .display import display
from .game import game
from .ui.panel import panel
from .events.io import io_events
from .events.actions import game_events
from .ui.level1 import level1

class GameEngine:
    """A Engine Pura: Controla o ciclo de vida, janelas, eventos e loops."""
    def __init__(self):
        pygame.init() # load all modules
        #pygame.display.init()
        #pygame.font.init()
        #pygame.joystick.init()
        #pygame.mixer.init()
        #...

        display.create_display()
        game.init_assets()
        #menu.create()
        panel.create()
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
        game.all_sprites.update(dt)
        panel.update(dt)


    def draw(self):
        """Loop de Renderização: Onde desenhamos na tela"""        
        level1.scenario() # background, tiles
        panel.draw()
        
        # Desenha todas as entidades registradas no grupo de sprites
        game.all_sprites.draw(display.screen)        
        # Atualiza o buffer da tela para o monitor do jogador
        pygame.display.flip()


engine = GameEngine() # singleton 