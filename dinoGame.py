import pygame
from sys import exit

pygame.init()
screen =  pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dino Armageddon')   # Window name
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 80)

background = pygame.image.load('ui/background.png').convert()

score_surf = test_font.render("Dino Armageddon", False, "Orange").convert()
score_rect = score_surf.get_rect(center = (650, 300))

# fireball object (to dodge)
fireball_surface = pygame.image.load('ui/fireball.png').convert_alpha()
fireball_surface_downscaled = pygame.transform.smoothscale(fireball_surface, (120, 70)).convert_alpha()
fireball_rect = fireball_surface_downscaled.get_rect(midbottom = (1280,600)) # fireball position

# player object
player_surface = pygame.image.load("ui/dino_walk.png").convert_alpha()
player_surface_downscaled = pygame.transform.smoothscale(player_surface, (160, 90)).convert_alpha()
player_rect = player_surface_downscaled.get_rect(midbottom = (80,600)) # dino position
player_gravity = 0

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20


    screen.blit(background, (0, 0))
    pygame.draw.rect(screen,'Brown', score_rect)
    pygame.draw.rect(screen,'Brown', score_rect, 12)
    screen.blit(score_surf, score_rect)

    # Fireball animation and looping
    fireball_rect.x -=3
    if fireball_rect.right <= 0:
        fireball_rect.left = 1280

    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surface_downscaled, player_rect)

    screen.blit(fireball_surface_downscaled,fireball_rect)
    screen.blit(player_surface_downscaled,player_rect)

#    if player_rect.colliderect(fireball_rect):
#         print('collision')

#    mouse_pos = pygame.mouse.get_pos()
#    if player_rect.collidepoint(mouse_pos):

#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_SPACE]:



    pygame.display.update()
    clock.tick(60)
