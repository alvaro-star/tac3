import pygame
from ..utils import utils

# direcoes das setas de navegacao
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Button():
    def __init__(self, rect:tuple, action, label:str = None, arrow:tuple = None):
        pygame.font.init()
        self.rect = pygame.Rect(rect)
        self.action = action        # funcao chamada no clique
        self.label = label          # texto (botao salvar)
        self.arrow = arrow          # direcao (botoes de navegacao)
        self.font = pygame.font.Font("assets/fonts/FreeSans.ttf", int(self.rect.h*0.45))
        self.color = pygame.Color("#303030")

        self.image = pygame.Surface(self.rect.size).convert_alpha()
        self.texture_id = utils.surface_to_texture(self.image)
        self.render()


    def render(self):
        w, h = self.rect.size
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, self.color, (0, 0, w, h), border_radius=8)
        pygame.draw.rect(self.image, "white", (0, 0, w, h), 2, border_radius=8)

        if self.arrow:
            # triangulo apontando para a direcao
            dx, dy = self.arrow
            cx, cy, s = w/2, h/2, min(w, h)*0.28
            tip = (cx + dx*s, cy + dy*s)
            base1 = (cx - dx*s - dy*s, cy - dy*s - dx*s)
            base2 = (cx - dx*s + dy*s, cy - dy*s + dx*s)
            pygame.draw.polygon(self.image, "white", [tip, base1, base2])
        if self.label:
            text = self.font.render(self.label, True, pygame.Color("white"))
            self.image.blit(text, text.get_rect(center=(w/2, h/2)))

        self.texture_id = utils.update_texture(self.texture_id, self.image)


    def set_label(self, label:str, color:str):
        self.label = label
        self.color = pygame.Color(color)
        self.render()


    def click(self, x, y):
        if self.rect.collidepoint(x, y):
            self.action()
            return True
        return False


    def draw(self):
        x,y,w,h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
        utils.draw_textured_quad(self.texture_id, x,y,w,h)
