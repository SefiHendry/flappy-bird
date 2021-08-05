import os.path
from typing import Union
import sys
import pygame
from pygame.surface import SurfaceType
import env
from env import CONFIG

# sys.path.insert(1,"src/entities")
# import Player
import src.entities.Player as p
import src.entities.Obstacle as o

fpsClock = pygame.time.Clock()


# def draw()


def gameloop(screen: Union[pygame.Surface, SurfaceType], score):
    font = pygame.font.Font(os.path.join("fonts", "GOUDYSTO.TTF"), 32)
    running = True
    player = p.Player(x=200, y=200, size=30, color=(255, 51, 51))
    obstacle1 = o.Obstacle()
    difficult = 10

    # screen.fill((255, 255, 255))
    while running:

        text = font.render("Your Score: " + str(player.score), True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (CONFIG["graphics"]["width"] - 270, 30)
        keys = pygame.key.get_pressed()
        player.move(keys)
        screen.fill((128, 255, 255))
        player.draw(screen)
        obstacle1.draw(screen)
        screen.blit(text, text_rect)
        obstacle1.move(difficult)
        running = not player.collision(obstacle1)

        if obstacle1.up_x <= -30:
            obstacle1 = o.Obstacle()
            difficult *= 1.05
            player.score += 1
            score = player.score
            # player.size *= 1.1
        fpsClock.tick((CONFIG["graphics"]["FPS"]))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False
    print("your score is: ", score)


def main():
    score = 0
    pygame.init()
    screen = pygame.display.set_mode((CONFIG["graphics"]["width"], CONFIG["graphics"]["height"]))
    gameloop(screen, score)

    pygame.quit()


if __name__ == "__main__":
    main()

