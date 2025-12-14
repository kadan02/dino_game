import pygame
from sys import exit

def display_score():
    current_time = int(round((pygame.time.get_ticks() - start_time) / 1000,0))
    score_surf = test_font.render(str(current_time), False, 'Orange')
    score_rect = score_surf.get_rect(center = (650, 100))
    screen.blit(score_surf, score_rect)
    return current_time

pygame.init()
pygame.mixer.init()

# sound effects (from https://sounds.spriters-resource.com/)
jump_sound = pygame.mixer.Sound("sounds/dino_jump.wav")
death_sound = pygame.mixer.Sound("sounds/dino_death.WAV")
jump_sound.set_volume(0.4)
death_sound.set_volume(0.6)

screen =  pygame.display.set_mode((1280, 720))
test_font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 50)
pygame.display.set_caption('Dino Armageddon')   # Window name
clock = pygame.time.Clock()
background = pygame.image.load('ui/background.png').convert()

game_active = False
start_time = 0
score = 0

# fireball object (to dodge)
fireball_surface = pygame.image.load('ui/fireball.png').convert_alpha()
fireball_surface_downscaled = pygame.transform.smoothscale(fireball_surface, (120, 70)).convert_alpha()
fireball_rect = fireball_surface_downscaled.get_rect(midbottom = (1280,600)) # fireball position
fireball_speed = 8


# player object
player_surface = pygame.image.load("ui/dino_walk.png").convert_alpha()
player_surface_downscaled = pygame.transform.smoothscale(player_surface, (160, 90)).convert_alpha()
player_rect = player_surface_downscaled.get_rect(midbottom = (80,600)) # dino position
player_gravity = 0

# intro screen
game_name =  test_font.render("Dino Armageddon (press space to start)", False, "orange")
game_name_rect = game_name.get_rect(center = (650, 600))

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.bottom >=600:
                        player_gravity = -20
                        jump_sound.play()
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True
                        fireball_rect.left = 900
                        start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(background, (0, 0))
        score = display_score()

        # Fireball animation and looping
        fireball_speed = 8 + score * 0.2
        fireball_rect.x -= fireball_speed
        if fireball_rect.right <= 0:
            fireball_rect.left = 1280

        # Player gravity
        player_gravity += 0.7
        player_rect.y += player_gravity
        if player_rect.bottom >= 600:
            player_rect.bottom = 600

        screen.blit(fireball_surface_downscaled,fireball_rect)
        screen.blit(player_surface_downscaled,player_rect)

        # collision
        if fireball_rect.colliderect(player_rect):
            game_active = False
            death_sound.play()
            pygame.mixer.music.stop()
    else:
        screen.blit(background, (0, 0))
        score_message = test_font.render(f"Last score: {score}", False,"orange")
        score_message_rect = score_message.get_rect(center = (650, 600))

        if score ==0:
            screen.blit(game_name, game_name_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
