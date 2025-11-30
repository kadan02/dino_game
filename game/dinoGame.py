import pygame
from sys import exit

pygame.init()
screen =  pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Dino Survival')   # Window name
clock = pygame.time.Clock()

test_surface = pygame.image.load('ui/background.png')

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    screen.blit(test_surface, (0,0))

    pygame.display.update()
    clock.tick(180)  # Max FPS