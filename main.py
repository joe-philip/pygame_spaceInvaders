import pygame
pygame.init()  # Initialize pygame
window = pygame.display.set_mode((800, 600))  # create game window
pygame.display.set_caption("Space Invaders")  # Setting game caption
Icon = pygame.image.load("Images/Icon.png")  # Setting Icon for app
pygame.display.set_icon(Icon)  # Loading icon to app
gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when close button is pressed
            gameRunning = False
