import pygame
from math import sqrt
class Grenade(pygame.sprite.Sprite):
    def __init__(self,pos, fish_group, grenade_group):
        super().__init__()
        # image rect velocity
        self.image = pygame.image.load("Weapons/grenade.png")
        self.image = pygame.transform.scale_by(self.image, 0.2)
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        self.velocity = 2
        self.boom_time = 0
        self.fish_group = fish_group
        self.grenade_group = grenade_group
        self.kill_radius = 150
        self.zombie_fish = []

    def update(self):
        #grenade moves down

        self.rect.y += self.velocity
        self.hit_fish()
        if self.boom_time:
            if pygame.time.get_ticks() - self.boom_time > 500:
                self.kill()
    def hit_fish(self):
        for grenade in self.grenade_group:
            for fish in self.fish_group:
                if pygame.sprite.collide_rect(self, fish):
                    fish.skeleton()



    def boom(self):
        self.boom_time = pygame.time.get_ticks()
        # grenade changes it image
        self.image = pygame.image.load('Weapons/explosion3.png')
        self.image = pygame.transform.scale_by(self.image, 0.05)
        self.velocity = 0
        self.kill_zombie()
        self.kill_fish()




        # Need to find a way to keep the zombie fish from getting killed immediatly

    def kill_fish(self):
        grenade_coord = self.rect.center
        for fish in self.fish_group:
            fish_coord = fish.rect.center
            if self.get_distance(grenade_coord, fish_coord) < self.kill_radius:
                fish.skeleton()
                self.zombie_fish.append(fish)

    def kill_zombie(self):
        grenade_coord = self.rect.center
        for zombie in self.zombie_fish:
            fish_coord = zombie.rect.center
            if self.get_distance(grenade_coord, fish_coord) < self.kill_radius:
                pygame.sprite.Sprite.kill(zombie)


    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return sqrt((x2-x1)**2 + (y2-y1)**2)










