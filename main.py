import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable,updatable,asteroid)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        for item in asteroid:
            if item.collision(player) == True:
                print("Game over!")
                exit()
        pygame.display.flip()


        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()