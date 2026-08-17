import pygame

# Initialize pygame-ce
pygame.init()

# Set up window size and title
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame-CE Window Skeleton")

# Setup a clock for stable frame rate control
clock = pygame.time.Clock()
running = True

# Main game loop
while running:
    # Process input events (like clicking the close button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background color (e.g., dark gray/black)
    screen.fill((30, 30, 30))

    # Refresh the display surface
    pygame.display.flip()

    # Limit frame rate to 60 FPS
    clock.tick(60)

# Safely exit
pygame.quit()