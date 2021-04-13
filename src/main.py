from typing import Union
import sys
import pygame
from pygame.surface import SurfaceType
import env
from env import CONFIG

# sys.path.insert(1,"src/entities")
# import Player
import src.entities.Player as p
fpsClock = pygame.time.Clock()

def gameloop(screen: Union[pygame.Surface, SurfaceType]):
    running = True
    player = p.Player(x=200, y=200, size=30, color=(50, 40, 30), speed=0.3)
    # screen.fill((255, 255, 255))
    while running:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        player.move(keys)
        screen.fill((255, 255, 255))
        player.draw(screen)
        fpsClock.tick((CONFIG["graphics"]["FPS"]))
        pygame.display.flip()



def main():
    pygame.init()
    screen = pygame.display.set_mode((CONFIG["graphics"]["width"], CONFIG["graphics"]["height"]))
    gameloop(screen)

    pygame.quit()


if __name__ == "__main__":
    main()
