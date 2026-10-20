import pygame
from ..utils import utils
from ..constants import TILE_SIZE
from ..constants import *#TILE_CROP, FILE_MAP_1


class Tile():
    def __init__(self,
                 id:int, 
                 surf:pygame.Surface,
                 desc:str,
                 w=TILE_SIZE,
                 h=TILE_SIZE):
        
        self.id = id
        self.image = surf
        self.desc = desc

        if w != TILE_CROP or h != TILE_CROP:            
            self.image = pygame.transform.smoothscale(self.image, (w,h))
        self.rect = self.image.get_rect()

        # Converte e guarda o ID da GPU        
        self.texture_id = utils.surface_to_texture(self.image)


    def get(self):
        return self.id, self.image, self.desc 
         
       
    def draw(self):
        x,y = self.rect.x, self.rect.y
        w,h = self.rect.w, self.rect.h                
        utils.draw_textured_quad(self.texture_id, x,y,w,h)


class TileMap():
    def load_sprite_maps(self):
        self.map_items = utils.load_image(FILE_MAP_1)
        self.map_items2 = utils.load_image(FILE_MAP_2)
        
        # items        
        #self.floor1 = self.map_items.subsurface((0,208,TILE_CROP,TILE_CROP))
        #self.floor2 = self.map_items.subsurface((768,448,TILE_CROP,TILE_CROP))
        #self.brick1 = self.map_items.subsurface((320,144,TILE_CROP,TILE_CROP))
        #self.brick2 = self.map_items.subsurface((832,400,TILE_CROP,TILE_CROP))

        # collide objects        
        left = [0,3235,768,832,448,464,448,464,2192,976,976,992,992,1008,1008]        
        top = [176,139,416,368,144,144,160,160,128,384,400,384,400,384,400]
        w = [TILE_CROP] * len(left)
        h = [TILE_CROP] * len(left)
        self.objects, self.objects_mask = self.cut_sub_surface(self.map_items2, left, top, w, h)

        #pygame.image.save(self.floor1,"1.png")
      
        # object codes
        self.codes = []            
            #None,   # code by index - 0 draw nothing
            #(1, self.floor1, "floor1"),     
            # id, surface, description
            #(2, self.floor2, "floor2"),
            #(3, self.brick1, "brick1"),
            #(4, self.brick2, "brick2")
        #]
        i = 0
        for surf in self.objects:
            self.codes.append((i, surf, f"collide {i}"))
            i += 1

        # objects that not collide - background
        left = [136,152,136,151,456,455,664,680,696,257,272,1568,1584,272,287]        
        top = [16,16,32,32,16,32,160,160,160,160,160,160,160,145,160]
        w = [TILE_CROP] * len(left)
        h = [TILE_CROP] * len(left)
        self.back, self.back_mask = self.cut_sub_surface(self.map_items2, left, top, w, h)

        for surf in self.back:
            self.codes.append((i, surf, f"background {i}"))
            i += 1


    def create_tile_matrix(self, cols):
        self.tiles:list[list[Tile]] = []
        i = 1
        for lin in range(TILE_MAP_PALLET):
            line = []           
            for col in range(cols):                 
                if i < len(self.codes):
                    obj = Tile(*self.codes[i])
                    x, y = col, lin # 2d position
                    obj.rect.topleft = (x*TILE_SIZE, y*TILE_SIZE)
                    line.append(obj)                
                else: line.append(None) 
                i += 1 
            self.tiles.append(line)


    def cut_sub_surface(self, surface:pygame.Surface, left, top, w, h):        
        list = []
        mask_list = []
        if not (len(left) == len(top) == len(w) == len(h)):
            print('Subsurface empty list!!!')
            return list, mask_list      
        for i in range(len(left)):
            surf = surface.subsurface((left[i],top[i]),(w[i],h[i]))                        
            list.append(surf)
            mask = pygame.mask.from_surface(surf)
            mask_list.append(mask)
        return list, mask_list
    
#tile_map = TileMap()