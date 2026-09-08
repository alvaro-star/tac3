import pygame
import os
import sys

class Utils():
    def __init__(self):                   
        if getattr(sys, 'frozen', False):
            # Executável compilado com cx_Freeze
            self.path = os.path.dirname(sys.executable)
            # ou no main.py
            #os.path.split(os.path.abspath(__file__))[0]
        else:
            # Modo desenvolvimento (.py)
            self.path = os.path.abspath(".")       
  
    def get_full_path(self, resource):
        return os.path.join(self.path, resource)

    def load_font(self, file, size):
        return pygame.font.Font(os.path.join(self.path, file), size)
    
    def load_image(self, file):
        return pygame.image.load(os.path.join(self.path, file)).convert_alpha()

              

utils = Utils()