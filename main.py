import pygame
pygame.init()  # Initialize pygame
window = pygame.display.set_mode((800, 600))  # create game window
pygame.display.set_caption("Game Caption")  # Setting game caption
gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when close button is pressed
            gameRunning = False
