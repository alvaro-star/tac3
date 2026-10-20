import pygame
from ..utils import utils
from ..constants import *


class Scroll():
    def __init__(self, size:tuple[int,int]):                            
        w, h = size        
        self.clicked = False        
        self.color = COLOR_SCROLL
        
        # adaptative button size       
        self.image = pygame.Surface((w,h)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect_original = self.rect.copy()
        pygame.draw.rect(self.image, self.color, self.rect, 1)

        slider_size = (w,w) if w < h else (h,h)
        self.image_slider = pygame.Surface(slider_size).convert_alpha()
        self.image_slider.fill(self.color)
        self.rect_slider = self.image_slider.get_rect()

        # Converte e guarda o ID da GPU
        self.texture_id = utils.surface_to_texture(self.image)
       
       
    
    def update_slider_vertical(self, y_tiles, anchor, max_y):        
        # position anchor - topleft
        final_pos = self.rect.h - self.rect_slider.h
        max = max_y - y_tiles
        percentage = anchor[1] / max
        self.rect_slider.topleft = (0, int(final_pos*percentage)) 
        
        self.image.fill("black") # clear
        pygame.draw.rect(self.image, self.color, self.rect_original, 1)
        self.image.blit(self.image_slider, self.rect_slider)
        self.texture_id = utils.update_texture(self.texture_id, self.image)
        


    def update_slider_horizontal(self, x_tiles, anchor, max_x):                
        final_pos = self.rect.w - self.rect_slider.w
        max = max_x - x_tiles
        percentage = anchor[0] / max
        self.rect_slider.topleft = (int(final_pos*percentage), 0)

        self.image.fill("black")
        pygame.draw.rect(self.image, self.color, self.rect_original, 1)
        self.image.blit(self.image_slider, self.rect_slider)
        self.texture_id = utils.update_texture(self.texture_id, self.image)
        

    def set_clicked(self):
        self.clicked = True

    def unset_clicked(self):
        self.clicked = False
      
    def update(self, dt:float): 
        pass       
        #self.clicked = False
        '''for event in notify.get_events():
            if event.type == EVENT_ANCHOR_VERTICAL:
                self.update_slider_vertical()  
            if event.type == EVENT_ANCHOR_HORIZONTAL:
                self.update_slider_horizontal() '''
        '''for event in self.events_get():            
            if event == Clicked:
                self.clicked = True
            if event == AnchorV:
                self.update_slider_vertical()                
            if event == AnchorH:
                self.update_slider_horizontal()'''


    def draw(self):            
        utils.draw_textured_quad(self.texture_id, *self.rect) 
