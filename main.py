import pygame

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
        if event.type == pygame.KEYUP:  # true when any key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    window.fill((0, 0, 0))  # Setting window background color
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()  # updated window to background color
