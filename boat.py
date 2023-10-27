import pygame
from math import sin

class Boat(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load('Fishpics/ship-clipart-45.png')
        self.image = pygame.transform.scale_by(self.image,0.15)
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width()/2
        self.rect.y = 10
        self.velocity = -1
    def update(self):
        self.rect.x += self.velocity
    def draw(self, screen):
        screen.blit(self.image, self.rect)
