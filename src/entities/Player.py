import pygame
from ..env import CONFIG
import os
from ..entities import Obstacle


class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.jump = 5.5
        self.gravity = 0.3
        self.velocity_x = 0
        self.velocity_y = 0
        self.score = 0
        # self.image = pygame.image.load(CONFIG["path"]["player"])

    def draw(self, screen):
        pass
        # screen.blit(self.image,(self.x, self.y))
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def move(self, keys):
        #     if keys[pygame.K_UP]:
        #         self.velocity_y -= self.speed
        #     if keys[pygame.K_DOWN]:
        #         self.velocity_y += self.speed
        #     if keys[pygame.K_LEFT]:
        #         self.velocity_x -= self.speed
        #     if keys[pygame.K_RIGHT]:
        #         self.velocity_x += self.speed

        if keys[pygame.K_SPACE]:
            self.velocity_y = -1 * self.jump

        if self.x < 0:
            self.x = 0
        if self.x > CONFIG["graphics"]["width"]:
            self.x = CONFIG["graphics"]["width"]

        if self.y < 0:
            self.y = 0
        if self.y > CONFIG["graphics"]["height"]:
            self.velocity_y *= -0.8
            self.y = CONFIG["graphics"]["height"]

        self.x += self.velocity_x
        self.y += self.velocity_y

        # if (self.velocity_x > 0):
        #     self.velocity_x -= self.friction
        # elif (self.velocity_x < 0):
        #     self.velocity_x += self.friction
        # if (self.velocity_y > 0):
        #     self.velocity_y -= self.friction
        # elif (self.velocity_y < 0):
        self.velocity_y += self.gravity

    def collision(self, obstacle1):
        if ((self.y <= obstacle1.up_y_finish)
                and (self.x <= obstacle1.up_x + obstacle1.size / 1.5 and self.x >= obstacle1.up_x - obstacle1.size / 1.5)
                or (self.y >= obstacle1.up_y_finish + obstacle1.margin)
                and (self.x <= obstacle1.up_x + obstacle1.size / 1.5 and self.x >= obstacle1.up_x - obstacle1.size / 1.5)):
            self.score = 0
            return True
        return False
