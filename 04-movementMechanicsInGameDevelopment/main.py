import pygame

# iniciar o pygame
pygame.init()

# criar de screen/tela
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


# titulo e icon
pygame.display.set_caption("space invaders")

# player/ onde x,y que a imagem serah colocada 
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480

def player(x, y):
    screen.blit(playerImg, (x, y)) # imagemDoPlayer, (x, y do player)


# game loop
running = True
while running:
    # RGB = red green blue
    screen.fill((0, 0, 0))

    playerX += .1 # para movimentar 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player(playerX, playerY)
    pygame.display.update()

