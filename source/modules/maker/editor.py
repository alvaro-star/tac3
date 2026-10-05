import pygame
import sys, os
from ..display import display
from .info import Info
from .grid import Grid
from ..entities.tiles import TileMap
from OpenGL.GL import *
from ..ui.background import Background
from ..ui.levels import Level1
from ..constants import TILE_MAP_LEVEL1


class Editor:
    def run(self):
            self.running = True 
            display.create_display()
            self.bg = Background("Black")
            
            self.grid = Grid()
            self.info = Info(self.grid)
            # load tiles
            self.tile_map = TileMap()        
            self.tile_map.load_sprite_maps()
            self.level1 = Level1()
            if not self.level1.load(self.tile_map):
                self.level1.load(self.tile_map)

            self.grid.load_level(self.level1)
    
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.grid.anchor[0] > 0:
                self.grid.anchor[0] -= 1
        if keys[pygame.K_RIGHT]:
            max = TILE_MAP_LEVEL1[0] - self.grid.x_tiles
            if self.grid.anchor[0] < max:
                self.grid.anchor[0] += 1
        if keys[pygame.K_UP]:
            if self.grid.anchor[1] > 0:
                self.grid.anchor[1] -= 1
        if keys[pygame.K_DOWN]:
            max = TILE_MAP_LEVEL1[1] - self.grid.y_tiles
            if self.grid.anchor[1] < max:
                self.grid.anchor[1] += 1
        pass

    def update(self, dt):
        """Loop de Atualização: Onde a lógica matemática acontece"""
        # new thread!                
        # check_collisions()
        #game.player.update(dt)
        self.info.update(dt, self.grid)
        self.grid.update(dt)
            
    def draw(self):
        """Loop de Renderização: Onde desenhamos na tela"""                 
        # Render Phase
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # ordem importa - cada layer por vez - pode organizar
        self.bg.draw()
        self.info.draw()
        self.grid.draw()
        
        pygame.display.flip()
        # forçar sincronização de hardware CPU e GPU - chamadas assincronas
        #glFinish()


editor = Editor()