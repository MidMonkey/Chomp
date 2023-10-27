import pygame

class Grenade(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        # image rect velocity
        self.image = pygame.image.load("Weapons/grenade.png")
        self.image = pygame.transform.scale_by(self.image, 0.2)
        self.rect = self.image.get_rect()
        # self.rect.midtop = pos
        self.velocity = 2
        self.boom_time = 1000
        self.dt = pygame.time.get_ticks()

    def update(self):
        #grenade moves down

        self.rect.y += self.velocity
        if self.boom_time:
            if self.dt - self.boom_time == 0:
                self.kill


    def boom(self):
        self.boom_time = pygame.time.get_ticks()
        # grenade changes it image
        while pygame.time.get_ticks() < self.boom_time + 1000:
            self.image = pygame.image.load('Weapons/explosion3.png')
            self.image = pygame.transform.scale_by(self.image, 0.05)
            self.velocity = 0





