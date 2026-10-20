import pygame
from ..display import display
from ..constants import TILE_SIZE
from ..utils import utils
from ..entities.tiles import TileMap, Tile
from .notify import Interested, Select, Anchor

class Pallet(Interested):
    def __init__(self, tilemap:TileMap): 
        super().__init__() 
        self.size = (display.size[0]*0.1, display.size[1]*0.5)
        self.image = pygame.Surface(self.size).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect_orig = self.image.get_rect()
        
        self.anchor = [0,0]
        self.tilemap = tilemap
        self.tiles:list[Tile] = []
        self.select:Tile = None
                
        self.x_tiles = int(self.size[0]//TILE_SIZE)
        self.y_tiles = int(self.size[1]//TILE_SIZE)

        # Converte e guarda o ID da GPU
        self.texture_id = utils.surface_to_texture(self.image)

        self.clear()
        self.update_tiles()
        self.rect.topleft = (display.size[0]*0.9, display.size[1]*0.3)

        # painel de informacoes da paleta - canto superior direito da tela
        pygame.font.init()
        self.font_desc = pygame.font.Font("assets/fonts/FreeSans.ttf", int(display.size[1]*0.022))
        desc_w, desc_h = int(display.size[0]*0.17), int(display.size[1]*0.25)
        self.desc_image = pygame.Surface((desc_w, desc_h)).convert_alpha()
        self.desc_rect = self.desc_image.get_rect()
        margin = int(display.size[1]*0.02)
        self.desc_rect.topright = (display.size[0] - margin, margin)
        self.desc_texture_id = utils.surface_to_texture(self.desc_image)
        self.showPanelDesc()


    def showPanelDesc(self):
        # redesenha o painel com o total de tiles e o tile selecionado
        w, h = self.desc_rect.size
        pad = int(h*0.06)
        self.desc_image.fill((20, 20, 20, 230))
        pygame.draw.rect(self.desc_image, "blue", (0, 0, w, h), 3)

        lines = ["PALETA", f"Tiles: {len(self.tilemap.codes) - 1}"]
        if self.select:
            lines += [f"Selecionado: {self.select.desc}", f"ID: {self.select.id}"]
        else:
            lines.append("Selecionado: nenhum")

        y = pad
        for i, text in enumerate(lines):
            color = "gold" if i == 0 else "white"
            img = self.font_desc.render(text, True, pygame.Color(color))
            self.desc_image.blit(img, (pad, y))
            y += img.get_height() + pad//2

        # preview do tile selecionado (2x)
        if self.select:
            preview = pygame.transform.scale(self.select.image, (TILE_SIZE*2, TILE_SIZE*2))
            rect = preview.get_rect(bottomright=(w - pad, h - pad))
            self.desc_image.blit(preview, rect)
            pygame.draw.rect(self.desc_image, "gold", rect, 2)

        self.desc_texture_id = utils.update_texture(self.desc_texture_id, self.desc_image)


    def clear(self):
        self.image.fill("black")
        for linha in range(self.y_tiles):
            pygame.draw.line(self.image, "white", (0,linha * TILE_SIZE), (self.size[0], linha * TILE_SIZE))
        for col in range(self.x_tiles):
            pygame.draw.line(self.image, "white", (col * TILE_SIZE, 0), (col * TILE_SIZE, self.size[1]))
        pygame.draw.rect(self.image, "blue", self.rect_orig, 5)

     
    def update(self, dt): 
        for event in self.events_get():
            if event == Anchor:
                self.clear()             
                self.update_tiles()
            if event == Select: 
                self.clear()             
                self.update_tiles()
                self.update_select()
                self.showPanelDesc()

               
    def update_select(self):       
        tile = self.select               
        if tile:   
            #print("select")          
            pygame.draw.rect(self.image, "gold", tile.rect, 3)
        self.texture_id = utils.update_texture(self.texture_id, self.image)
              

    def update_tiles(self):
        # recria a lista - senao ela cresce com copias a cada redesenho
        self.tiles = []
        i = 1
        for lin in range(self.y_tiles): 
            if i >= len(self.tilemap.codes): break                      
            for col in range(self.x_tiles):
                if i >= len(self.tilemap.codes): break
                tile = Tile(*self.tilemap.codes[i])               
                if tile: 
                    self.tiles.append(tile)                   
                    l = col*TILE_SIZE - (self.anchor[0]*TILE_SIZE)
                    t = lin*TILE_SIZE - (self.anchor[1]*TILE_SIZE)
                    tile.rect.topleft = (l, t)                    
                    self.image.blit(tile.image, tile.rect)
                i += 1
        self.texture_id = utils.update_texture(self.texture_id, self.image)
   

    def draw(self):
        x,y,w,h = self.rect.x, self.rect.y, self.rect.w, self.rect.h        
        utils.draw_textured_quad(self.texture_id, x,y,w,h)

        x,y,w,h = self.desc_rect.x, self.desc_rect.y, self.desc_rect.w, self.desc_rect.h
        utils.draw_textured_quad(self.desc_texture_id, x,y,w,h)


