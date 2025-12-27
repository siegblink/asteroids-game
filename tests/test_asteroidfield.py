import unittest

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class AsteroidFieldTest(unittest.TestCase):
    def setUp(self):
        self.asteroids = pygame.sprite.Group()
        self.updatable = pygame.sprite.Group()
        Asteroid.containers = (self.asteroids,)
        AsteroidField.containers = (self.updatable,)
        self.field = AsteroidField()

    def tearDown(self):
        del Asteroid.containers
        del AsteroidField.containers

    def test_nothing_spawns_before_the_spawn_rate_has_passed(self):
        self.field.update(ASTEROID_SPAWN_RATE / 2)
        self.assertEqual(len(self.asteroids), 0)

    def test_one_asteroid_spawns_after_the_spawn_rate(self):
        self.field.update(ASTEROID_SPAWN_RATE + 0.01)
        self.assertEqual(len(self.asteroids), 1)

    def test_asteroids_spawn_just_outside_the_screen(self):
        for _ in range(50):
            self.field.update(ASTEROID_SPAWN_RATE + 0.01)

        for asteroid in self.asteroids:
            x, y = asteroid.position
            outside = (
                x == -ASTEROID_MAX_RADIUS
                or x == SCREEN_WIDTH + ASTEROID_MAX_RADIUS
                or y == -ASTEROID_MAX_RADIUS
                or y == SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            )
            self.assertTrue(outside, f"spawned on screen at {asteroid.position}")

    def test_asteroids_come_in_the_configured_sizes(self):
        for _ in range(50):
            self.field.update(ASTEROID_SPAWN_RATE + 0.01)

        sizes = {ASTEROID_MIN_RADIUS * kind for kind in range(1, ASTEROID_KINDS + 1)}
        for asteroid in self.asteroids:
            self.assertIn(asteroid.radius, sizes)

    def test_asteroids_head_towards_the_screen(self):
        for _ in range(50):
            self.field.update(ASTEROID_SPAWN_RATE + 0.01)

        centre = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        for asteroid in self.asteroids:
            before = asteroid.position.distance_to(centre)
            after = (asteroid.position + asteroid.velocity * 0.1).distance_to(centre)
            self.assertLess(after, before)


if __name__ == "__main__":
    unittest.main()
