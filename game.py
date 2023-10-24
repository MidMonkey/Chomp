import pygame
from random import randint

# pygame setup
pygame.init()
# Set window resolution
WIDTH = 1080
HEIGHT = 650
sand_height = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sand = pygame.image.load("Fishpics/fishTile_021.png")
weed = pygame.image.load("Fishpics/fishTile_030.png")
fish = pygame.image.load("Fishpics/fishTile_073.png")
picwidth= sand.get_width()
picheight = sand.get_height()
wh = randint(picheight, 2 * picheight)
ww = randint(0, WIDTH)
nwh = randint(picheight, 2 * picheight)
nww = randint(0, WIDTH)
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((52, 140, 235))
clock = pygame.time.Clock()
running = True
dt = 0
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # background.fill(50, 20, 255)
    pygame.draw.rect(background, (204, 179, 129), (0, HEIGHT - sand_height, WIDTH, sand_height))
    screen.blit(background, (0, 0))
    for i in range(1, 100):
        screen.blit(sand, (WIDTH - i * picwidth, HEIGHT - picheight))
    screen.blit(weed, (WIDTH - ww, HEIGHT - wh))
    screen.blit(weed, (WIDTH - nww, HEIGHT - nwh))
    screen.blit(fish, (ww, HEIGHT - 2 * wh))



    # pygame.QUIT event means the user clicked X to close your window
    # fill the screen with a color to wipe away anything from last frame
    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for frame rate-
    # independent physics.
    # dt = clock.tick(60) / 1000

pygame.quit()

# define a class
# attributes image, rect, velocity
#methods
#updade
#draw(takes screen as argument).