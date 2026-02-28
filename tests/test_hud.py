import unittest

import pygame

from constants import HUD_FONT_SIZE, HUD_MARGIN, SCREEN_HEIGHT, SCREEN_WIDTH
from hud import draw_game_over, draw_hud

LEFT_HALF = pygame.Rect(0, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT)
RIGHT_HALF = pygame.Rect(SCREEN_WIDTH // 2, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT)


class HudTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.font.init()
        cls.font = pygame.font.Font(None, HUD_FONT_SIZE)

    def drawn_area(self, half, score=0, lives=3):
        # On a transparent surface the bounding rect is exactly what was drawn
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        draw_hud(screen, self.font, score, lives)
        area = screen.subsurface(half).get_bounding_rect()
        return area.move(half.topleft)

    def test_score_is_drawn_in_the_top_left_corner(self):
        area = self.drawn_area(LEFT_HALF)

        self.assertGreater(area.width, 0)
        self.assertGreaterEqual(area.left, HUD_MARGIN)
        self.assertGreaterEqual(area.top, HUD_MARGIN)
        self.assertLess(area.bottom, SCREEN_HEIGHT / 4)

    def test_a_longer_score_takes_more_room(self):
        short = self.drawn_area(LEFT_HALF, score=0)
        long = self.drawn_area(LEFT_HALF, score=123456)

        self.assertGreater(long.width, short.width)

    def test_lives_are_drawn_in_the_top_right_corner(self):
        area = self.drawn_area(RIGHT_HALF)

        self.assertGreater(area.width, 0)
        self.assertLessEqual(area.right, SCREEN_WIDTH - HUD_MARGIN)
        self.assertGreaterEqual(area.top, HUD_MARGIN)
        self.assertLess(area.bottom, SCREEN_HEIGHT / 4)

    def test_game_over_message_is_centred(self):
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        draw_game_over(screen, self.font, 1250)
        area = screen.get_bounding_rect()

        self.assertGreater(area.width, 0)
        self.assertAlmostEqual(area.centerx, SCREEN_WIDTH / 2, delta=2)
        # Glyphs do not fill their line box, so the ink sits a little off centre
        slack = self.font.get_linesize() / 2
        self.assertAlmostEqual(area.centery, SCREEN_HEIGHT / 2, delta=slack)


if __name__ == "__main__":
    unittest.main()
