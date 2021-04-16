import random

import pygame
from ..env import CONFIG
import os


class Obstacle:
    def __init__(self):
        self.up_x = (CONFIG["graphics"]["width"])
        self.up_y_start = 0
        self.up_y_finish = (CONFIG["graphics"]["height"]) / (random.randrange(2, 8, 1))
        self.down_y_start = 0
        self.margin = 150
        self.size = 70
        self.color = (100, 150, 200)
        self.velocity_x = 0.5
        self.velocity_y = 0

    def draw(self, screen):
         pygame.draw.line(screen, self.color, (self.up_x, self.up_y_start), (self.up_x, self.up_y_finish), self.size)
         pygame.draw.line(screen, self.color, (self.up_x, self.up_y_finish + self.margin),(self.up_x, CONFIG["graphics"]["height"]), self.size)

    def move(self, difficult):
        self.up_x -= (self.velocity_x * difficult)
