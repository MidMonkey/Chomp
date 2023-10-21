import pygame

# pygame setup
pygame.init()
# Set window resolution
WIDTH = 800
HEIGHT = 600
sand_height = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sand = pygame.image.load("kenney_fish_pack.zip/Preview.png").convert()
screen.blit(sand, (200,200,64,64))
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
    pygame.draw.rect(background, (204, 179, 129), (0, HEIGHT-sand_height, WIDTH, sand_height))
    screen.blit(background, (0,0))
    # pygame.QUIT event means the user clicked X to close your window
    # fill the screen with a color to wipe away anything from last frame
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for frame rate-
    # independent physics.
    # dt = clock.tick(60) / 1000

pygame.quit()
