import pygame
from sys import exit

pygame.init()
screen =  pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dino Armageddon')   # Window name
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 80)

background = pygame.image.load('ui/background.png').convert()
# Maybe add separate ground texture?
text_surface = test_font.render("Dino Armageddon", False, "Orange").convert()
fireball_surface = pygame.image.load('ui/fireball.png').convert_alpha()
fireball_surface_downscaled = pygame.transform.smoothscale(fireball_surface, (120, 70)).convert_alpha()

fireball_x_pos =  600

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    screen.blit(background, (0, 0))
    screen.blit(text_surface, (350, 300))

    if fireball_x_pos < 0:
        fireball_x_pos = 1380

    fireball_x_pos -= 1

    screen.blit(fireball_surface_downscaled, (fireball_x_pos, 250))

    pygame.display.update()
    clock.tick(180)
