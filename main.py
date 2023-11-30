import pygame
from Player import Player
pygame.init()

BG_COLOR = (0, 255, 200)
WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
pygame.display.flip()

p1 = Player((200, 0, 0),WIDTH, HEIGHT)

running = True

while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.Jump()
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                p1.xspeed = -1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    p1.xspeed = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                p1.xspeed = -0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                p1.xspeed = 0
    p1.update(screen)
    pygame.time.wait(1)
    pygame.display.update()

