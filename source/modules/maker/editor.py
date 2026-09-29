import pygame
import sys, os
from ..display import display
from .panel import Panel
from .grid import Grid
from ..entities.tiles import TileMap2
from OpenGL.GL import *
from ..ui.background import Background
from ..ui.level1 import Level1


class Editor:
    def run(self):
            self.running = True 
            display.create_display()
            self.bg = Background("Black")
            self.panel = Panel()
            self.grid = Grid()
            # load tiles
            self.tile_map = TileMap2()        
            self.tile_map.load_sprite_maps()
            self.level1 = Level1()
            if not self.level1.load(self.tile_map):
                self.level1.load(self.tile_map)
    
            #self.bg.add_cenario(self.level1.tiles)
            
            """O Game Loop Principal"""
            try:           
                while self.running:
                    dt = display.game_tick()   
                    self.handle_events()
                    self.update(dt)
                    self.draw()
            except Exception as e:
                print(e)            # log here
                self.running = False
                pygame.quit()
                sys.exit()


    def handle_events(self):
        """Loop de Eventos: Inputs globais do sistema e interrupções"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
        #game_events()
        pass

    def update(self, dt):
        """Loop de Atualização: Onde a lógica matemática acontece"""
        # new thread!                
        # check_collisions()
        #game.player.update(dt)
        self.panel.update(dt)
            
    def draw(self):
        """Loop de Renderização: Onde desenhamos na tela"""                 
        # Render Phase
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # ordem importa - cada layer por vez - pode organizar
        self.bg.draw()
        self.panel.draw()
        self.grid.draw()
        
        pygame.display.flip()
        # forçar sincronização de hardware CPU e GPU - chamadas assincronas
        #glFinish()


editor = Editor()