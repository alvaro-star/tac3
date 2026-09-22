import pygame
from ..constants import WIDTH, HEIGHT, GRAVITY, SIZE_PLAYER
from ..constants import MAP_H, FILE_PLAYER_1, TILE_SIZE, SCALE, FILE_SPRITES_PLAYER
from ..utils import utils


class Player():
    """Classe que gerencia o personagem, suas físicas básicas e inputs."""
    def __init__(self, x=WIDTH*0.2, y=HEIGHT*0.6):
        self.frame_index = 0
        self.frame_speed = 16
        self.current_frame = 0.0
        
        self.textures_walk_right = []        
        self.textures_walk_left = []        
        self.textures_jump = []
        
        for i in range(14):
            img = pygame.image.load(f"assets/image/walk/frame{i:04d}.png").convert_alpha()
            img = pygame.transform.smoothscale(img, SIZE_PLAYER)    
            img_mirror = pygame.transform.flip(img, True, False)            
            self.textures_walk_right.append(utils.surface_to_texture(img))            
            self.textures_walk_left.append(utils.surface_to_texture(img_mirror))

        self.image = img
        self.rect = self.image.get_frect(topleft=(x, y))
        self.texture_stand_right = self.textures_walk_right[0]
        self.texture_stand_left = self.textures_walk_left[0]
         
        # Vetores de movimento e física
        self.direction = pygame.math.Vector2(0, 0)
        self.direction_last = 1       

        self.speed = 300  # Pixels por segundo (multiplicado pelo delta time)
        self.gravity = GRAVITY
        self.jump_speed = -600
        self.is_grounded = False

   
    def get_input(self):
        keys = pygame.key.get_pressed()
               
        # Movimentação Horizontal
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.direction_last = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.direction_last = 1
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
        current_frame = self.current_frame
        # atualizar indice animação
        current_frame += self.frame_speed * dt
        if current_frame >= len(self.textures_walk_right):
            current_frame = 0
            #play_sound(sound_wow)
        self.frame_index = int(current_frame)

        self.current_frame = current_frame

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
        texture = self.texture_stand_right             
        if self.direction.x == 1:
            texture = self.textures_walk_right[self.frame_index]
        elif self.direction.x == -1:
            texture = self.textures_walk_left[self.frame_index]
        else:
            if self.direction_last == -1:
                texture = self.texture_stand_left
            else: texture = self.texture_stand_right
        utils.draw_textured_quad(texture, x,y,w,h)