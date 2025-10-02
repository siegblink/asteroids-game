# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create common groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Create group related to asteroids
    asteroids = pygame.sprite.Group()

    # Set the containers for Player class
    Player.containers = (updatable, drawable)

    # Set the containers for Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)
    # Set the containers for Asteroidfields class
    AsteroidField.containers = updatable

    # Now create the player (it will automatically be added to both groups)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Initialize the asteroid field
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable objects
        updatable.update(dt)

        screen.fill("black")

        # Draw all drawable objects
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
