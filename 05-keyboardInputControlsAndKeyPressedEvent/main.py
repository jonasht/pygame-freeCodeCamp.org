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
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y)) # imagemDoPlayer, (x, y do player)


# game loop
running = True
while running:
    # RGB = red green blue
    screen.fill((0, 0, 0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # se keystroke for pressionado check se eh direita ou esquerda
        if event.type == pygame.KEYDOWN: # 1-quando a tecla estah sendo apartada
            if event.key == pygame.K_LEFT:
                # print('left foi pressionado')   
                playerX_change = -.3   
            if event.key == pygame.K_RIGHT:
                # print('right foi pressionado')
                playerX_change = .3

            
        if event.type == pygame.KEYUP: # 2-quando a tecla estah sendo desapartada 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print('keystoke has been released/tecla foi despressionada')
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()

