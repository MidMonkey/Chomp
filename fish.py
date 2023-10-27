import random
import pygame

class Fish(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('Fishpics/fishTile_080.png')
        self.image = pygame.transform.flip(self.image, 1,0)
        self.speed = random.random() * 6
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(100,(screen.get_height()-200))
        self.x = screen.get_width()
        self.screen = screen
    def update(self):
        self.x = self.x - int(self.speed)
        if self.x < 0:
            self.x = self.screen.get_width()
        self.rect.x = self.x