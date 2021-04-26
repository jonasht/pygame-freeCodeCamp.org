import pygame
from random import randint
from math import sqrt, pow
from pygame.constants import K_ESCAPE, K_q

# iniciar o pygame
pygame.init()

# criar de screen/tela
screen = pygame.display.set_mode((800, 600))  # definindo tamanho da tela x y
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('background.png')

# titulo e icon
pygame.display.set_caption('space invaders')


# ------------------------------------------------------
# player/ onde x,y que a imagem serah colocada
playerImg = pygame.image.load('nave.png')
playerX = 370
playerY = 480
playerX_change = 0

# ------------------------------------------------------
# enemy / onde x,y que a imagem serah colocada
enemyImg = pygame.image.load('enemy.png')
enemyX = randint(0, 735)
enemyY = randint(50, 150)
enemyX_change = .3
enemyY_change = 40

# ------------------------------------------------------
# bullet | onde x,y que a imagem serah colocada
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'  # ready - means that you can see the bullet on the screen
# fire - means that the bullet is currently moving

score = 0 # pontos


def player(x, y):
    screen.blit(playerImg, (x, y))  # imagemDoPlayer, (x, y do player)


def enemy(x, y):
    screen.blit(enemyImg, (x, y))  # imagemDoEnemy, (x, y do enemy)


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = sqrt((pow(enemyX-bulletX, 2)) + (pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True 
    else:
        return False


# game loop
running = True
while running:
    # RGB = red green blue
    screen.fill((0, 0, 0))

    # background image em loop
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == K_ESCAPE:
            running = False

    # se keystroke for pressionado check se eh direita ou esquerda
        if event.type == pygame.KEYDOWN:  # 1-quando a tecla estah sendo apartada
            if event.key == K_ESCAPE or event.key == K_q:  # para fechar
                print('esc/q foi apartado')
                running = False
            if event.key == pygame.K_LEFT:
                # print('left foi pressionado')
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                # print('right foi pressionado')
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # 2-quando a tecla estah sendo desapartada
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print('keystoke has been released/tecla foi despressionada')
                playerX_change = 0

    # Player e enemy aqui serve para nao passar nas bordas quando eles se movimentarem
    # =-=-=-= player movement =-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 736 por causa do tamanho de pixels da nava/imagem
        playerX = 736

    # =-=-=-= Enemy movement =-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = .3
        enemyY += enemyY_change
    elif enemyX >= 736:  # 736 por causa do tamanho de pixels
        enemyX_change = -.3
        enemyY += enemyY_change

    # =-=-=-= bullet movement =-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # colisao de bala com alien / collision
    Collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if Collision:
        bulletY = 480
        bullet_state = 'ready'
        score += 1 # fazendo pontos
        print(score)
        enemyX = randint(5, 800)
        enemyY = randint(100, 150)
        

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
