import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Your drawing code here
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()