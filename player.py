import pygame
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_RESPAWN_INVULNERABILITY,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.invulnerable_timer = 0

    @property
    def invulnerable(self):
        return self.invulnerable_timer > 0

    def respawn(self, x, y):
        # Back to the start, with a moment of safety to get clear
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.shoot_timer = 0
        self.invulnerable_timer = PLAYER_RESPAWN_INVULNERABILITY

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90)
            * self.radius / 1.5
        )
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Blink while invulnerable
        if self.invulnerable and int(self.invulnerable_timer * 10) % 2 == 0:
            return

        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.wrap()
        self.tick(dt)

    def tick(self, dt):
        # Count the timers down
        self.shoot_timer -= dt
        self.invulnerable_timer = max(0, self.invulnerable_timer - dt)

    def wrap(self):
        # Leaving one edge brings the ship back in on the opposite one
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        )

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
