import pygame
import random

pygame.init()  # Initialize pygame

window = pygame.display.set_mode((800, 600))  # create game window

pygame.display.set_caption("Space Invaders")  # Setting game caption

# Setting Icon for app always 16x16 size images
Icon = pygame.image.load("Images/Icon.png")
pygame.display.set_icon(Icon)  # Loading icon to app

# loading player image
player_spaceship = pygame.image.load("Images/player.png")
playerX = 370  # X position of the image on the screen
playerY = 480  # Y position of the image on the screen
playerX_change = 0
playerY_change = 0


def player(playerX, playerY):
    # the blit function is used to draw objects to the game window
    window.blit(player_spaceship, (playerX, playerY))


# defining Enemy
enemyImage = pygame.image.load("Images/enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Change = 0.3
enemyY_Change = 40


def enemy(enemyX, enemyY):
    window.blit(enemyImage, (enemyX, enemyY))


gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when close button is pressed
            gameRunning = False

        if event.type == pygame.KEYDOWN:  # true when any key is pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1
            if event.key == pygame.K_ESCAPE:
                gameRunning = False
        if event.type == pygame.KEYUP:  # true when any key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    window.fill((0, 0, 0))  # Setting window background color
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 530:
        playerY = 530
    player(playerX, playerY)

    enemyX += enemyX_Change
    if enemyX <= 0:
        enemyX_Change = 0.3
        enemyY+=enemyY_Change
    elif enemyX >= 736:
        enemyX_Change = -0.3
        enemyY+=enemyY_Change
    enemy(enemyX, enemyY)
    pygame.display.update()  # updated window to background color
