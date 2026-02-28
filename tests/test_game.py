import unittest

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    ASTEROID_MIN_RADIUS,
    PLAYER_LIVES,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from game import Game
from player import Player
from shot import Shot

CENTRE = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


class GameTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The player reads the keyboard, which needs the video system
        pygame.display.init()

    @classmethod
    def tearDownClass(cls):
        pygame.display.quit()

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        # Leave the sprite classes as the other tests expect to find them
        for sprite_class in (Player, Shot, Asteroid, AsteroidField):
            del sprite_class.containers

    def test_a_new_game_starts_clean(self):
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.lives, PLAYER_LIVES)
        self.assertFalse(self.game.over)
        self.assertEqual(self.game.player.position, CENTRE)
        self.assertEqual(len(self.game.asteroids), 0)

    def test_destroying_an_asteroid_scores_it(self):
        Asteroid(100, 100, ASTEROID_MIN_RADIUS)
        Shot(100, 100)

        self.game.update(0)

        self.assertEqual(self.game.score, 100)
        self.assertEqual(len(self.game.asteroids), 0)

    def test_hitting_an_asteroid_costs_a_life(self):
        self.game.player.position = pygame.Vector2(200, 200)
        Asteroid(200, 200, ASTEROID_MIN_RADIUS)

        self.game.update(0)

        self.assertEqual(self.game.lives, PLAYER_LIVES - 1)
        self.assertFalse(self.game.over)
        self.assertEqual(self.game.player.position, CENTRE)
        self.assertTrue(self.game.player.invulnerable)

    def test_a_protected_player_is_not_hit(self):
        self.game.player.respawn(CENTRE.x, CENTRE.y)
        Asteroid(CENTRE.x, CENTRE.y, ASTEROID_MIN_RADIUS)

        self.game.update(0)

        self.assertEqual(self.game.lives, PLAYER_LIVES)

    def test_losing_the_last_life_ends_the_game(self):
        self.game.lives = 1
        Asteroid(CENTRE.x, CENTRE.y, ASTEROID_MIN_RADIUS)

        self.game.update(0)

        self.assertEqual(self.game.lives, 0)
        self.assertTrue(self.game.over)

    def test_nothing_moves_once_the_game_is_over(self):
        asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS)
        asteroid.velocity = pygame.Vector2(50, 0)
        self.game.over = True

        self.game.update(1)

        self.assertEqual(asteroid.position, pygame.Vector2(100, 100))

    def press(self, key):
        self.game.handle_event(pygame.event.Event(pygame.KEYDOWN, key=key))

    def test_r_restarts_after_game_over(self):
        self.game.score = 500
        self.game.lives = 0
        self.game.over = True

        self.press(pygame.K_r)

        self.assertFalse(self.game.over)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.lives, PLAYER_LIVES)

    def test_r_does_nothing_during_a_round(self):
        self.game.score = 500

        self.press(pygame.K_r)

        self.assertEqual(self.game.score, 500)

    def test_reset_starts_a_new_round(self):
        Asteroid(100, 100, ASTEROID_MIN_RADIUS)
        self.game.score = 500
        self.game.lives = 0
        self.game.over = True

        self.game.reset()

        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.lives, PLAYER_LIVES)
        self.assertFalse(self.game.over)
        self.assertEqual(len(self.game.asteroids), 0)


if __name__ == "__main__":
    unittest.main()
