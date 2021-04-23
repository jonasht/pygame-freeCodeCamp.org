import pygame

# iniciar o pygame
pygame.init()

# criar de screen/tela
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

running = True

# titulo e icon
pygame.display.set_caption("space invaders")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # RGB = red green blue
    screen.fill((255, 0, 0))
    pygame.display.update()

