import pygame
from random import *
from grenade import Grenade
from fish import Fish
from boat import Boat

# pygame setup
pygame.init()
# set up a clock
clock = pygame.time.Clock()
# Set window resolution
WIDTH = 1080
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# set various dimensions
sand_height = 100
sand = pygame.image.load("Fishpics/fishTile_021.png")
weed = pygame.image.load("Fishpics/fishTile_030.png")
fish = pygame.image.load("Fishpics/fishTile_073.png")
picwidth = sand.get_width()
picheight = sand.get_height()
wh = randint(picheight, 2 * picheight)
ww = randint(0, WIDTH)
nwh = randint(picheight, 2 * picheight)
nww = randint(0, WIDTH)

# make background
background = pygame.Surface((WIDTH, HEIGHT))  #  make_background(screen)
background.fill((153, 246, 255))
# shuow title
print(pygame.font.get_fonts())
game_font = pygame.font.SysFont('impact', 110)

# setup groups
grenade_group = pygame.sprite.Group()
fish_group = pygame.sprite.Group()
boat_group = pygame.sprite.Group()
# setup my boat

bomb_boat = Boat(screen)
boat_group.add(bomb_boat)
# describe fish group
num_fish = 100
[fish_group.add(Fish(screen)) for i in range(num_fish) ]


running = True
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bomb_boat.velocity += 1
            if event.key == pygame.K_LEFT:
                bomb_boat.velocity -= 1
            if event.key == pygame.K_RSHIFT:
                grenade_group.add(Grenade(bomb_boat.rect.center, fish_group, grenade_group))
            if event.key == pygame.K_SPACE:
                [g.boom() for g in grenade_group]
    # update sprites
    fish_group.update()
    grenade_group.update()
    bomb_boat.update()
    # background.fill(50, 20, 255)
    pygame.draw.rect(background, (153, 246, 255), (0, HEIGHT - sand_height, WIDTH, sand_height))
    screen.blit(background, (0, 0))

    for i in range(1, 100):
        screen.blit(sand, (WIDTH - i * picwidth, HEIGHT - picheight))
    screen.blit(weed, (WIDTH - ww, HEIGHT - wh))
    screen.blit(weed, (WIDTH - nww, HEIGHT - nwh))

    # draw sprites and text
    #  if pygame.time.get_ticks() < 2500:
        #  font_surface = game_font.render('Depth Charge!', 1, (42, 65, 102))
        #  center_surfaces(screen, font_surface)

    grenade_group.draw(screen)
    fish_group.draw(screen)
    bomb_boat.draw(screen)
    clock.tick(60)
    #  this means that the game must run at 60 fps
    pygame.display.set_caption(f"Depth Charge {clock.get_fps():0}")

    # pygame.QUIT event means the user clicked X to close your window
    # fill the screen with a color to wipe away anything from last frame
    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for frame rate-
    # independent physics.
    # dt = clock.tick(60) / 1000

pygame.quit()

