"""
Last Dino - a simple arcade game

To start the game and jump, press space. The longer space is held the higher the dino jumps.

The game features only very simple logic, including:
- Player input checking, jumping and simple gravity simulation
- Variable object (fireballs) spawning and collision detection
- Timer based score counting
"""

import pygame
from sys import exit
from random import randint

# --------------------- Helper function(s) -----------------------------

def display_score():
    """Display elapsed time since game start and return current score."""
    current_time = int(round((pygame.time.get_ticks() - start_time) / 1000,0))
    score_surf = test_font.render(str(current_time), False, 'Orange')
    score_rect = score_surf.get_rect(center = (650, 100))
    screen.blit(score_surf, score_rect)
    return current_time

# --------------------- Pygame setup -----------------------------

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/PixelifySans-VariableFont_wght.ttf', 50)
pygame.display.set_caption('Last Dino')

background = pygame.image.load('ui/background.png').convert()

# --------------------- Audio -----------------------------
# Sound effects from https://sounds.spriters-resource.com/)

jump_sound = pygame.mixer.Sound("sounds/dino_jump.wav")
death_sound = pygame.mixer.Sound("sounds/dino_death.WAV")

jump_sound.set_volume(0.4)
death_sound.set_volume(0.6)

# --------------------- Game state -----------------------------
game_active = False
start_time = 0
score = 0

# --------------------- Fireball (obstacle) -----------------------------
fireball_surface = pygame.image.load('ui/fireball.png').convert_alpha()
fireball_surface_downscaled = pygame.transform.smoothscale(fireball_surface, (120, 70)).convert_alpha()

fireball_rect = fireball_surface_downscaled.get_rect(midbottom=(1400, 600))

fireball_speed = 8
fireball_active = True
fireball_spawn_time = 0
fireball_delay = 0

# --------------------- Player character -----------------------------
player_surface = pygame.image.load("ui/dino_walk.png").convert_alpha()
player_surface_downscaled = pygame.transform.smoothscale(player_surface, (160, 90)).convert_alpha()

player_rect = player_surface_downscaled.get_rect(midbottom=(80, 600))

player_gravity = 0
jumping = False

# --------------------- Intro screen -----------------------------
game_name =  test_font.render("Last Dino (press space to start)", False, "orange")
game_name_rect = game_name.get_rect(center = (650, 600))


# --------------------- Main game loop -----------------------------
while True:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:

                # Jump input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.bottom >= 600:
                        player_gravity = -22  # max jump
                        jumping = True
                        jump_sound.play()

                # Variable jump height
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE and jumping:
                        if player_gravity < -15:
                            player_gravity = -15
                        jumping = False

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_active = True
                        start_time = pygame.time.get_ticks()

                        fireball_rect.left = 900
                        fireball_speed = 8
                        fireball_active = True
                        fireball_rect.left = 900
                        fireball_spawn_time = 0
                        fireball_delay = 0

    # -------------- Game logic ---------------------
    if game_active:
        screen.blit(background, (0, 0))

        # Score and difficulty scaling
        score = display_score()
        fireball_speed = 8 + score * 0.2


        # Fireball movement and respawn delay
        if fireball_active:
            fireball_rect.x -= fireball_speed

            if fireball_rect.right <= 0:
                fireball_active = False
                fireball_spawn_time = pygame.time.get_ticks()
                fireball_delay = randint(500, 1500)
        else:
            if pygame.time.get_ticks() - fireball_spawn_time >= fireball_delay:
                fireball_active = True
                fireball_rect.left = 1280
                fireball_rect.bottom = randint(540, 600)

        # Player gravity and ground collision
        player_gravity += 0.7
        player_rect.y += player_gravity

        if player_rect.bottom >= 600:
            player_rect.bottom = 600
            jumping = False

        if fireball_active:
            screen.blit(fireball_surface_downscaled, fireball_rect)

        screen.blit(player_surface_downscaled,player_rect)

        # collision detection
        if fireball_active and fireball_rect.colliderect(player_rect):
            game_active = False
            death_sound.play()

    # -------------- Menu/game over screen ---------------------
    else:
        screen.blit(background, (0, 0))

        if score == 0:
            screen.blit(game_name, game_name_rect)
        else:
            score_message = test_font.render(f"Last score: {score}", False, "orange")
            score_message_rect = score_message.get_rect(center=(650, 600))
            screen.blit(score_message, score_message_rect)

    # Frame update
    pygame.display.update()
    clock.tick(60)
