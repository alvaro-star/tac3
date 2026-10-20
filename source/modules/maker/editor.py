import pygame
import sys, os
from ..display import display
from .info import Info
from .grid import Grid
from ..entities.tiles import TileMap, Tile
from OpenGL.GL import *
from ..ui.background import Background
from ..ui.levels import Level1
from ..constants import TILE_MAP_LEVEL1, TILE_SIZE
from .notify import Notify, Anchor, Select, Fill
from .pallet import Pallet
from .buttons import Button, UP, DOWN, LEFT, RIGHT

class Editor:
    def run(self):
            self.running = True 
            display.create_display()
            self.bg = Background("Black")

            # load tiles
            self.tile_map = TileMap()        
            self.tile_map.load_sprite_maps()
            self.level1 = Level1()
            if not self.level1.load(self.tile_map):
                self.level1.load(self.tile_map)
            
            self.grid = Grid(self.level1)
            self.info = Info(self.grid)
            self.pallet = Pallet(self.tile_map)

            #self.notify = Notify([self.grid, self.info])
            self.notify_anchor = Notify([self.grid, self.info], Anchor)
            self.notify_select = Notify([self.pallet], Select)
            self.notify_fill = Notify([self.grid], Fill)

            self.create_buttons()
            
            
            
            """O Game Loop Principal"""
            #try:           
            while self.running:
                dt = display.game_tick()   
                self.handle_events()
                self.update(dt)
                self.draw()
            '''except Exception as e:
                print(e)            # log here
                self.running = False
                pygame.quit()
                sys.exit()'''


    def create_buttons(self):
        size = int(display.size[1]*0.05)
        gap = size//5
        g = self.grid.rect

        # setas de navegacao - uma no meio de cada lado da grid
        positions = {
            UP:    (g.centerx - size//2, g.top - gap - size),
            DOWN:  (g.centerx - size//2, g.bottom + gap),
            LEFT:  (g.left - gap - size, g.centery - size//2),
            RIGHT: (g.right + gap, g.centery - size//2),
        }
        self.buttons:list[Button] = []
        for direction, (x, y) in positions.items():
            action = lambda d=direction: self.move_anchor(*d)
            self.buttons.append(Button((x, y, size, size), action, arrow=direction))

        # salvar - canto inferior direito, abaixo da paleta
        save_w = size*3
        top = int(display.size[1]*0.925)
        rect = (display.size[0] - gap*2 - save_w, top, save_w, size)
        self.button_save = Button(rect, self.save, label="SALVAR")
        self.buttons.append(self.button_save)
        self.save_counter = 0


    def move_anchor(self, dx, dy):
        max_x = TILE_MAP_LEVEL1[0] - self.grid.x_tiles
        max_y = TILE_MAP_LEVEL1[1] - self.grid.y_tiles
        x = min(max(self.grid.anchor[0] + dx, 0), max_x)
        y = min(max(self.grid.anchor[1] + dy, 0), max_y)
        if [x, y] != self.grid.anchor:
            self.grid.anchor[0], self.grid.anchor[1] = x, y
            self.notify_anchor.event()


    def save(self):
        self.level1.save()
        self.button_save.set_label("SALVO", "#1E7A1E")
        self.save_counter = 1.5


    def handle_events(self):
        """Loop de Eventos: Inputs globais do sistema e interrupções"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if (event.button == 1):    
                    if any(button.click(x,y) for button in self.buttons):
                        continue
                    if self.pallet.rect.collidepoint(x,y):
                        for tile in self.pallet.tiles:
                            l = self.pallet.rect.left + tile.rect.left
                            t = self.pallet.rect.top + tile.rect.top
                            r = pygame.rect.Rect(l,t, tile.rect.w, tile.rect.h)
                            if r.collidepoint(x,y):
                                self.pallet.select = tile
                                self.notify_select.event()
                                #print(tile.id)  
                                break
                    if self.grid.rect.collidepoint(x,y):
                        if self.pallet.select:
                            for tile in self.grid.tiles:
                                if tile.rect.collidepoint(x,y):
                                    col, lin = tile.desc.split(",")
                                    col = int(col)
                                    lin = int(lin)
                                    # posicao no mapa = posicao no grid + anchor
                                    col += self.grid.anchor[0]
                                    lin += self.grid.anchor[1]
                                    print(col, lin)
                                    # novo Tile por celula - senao todas compartilham o mesmo rect
                                    new_tile = Tile(*self.tile_map.codes[self.pallet.select.id])
                                    new_tile.rect.topleft = (col * TILE_SIZE, lin * TILE_SIZE)
                                    self.grid.level.tiles[lin][col] = new_tile
                                    self.notify_fill.event()

                                    break
                                
                if (event.button == 3):
                    if self.grid.rect.collidepoint(x,y):
                        for tile in self.grid.tiles:
                            if tile.rect.collidepoint(x,y):
                                col, lin = tile.desc.split(",")
                                col = int(col)
                                lin = int(lin)
                                # posicao no mapa = posicao no grid + anchor
                                col += self.grid.anchor[0]
                                lin += self.grid.anchor[1]
                                print(col, lin)
                                # novo Tile por celula - senao todas compartilham o mesmo rect
                                self.grid.level.tiles[lin][col] = None
                                self.notify_fill.event()

                                break

                        

        #game_events()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.move_anchor(*LEFT)
        if keys[pygame.K_RIGHT]: self.move_anchor(*RIGHT)
        if keys[pygame.K_UP]: self.move_anchor(*UP)
        if keys[pygame.K_DOWN]: self.move_anchor(*DOWN)
        

    def update(self, dt):
        """Loop de Atualização: Onde a lógica matemática acontece"""
        # new thread!                
        # check_collisions()
        #game.player.update(dt)
        self.info.update(dt, self.grid)
        self.grid.update(dt)
        self.pallet.update(dt)

        # volta o botao salvar ao normal
        if self.save_counter > 0:
            self.save_counter -= dt
            if self.save_counter <= 0:
                self.button_save.set_label("SALVAR", "#303030")

            
    def draw(self):
        """Loop de Renderização: Onde desenhamos na tela"""                 
        # Render Phase
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # ordem importa - cada layer por vez - pode organizar
        self.bg.draw()
        self.info.draw()
        self.grid.draw()
        self.pallet.draw()
        for button in self.buttons:
            button.draw()
        
        pygame.display.flip()
        # forçar sincronização de hardware CPU e GPU - chamadas assincronas
        #glFinish()


editor = Editor()