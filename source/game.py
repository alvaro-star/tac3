import pygame as pg
import sys
from .display import display

class Game():
    def __init__(self):  
        pass

    def load_assets(self):
        pg.init()
        display.create_display()
        #splash() 
        # load sprites, sounds, etc


    def start(self):
        self.running = True 


    def quit(self):
        self.running = False        
        pg.quit()
        sys.exit()

game = Game()