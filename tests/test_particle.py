import unittest

import pygame

from constants import (
    PARTICLE_COUNT,
    PARTICLE_LIFETIME,
    PARTICLE_MAX_SPEED,
    PARTICLE_MIN_SPEED,
)
from particle import Particle, burst


class ParticleTest(unittest.TestCase):
    def setUp(self):
        self.particles = pygame.sprite.Group()
        Particle.containers = (self.particles,)

    def tearDown(self):
        del Particle.containers

    def test_a_particle_moves_and_then_disappears(self):
        particle = Particle(100, 100)
        particle.velocity = pygame.Vector2(100, 0)

        particle.update(PARTICLE_LIFETIME / 2)
        self.assertTrue(particle.alive())
        self.assertGreater(particle.position.x, 100)

        particle.update(PARTICLE_LIFETIME / 2)
        self.assertFalse(particle.alive())

    def test_a_burst_scatters_particles_from_one_point(self):
        burst(300, 200)

        self.assertEqual(len(self.particles), PARTICLE_COUNT)
        for particle in self.particles:
            self.assertEqual(particle.position, pygame.Vector2(300, 200))
            speed = particle.velocity.length()
            self.assertGreaterEqual(speed, PARTICLE_MIN_SPEED - 0.001)
            self.assertLessEqual(speed, PARTICLE_MAX_SPEED + 0.001)


if __name__ == "__main__":
    unittest.main()
