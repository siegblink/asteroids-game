import unittest

import pygame

from asteroid import Asteroid
from circleshape import CircleShape
from constants import (
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from player import Player
from shot import Shot


class CollisionTest(unittest.TestCase):
    def test_overlapping_circles_collide(self):
        a = CircleShape(100, 100, 20)
        b = CircleShape(130, 100, 20)
        self.assertTrue(a.has_collided(b))
        self.assertTrue(b.has_collided(a))

    def test_distant_circles_do_not_collide(self):
        a = CircleShape(100, 100, 20)
        b = CircleShape(200, 100, 20)
        self.assertFalse(a.has_collided(b))

    def test_circles_that_only_touch_do_not_collide(self):
        a = CircleShape(100, 100, 20)
        b = CircleShape(140, 100, 20)
        self.assertFalse(a.has_collided(b))


class AsteroidSplitTest(unittest.TestCase):
    def setUp(self):
        self.asteroids = pygame.sprite.Group()
        Asteroid.containers = (self.asteroids,)

    def tearDown(self):
        del Asteroid.containers

    def test_smallest_asteroid_disappears(self):
        asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS)
        asteroid.split()
        self.assertEqual(len(self.asteroids), 0)

    def test_larger_asteroid_splits_in_two(self):
        asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS * 3)
        asteroid.velocity = pygame.Vector2(50, 0)
        asteroid.split()

        self.assertFalse(asteroid.alive())
        pieces = self.asteroids.sprites()
        self.assertEqual(len(pieces), 2)
        for piece in pieces:
            self.assertEqual(piece.radius, ASTEROID_MIN_RADIUS * 2)
            self.assertEqual(piece.position, pygame.Vector2(100, 100))
            self.assertAlmostEqual(piece.velocity.length(), 60)

    def test_pieces_fly_apart(self):
        asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS * 2)
        asteroid.velocity = pygame.Vector2(50, 0)
        asteroid.split()

        first, second = self.asteroids.sprites()
        angle = abs(first.velocity.angle_to(second.velocity))
        self.assertGreaterEqual(angle, 40)
        self.assertLessEqual(angle, 100)


class OffScreenTest(unittest.TestCase):
    def setUp(self):
        self.group = pygame.sprite.Group()

    def test_shot_is_removed_after_leaving_the_screen(self):
        shot = Shot(SCREEN_WIDTH - 1, 100)
        shot.velocity = pygame.Vector2(500, 0)
        self.group.add(shot)

        shot.update(0.001)
        self.assertTrue(shot.alive())
        shot.update(1)
        self.assertFalse(shot.alive())

    def test_new_asteroid_survives_outside_the_screen(self):
        asteroid = Asteroid(-ASTEROID_MAX_RADIUS, 100, ASTEROID_MAX_RADIUS)
        asteroid.velocity = pygame.Vector2(50, 0)
        self.group.add(asteroid)

        asteroid.update(0.016)
        self.assertTrue(asteroid.alive())

    def test_asteroid_is_removed_once_far_outside(self):
        asteroid = Asteroid(SCREEN_WIDTH + ASTEROID_MAX_RADIUS * 2, 100, 20)
        asteroid.velocity = pygame.Vector2(100, 0)
        self.group.add(asteroid)

        asteroid.update(0.016)
        self.assertFalse(asteroid.alive())


class PlayerWrapTest(unittest.TestCase):
    def test_player_reappears_on_the_opposite_edge(self):
        player = Player(SCREEN_WIDTH + 15, -10)
        player.wrap()
        self.assertAlmostEqual(player.position.x, 15)
        self.assertAlmostEqual(player.position.y, SCREEN_HEIGHT - 10)

    def test_player_inside_the_screen_stays_put(self):
        player = Player(300, 200)
        player.wrap()
        self.assertEqual(player.position, pygame.Vector2(300, 200))


if __name__ == "__main__":
    unittest.main()
