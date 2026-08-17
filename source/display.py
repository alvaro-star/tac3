import pygame as pg
from .constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, TITLE

class Display():
    def create_display(self):
        self.fps = 0
        self.clock = pg.time.Clock()  
        self.__size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
        #self.__info = pg.display.Info()
       
        pg.display.set_caption(TITLE) 
        self.screen = pg.display.set_mode(self.__size)             
        
    def reload(self):
        pass

    @property
    def size(self):
        return self.__size
     

display = Display()