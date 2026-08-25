import pygame
from ..constants import HEIGHT, PLAYER_COLOR


class Player(pygame.sprite.Sprite):
    """Classe que gerencia o personagem, suas físicas básicas e inputs."""
    def __init__(self, x, y):
        super().__init__()
        # Cria um quadrado temporário enquanto não há sprites carregados
        self.image = pygame.Surface((40, 60))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_frect(topleft=(x, y))
        
        # Vetores de movimento e física
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 300  # Pixels por segundo (multiplicado pelo delta time)
        self.gravity = 1200
        self.jump_speed = -500
        self.is_grounded = False

    def get_input(self):
        keys = pygame.key.get_pressed()
        
        # Movimentação Horizontal
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        # Pulo
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.is_grounded:
            self.direction.y = self.jump_speed
            self.is_grounded = False

    def apply_gravity(self, dt):
        self.direction.y += self.gravity * dt
        self.rect.y += self.direction.y * dt

    def update(self, dt):
        self.get_input()
        
        # Atualiza posição horizontal baseada no tempo delta (dt)
        self.rect.x += self.direction.x * self.speed * dt
        self.apply_gravity(dt)
        
        # Simulação temporária de colisão com o "chão" da tela
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.direction.y = 0
            self.is_grounded = True