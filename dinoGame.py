import pygame
from sys import exit

pygame.init()
screen =  pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dino Armageddon')   # Window name
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 80)

background = pygame.image.load('ui/background.png').convert()
text_surface = test_font.render("Dino Armageddon", False, "Orange").convert()

# fireball object (to dodge)
fireball_surface = pygame.image.load('ui/fireball.png').convert_alpha()
fireball_surface_downscaled = pygame.transform.smoothscale(fireball_surface, (120, 70)).convert_alpha()
fireball_rect = fireball_surface_downscaled.get_rect(midbottom = (1280,600)) # fireball position

# player object
player_surface = pygame.image.load("ui/dino_walk.png").convert_alpha()
player_surface_downscaled = pygame.transform.smoothscale(player_surface, (160, 90)).convert_alpha()
player_rect = player_surface_downscaled.get_rect(midbottom = (80,600)) # dino position


while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    screen.blit(background, (0, 0))
    screen.blit(text_surface, (350, 300))

    fireball_rect.x -=3
    if fireball_rect.right <= 0:
        fireball_rect.left = 1280

    screen.blit(fireball_surface_downscaled,fireball_rect)
    screen.blit(player_surface_downscaled,player_rect)

    pygame.display.update()
    clock.tick(180)
