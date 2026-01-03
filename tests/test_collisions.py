import unittest

import pygame

from asteroid import Asteroid
from collisions import resolve_hits
from constants import ASTEROID_MIN_RADIUS
from shot import Shot


class ResolveHitsTest(unittest.TestCase):
    def setUp(self):
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        Asteroid.containers = (self.asteroids,)
        Shot.containers = (self.shots,)

    def tearDown(self):
        del Asteroid.containers
        del Shot.containers

    def test_a_hit_splits_the_asteroid_and_uses_up_the_shot(self):
        asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS * 2)
        asteroid.velocity = pygame.Vector2(50, 0)
        shot = Shot(100, 100)

        hit = resolve_hits(self.asteroids, self.shots)

        self.assertEqual(hit, [asteroid])
        self.assertFalse(shot.alive())
        self.assertEqual(len(self.asteroids), 2)

    def test_a_miss_changes_nothing(self):
        asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS)
        shot = Shot(500, 500)

        hit = resolve_hits(self.asteroids, self.shots)

        self.assertEqual(hit, [])
        self.assertTrue(asteroid.alive())
        self.assertTrue(shot.alive())

    def test_two_shots_on_one_asteroid_split_it_once(self):
        asteroid = Asteroid(100, 100, ASTEROID_MIN_RADIUS * 2)
        asteroid.velocity = pygame.Vector2(50, 0)
        Shot(100, 100)
        Shot(102, 100)

        hit = resolve_hits(self.asteroids, self.shots)

        self.assertEqual(len(hit), 1)
        self.assertEqual(len(self.asteroids), 2)
        self.assertEqual(len(self.shots), 1)

    def test_one_shot_cannot_destroy_two_asteroids(self):
        Asteroid(100, 100, ASTEROID_MIN_RADIUS)
        Asteroid(105, 100, ASTEROID_MIN_RADIUS)
        Shot(102, 100)

        hit = resolve_hits(self.asteroids, self.shots)

        self.assertEqual(len(hit), 1)
        self.assertEqual(len(self.asteroids), 1)
        self.assertEqual(len(self.shots), 0)


if __name__ == "__main__":
    unittest.main()
