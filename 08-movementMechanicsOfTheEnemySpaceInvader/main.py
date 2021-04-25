import pygame
from random import randint

# iniciar o pygame
pygame.init()

# criar de screen/tela
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# titulo e icon
pygame.display.set_caption('space invaders')

# player/ onde x,y que a imagem serah colocada 
playerImg = pygame.image.load('nave.png')
playerX = 370
playerY = 480
playerX_change = 0

# -------------------------------------------
# enemy / onde x,y que a imagem serah colocada 
enemyImg = pygame.image.load('enemy.png')
enemyX = randint(0, 800)
enemyY = randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40



def player(x, y):
    screen.blit(playerImg, (x, y)) # imagemDoPlayer, (x, y do player)

def enemy(x, y):
    screen.blit(enemyImg, (x, y)) # imagemDoEnemy, (x, y do enemy)
    
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

    # Player e enemy aqui serve para nao passar nas bordas quando eles se movimentarem
    # =-=-=-= player movement =-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: # 736 por causa do tamanho de pixels da nava/imagem
        playerX = 736
    

    #=-=-=-= Enemy movement =-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    enemyX += enemyX_change        
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change 
    elif enemyX >= 736: # 736 por causa do tamanho de pixels
        enemyX_change = -0.3

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    
    pygame.display.update()

