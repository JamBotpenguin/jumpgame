import pygame
from Player import Player
pygame.init()

BG_COLOR = (0, 255, 200)
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
pygame.display.flip()

p1 = Player((200, 0, 0))

running = True

while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    p1.update(screen)
    pygame.time.wait(1)
    pygame.display.update()
