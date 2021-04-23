import pygame

# iniciar o pygame
pygame.init()

# criar de screen/tela
screen = pygame.display.set_mode((800, 600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
