import random
import pygame
from circleshape import CircleShape
from constants import (
    PARTICLE_COUNT,
    PARTICLE_LIFETIME,
    PARTICLE_MAX_SPEED,
    PARTICLE_MIN_SPEED,
    PARTICLE_RADIUS,
)


class Particle(CircleShape):
    # A speck of debris that flies off and disappears
    def __init__(self, x, y):
        super().__init__(x, y, PARTICLE_RADIUS)
        self.lifetime = PARTICLE_LIFETIME

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()


def burst(x, y):
    # Scatter particles in every direction from one point
    for _ in range(PARTICLE_COUNT):
        direction = pygame.Vector2(0, 1).rotate(random.uniform(0, 360))
        speed = random.uniform(PARTICLE_MIN_SPEED, PARTICLE_MAX_SPEED)

        particle = Particle(x, y)
        particle.velocity = direction * speed
