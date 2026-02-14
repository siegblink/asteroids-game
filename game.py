import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from collisions import resolve_hits
from constants import PLAYER_LIVES, SCREEN_HEIGHT, SCREEN_WIDTH
from hud import draw_hud
from player import Player
from shot import Shot


class Game:
    # One round of the game: the sprites, the score and the lives

    def __init__(self):
        self.reset()

    def reset(self):
        # Fresh groups, so nothing from an earlier round is left behind
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        Player.containers = (self.updatable, self.drawable)
        Shot.containers = (self.shots, self.updatable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = self.updatable

        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.field = AsteroidField()
        self.score = 0
        self.lives = PLAYER_LIVES
        self.over = False

    def update(self, dt):
        if self.over:
            return

        self.updatable.update(dt)
        self.check_player_hit()

        # Split the asteroids that were hit by a shot and score them
        for asteroid in resolve_hits(self.asteroids, self.shots):
            self.score += asteroid.score_value()

    def check_player_hit(self):
        # Hitting an asteroid costs a life, and the last life ends the game
        if self.player.invulnerable:
            return

        for asteroid in self.asteroids:
            if self.player.has_collided(asteroid):
                self.lives -= 1
                if self.lives == 0:
                    self.over = True
                else:
                    self.player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                return

    def draw(self, screen, font):
        screen.fill("black")

        for sprite in self.drawable:
            sprite.draw(screen)

        draw_hud(screen, font, self.score, self.lives)
