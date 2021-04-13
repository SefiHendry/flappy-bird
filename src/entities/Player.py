import pygame
from ..env import CONFIG


class Player:
    def __init__(self, x, y, size, color, speed):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        # self.direction = direction
        self.velocity_x = 0
        self.velocity_y = 0
        self.friction = 0.1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.velocity_y -= self.speed
        if keys[pygame.K_DOWN]:
            self.velocity_y += self.speed
        if keys[pygame.K_LEFT]:
            self.velocity_x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x += self.speed

        if self.x < 0:
            self.x = 0
        if self.x > CONFIG["graphics"]["width"]:
            self.x = CONFIG["graphics"]["width"]

        if self.y < 0:
            self.y=0
        if self.y > CONFIG["graphics"]["height"]:
            self.y = CONFIG["graphics"]["height"]

        # else:
        #     self.y=0
        self.x += self.velocity_x
        self.y += self.velocity_y

        if (self.velocity_x > 0):
            self.velocity_x -= self.friction
        elif (self.velocity_x < 0):
            self.velocity_x += self.friction
        if (self.velocity_y > 0):
            self.velocity_y -= self.friction
        elif (self.velocity_y < 0):
            self.velocity_y += self.friction
