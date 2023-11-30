

import pygame

GRAVITY = 0.02
class Player:

    def __init__(self, color, w, h):
        self.c = color
        self.radius = 25
        self.yspeed = 0
        self.xspeed = 0
        self.x = 500
        self.y = 300
        self.w = w
        self.h = h


    def update(self, screen):
        self.yspeed += GRAVITY
        self.y += self.yspeed
        self.x += self.xspeed
        self.wallcolision()
        pygame.draw.circle(screen, self.c,(self.x, self.y), self.radius )

    def Jump(self):
        self.yspeed = -3

    def wallcolision(self):
        if self.y <= 0 + self. radius:
            self.y = 0 + self. radius
            self.yspeed = 0.5
        if self.y >= self.h - self. radius:
            self.y = self.h - self. radius
            self.yspeed = 0.5