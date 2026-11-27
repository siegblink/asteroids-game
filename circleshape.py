import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class CircleShape(pygame.sprite.Sprite):
    # Base class for game objects
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def has_collided(self, circle):
        distance = self.position.distance_to(circle.position)
        return distance < self.radius + circle.radius

    def is_off_screen(self, margin=0):
        # True once the centre is more than `margin` pixels past any edge
        return (
            self.position.x < -margin
            or self.position.x > SCREEN_WIDTH + margin
            or self.position.y < -margin
            or self.position.y > SCREEN_HEIGHT + margin
        )
