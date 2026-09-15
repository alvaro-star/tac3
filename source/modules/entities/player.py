import pygame
from ..constants import WIDTH, HEIGHT, GRAVITY, SIZE_PLAYER
from ..constants import MAP_H, MAP_W, FILE_PLAYER_1, TILE_SIZE
from ..utils import utils


class Player():
    """Classe que gerencia o personagem, suas físicas básicas e inputs."""
    def __init__(self, x=WIDTH*0.2, y=HEIGHT*0.6):
        #super().__init__()
        # Cria um quadrado temporário enquanto não há sprites carregados
        #self.image = pygame.Surface((40, 60))
        #self.image.fill(pygame.Color("#5A1A1A"))
        self.image = utils.load_image(FILE_PLAYER_1)
        self.image = pygame.transform.smoothscale(self.image, SIZE_PLAYER)
        self.rect = self.image.get_frect(topleft=(x, y))

        # Converte e guarda o ID da GPU
        self.texture_id = utils.surface_to_texture(self.image)
        
        # Vetores de movimento e física
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 300  # Pixels por segundo (multiplicado pelo delta time)
        self.gravity = GRAVITY
        self.jump_speed = -600
        self.is_grounded = False

        #self.dirty = 1 # Draw once initially
        #self._layer = LAYER_PLAYER

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


    def apply_gravity(self, dt:float):
        self.direction.y += self.gravity * dt
        self.rect.y += self.direction.y * dt


    def update(self, dt):
        #self.dirty = 1

        self.get_input()
        
        # Atualiza posição horizontal baseada no tempo delta (dt)
        self.rect.x += self.direction.x * self.speed * dt
        self.apply_gravity(dt)
        
        # Simulação temporária de colisão com o "chão" da tela        
        floor = (int(MAP_H*0.9)*TILE_SIZE) + TILE_SIZE        
        if self.rect.bottom >= floor:
            self.rect.bottom = floor
            self.direction.y = 0
            self.is_grounded = True


    def draw(self):
        x,y,w,h = self.rect.x, self.rect.y, self.rect.w, self.rect.h        
        utils.draw_textured_quad(self.texture_id, x,y,w,h)