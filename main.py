import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, HUD_FONT_SIZE, PLAYER_LIVES
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from collisions import resolve_hits
from hud import draw_hud
from shot import Shot


def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, HUD_FONT_SIZE)
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

    score = 0
    lives = PLAYER_LIVES

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable objects
        updatable.update(dt)

        # Hitting an asteroid costs a life, and the last life ends the game
        if not player.invulnerable:
            for asteroid in asteroids:
                if player.has_collided(asteroid):
                    lives -= 1
                    if lives == 0:
                        print(f"Game over! Final score: {score}")
                        sys.exit()

                    player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    break

        # Split the asteroids that were hit by a shot and score them
        for asteroid in resolve_hits(asteroids, shots):
            score += asteroid.score_value()

        screen.fill("black")

        # Draw all drawable objects
        for sprite in drawable:
            sprite.draw(screen)

        draw_hud(screen, font, score, lives)

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
