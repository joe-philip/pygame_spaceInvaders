import pygame
import random
score = 0

pygame.init()  # Initialize pygame

window = pygame.display.set_mode((800, 600))  # create game window

pygame.display.set_caption("Space Invaders")  # Setting game caption

# Setting Icon for app always 16x16 size images
Icon = pygame.image.load("Images/Icon.png")
pygame.display.set_icon(Icon)  # Loading icon to app

# loading player image
player_spaceship = pygame.image.load("Images/player.png")
# X position of the image on the screen,Y position of the image on the screen
(playerX, playerY) = (370, 480)
(playerX_change, playerY_change) = (0, 0)


def player(playerX, playerY):
    # the blit function is used to draw objects to the game window
    window.blit(player_spaceship, (playerX, playerY))


# defining Enemy
enemyImage = pygame.image.load("Images/enemy.png")
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_Change = 0.3
enemyY_Change = 40


def enemy(enemyX, enemyY):
    window.blit(enemyImage, (enemyX, enemyY))


# defining bullet
bulletImage = pygame.image.load("Images/bullet.png")
(bulletX, bulletY) = (370, 480)
(bulletX_change, bulletY_change) = (0, 1)
bulletReady = True


def fireBullet(x_pos, y_pos):
    global bulletReady
    bulletReady = False
    window.blit(bulletImage, (x_pos+16, y_pos+10))


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
            if event.key == pygame.K_SPACE:
                bulletY_change = 1
                if bulletY == 480:
                    (bulletX, bulletY) = (playerX, playerY)
                bulletReady = False
            if event.key == pygame.K_ESCAPE:
                gameRunning = False

        if event.type == pygame.KEYUP:  # true when any key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    window.fill((0, 0, 0))  # Setting window background color
    if not bulletReady:
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:  # check wether bullet has reached top of screen
        bulletY = 480
        bulletReady = True
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
        enemyY += enemyY_Change
    elif enemyX >= 736:
        enemyX_Change = -0.3
        enemyY += enemyY_Change
    # collission detection
    if enemyY <= bulletY <= enemyY+16 and ((enemyX <= bulletX+32 <= enemyX+32) or (enemyX <= bulletX <= enemyX+32)):
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)
        bulletReady = not bulletReady
        (bulletX, bulletY) = (playerX, playerY)
        score += 1
        print(score)
        enemy(enemyX, enemyY)

    enemy(enemyX, enemyY)
    pygame.display.update()  # updated window to background color
