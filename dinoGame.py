import pygame
from sys import exit

def display_score():
    current_time = int(round((pygame.time.get_ticks() - start_time) / 1000,0))
    score_surf = test_font.render(str(current_time), False, 'Orange')
    score_rect = score_surf.get_rect(center = (650, 100))
    screen.blit(score_surf, score_rect)

pygame.init()
screen =  pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dino Armageddon')   # Window name
clock = pygame.time.Clock()

game_active = True
start_time = 0

test_font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 80)

background = pygame.image.load('ui/background.png').convert()

# score_surf = test_font.render("Dino Armageddon", False, "Orange").convert()
# score_rect = score_surf.get_rect(center = (650, 300))

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

            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.bottom >=600:
                        player_gravity = -20
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True
                        fireball_rect.left = 900
                        start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(background, (0, 0))
        score = display_score()

        # Fireball animation and looping
        fireball_rect.x -=8
        if fireball_rect.right <= 0:
            fireball_rect.left = 1280

        # Player gravity
        player_gravity += 0.7
        player_rect.y += player_gravity
        if player_rect.bottom >= 600:
            player_rect.bottom = 600
        screen.blit(player_surface_downscaled, player_rect)

        screen.blit(fireball_surface_downscaled,fireball_rect)
        screen.blit(player_surface_downscaled,player_rect)

        # collision
        if fireball_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('red')

    pygame.display.update()
    clock.tick(60)
