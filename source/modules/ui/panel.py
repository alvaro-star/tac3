import pygame
from ..display import display

class Panel():
    def __init__(self):
        pass

    def create(self):
        self.delay:int = 1
        self.counter = self.delay                

        # Initialize a font (system default or custom font file)
        #self.font = pygame.font.SysFont("Arial", 14)
        self.font = pygame.font.Font("assets/fonts/Call of Ops Duty II.otf", 30)
        
        
    def draw_fps(self):        
        # Draw it onto the screen at coordinates (x=10, y=10)
        display.screen.blit(self.fps_surface, (10, 10))


    def draw(self):
        self.draw_fps()


    def update(self, dt):        
        self.counter += dt 
        if self.counter >= self.delay:                      
            # clock.get_fps() returns a float, so we convert it to an int, then a string
            fps_text = f"FPS:{str(int(display.clock.get_fps()))}"
            # Render the text (Text, Anti-aliasing, Color)
            self.fps_surface = self.font.render(fps_text, True, pygame.Color("green"))           
            self.counter = 0
            
       

panel = Panel()
