import pygame
pygame.init()  # Initialize pygame
window = pygame.display.set_mode((800, 600))  # create game window
gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
