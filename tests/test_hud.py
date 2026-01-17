import unittest

import pygame

from constants import HUD_FONT_SIZE, HUD_MARGIN, SCREEN_HEIGHT, SCREEN_WIDTH
from hud import draw_hud


class HudTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.font.init()
        cls.font = pygame.font.Font(None, HUD_FONT_SIZE)

    def drawn_area(self, score):
        # On a transparent surface the bounding rect is exactly what was drawn
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        draw_hud(screen, self.font, score)
        return screen.get_bounding_rect()

    def test_score_is_drawn_in_the_top_left_corner(self):
        area = self.drawn_area(0)

        self.assertGreater(area.width, 0)
        self.assertGreaterEqual(area.left, HUD_MARGIN)
        self.assertGreaterEqual(area.top, HUD_MARGIN)
        self.assertLess(area.right, SCREEN_WIDTH / 2)
        self.assertLess(area.bottom, SCREEN_HEIGHT / 4)

    def test_a_longer_score_takes_more_room(self):
        self.assertGreater(self.drawn_area(123456).width, self.drawn_area(0).width)


if __name__ == "__main__":
    unittest.main()
