import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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
    # Create group related to shots
    shots = pygame.sprite.Group()

    # Set the containers for Player class
    Player.containers = (updatable, drawable)
    # Set the containers for Shot class
    Shot.containers = (shots, updatable, drawable)

    # Set the containers for Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)
    # Set the containers for Asteroidfields class
    AsteroidField.containers = updatable

    # Now create the player (it will automatically be added to both groups)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Initialize the asteroid field
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable objects
        updatable.update(dt)

        # Check for collisions between player and asteriods
        for asteroid in asteroids:
            if player.has_collided(asteroid):
                print("Game over!")
                sys.exit()

        # Check for collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.has_collided(shot):
                    asteroid.kill()
                    shot.kill()

        screen.fill("black")

        # Draw all drawable objects
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
