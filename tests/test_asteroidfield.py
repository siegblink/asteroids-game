import unittest

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MIN_SPAWN_RATE,
    ASTEROID_SPAWN_RAMP,
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

    def test_a_round_starts_at_the_base_spawn_rate(self):
        self.assertEqual(self.field.spawn_rate(), ASTEROID_SPAWN_RATE)

    def test_asteroids_arrive_faster_as_the_round_goes_on(self):
        self.field.elapsed = 20

        expected = ASTEROID_SPAWN_RATE - 20 * ASTEROID_SPAWN_RAMP
        self.assertAlmostEqual(self.field.spawn_rate(), expected)
        self.assertLess(self.field.spawn_rate(), ASTEROID_SPAWN_RATE)

    def test_the_spawn_rate_never_drops_below_the_floor(self):
        self.field.elapsed = 10_000

        self.assertEqual(self.field.spawn_rate(), ASTEROID_MIN_SPAWN_RATE)

    def test_a_late_round_spawns_more_asteroids_in_the_same_time(self):
        def spawned_in_ten_seconds(elapsed):
            self.asteroids.empty()
            self.field.elapsed = elapsed
            self.field.spawn_timer = 0
            for _ in range(600):
                self.field.update(1 / 60)
            return len(self.asteroids)

        self.assertGreater(spawned_in_ten_seconds(200), spawned_in_ten_seconds(0))


if __name__ == "__main__":
    unittest.main()
