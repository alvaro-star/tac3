import pygame
from .game import game
from .display import display

def run():
    game.start()
    # Main game loop
    while game.running:           
        # Process input events (like clicking the close button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.quit()

        # Fill background color (e.g., dark gray/black)
        display.screen.fill((30, 30, 30))

        # Refresh the display surface
        pygame.display.flip()

        # Limit frame rate to 60 FPS
        display.clock.tick(60)