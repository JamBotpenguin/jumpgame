

import pygame

GRAVITY = 0.02
class Player:

    def __init__(self, color):
        self.c = color
        self.radius = 25
        self.speed = 0
        self.x = 400
        self.y = 300


    def update(self, screen):
        self.speed += GRAVITY
        self.y += self.speed
        pygame.draw.circle(screen, self.c,(self.x, self.y), self.radius )