import unittest

import pygame

from constants import (
    PLAYER_RESPAWN_INVULNERABILITY,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
)
from player import Player
from shot import Shot


class RespawnTest(unittest.TestCase):
    def test_new_player_can_be_hit(self):
        self.assertFalse(Player(100, 100).invulnerable)

    def test_respawn_puts_the_player_back_and_protects_it(self):
        player = Player(100, 100)
        player.rotation = 135

        player.respawn(640, 360)

        self.assertEqual(player.position, pygame.Vector2(640, 360))
        self.assertEqual(player.rotation, 0)
        self.assertTrue(player.invulnerable)

    def test_protection_wears_off(self):
        player = Player(100, 100)
        player.respawn(640, 360)

        player.tick(PLAYER_RESPAWN_INVULNERABILITY / 2)
        self.assertTrue(player.invulnerable)
        player.tick(PLAYER_RESPAWN_INVULNERABILITY / 2)
        self.assertFalse(player.invulnerable)


class ShootTest(unittest.TestCase):
    def setUp(self):
        self.shots = pygame.sprite.Group()
        Shot.containers = (self.shots,)

    def tearDown(self):
        del Shot.containers

    def test_shot_leaves_from_the_ship_in_the_direction_it_faces(self):
        player = Player(100, 100)
        player.rotation = 90

        player.shoot()

        (shot,) = self.shots.sprites()
        self.assertEqual(shot.position, pygame.Vector2(100, 100))
        self.assertAlmostEqual(shot.velocity.x, -PLAYER_SHOOT_SPEED)
        self.assertAlmostEqual(shot.velocity.y, 0)

    def test_cooldown_blocks_a_second_shot(self):
        player = Player(100, 100)

        player.shoot()
        player.shoot()
        self.assertEqual(len(self.shots), 1)

        player.tick(PLAYER_SHOOT_COOLDOWN)
        player.shoot()
        self.assertEqual(len(self.shots), 2)


if __name__ == "__main__":
    unittest.main()
