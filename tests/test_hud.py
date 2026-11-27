import unittest

import pygame

from constants import HUD_FONT_SIZE, HUD_MARGIN, SCREEN_HEIGHT, SCREEN_WIDTH
from hud import draw_game_over, draw_hud, draw_paused

THIRD = SCREEN_WIDTH // 3
LEFT = pygame.Rect(0, 0, THIRD, SCREEN_HEIGHT)
MIDDLE = pygame.Rect(THIRD, 0, THIRD, SCREEN_HEIGHT)
RIGHT = pygame.Rect(THIRD * 2, 0, SCREEN_WIDTH - THIRD * 2, SCREEN_HEIGHT)


class HudTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.font.init()
        cls.font = pygame.font.Font(None, HUD_FONT_SIZE)

    def drawn_area(self, part, score=0, lives=3, high_score=0):
        # On a transparent surface the bounding rect is exactly what was drawn
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        draw_hud(screen, self.font, score, lives, high_score)
        area = screen.subsurface(part).get_bounding_rect()
        return area.move(part.topleft)

    def test_score_is_drawn_in_the_top_left_corner(self):
        area = self.drawn_area(LEFT)

        self.assertGreater(area.width, 0)
        self.assertGreaterEqual(area.left, HUD_MARGIN)
        self.assertGreaterEqual(area.top, HUD_MARGIN)
        self.assertLess(area.bottom, SCREEN_HEIGHT / 4)

    def test_a_longer_score_takes_more_room(self):
        short = self.drawn_area(LEFT, score=0)
        long = self.drawn_area(LEFT, score=123456)

        self.assertGreater(long.width, short.width)

    def test_lives_are_drawn_in_the_top_right_corner(self):
        area = self.drawn_area(RIGHT)

        self.assertGreater(area.width, 0)
        self.assertLessEqual(area.right, SCREEN_WIDTH - HUD_MARGIN)
        self.assertGreaterEqual(area.top, HUD_MARGIN)
        self.assertLess(area.bottom, SCREEN_HEIGHT / 4)

    def test_high_score_is_drawn_in_the_top_middle(self):
        area = self.drawn_area(MIDDLE, high_score=4200)

        self.assertGreater(area.width, 0)
        self.assertAlmostEqual(area.centerx, SCREEN_WIDTH / 2, delta=2)
        self.assertGreaterEqual(area.top, HUD_MARGIN)

    def test_a_new_high_score_adds_a_line_to_the_game_over_screen(self):
        def drawn_height(new_high_score):
            screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            draw_game_over(screen, self.font, 1250, new_high_score)
            return screen.get_bounding_rect().height

        self.assertGreater(drawn_height(True), drawn_height(False))

    def test_game_over_message_is_centred(self):
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        draw_game_over(screen, self.font, 1250, False)
        area = screen.get_bounding_rect()

        self.assertGreater(area.width, 0)
        self.assertAlmostEqual(area.centerx, SCREEN_WIDTH / 2, delta=2)
        # Glyphs do not fill their line box, so the ink sits a little off centre
        slack = self.font.get_linesize() / 2
        self.assertAlmostEqual(area.centery, SCREEN_HEIGHT / 2, delta=slack)

    def test_pause_message_is_centred(self):
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        draw_paused(screen, self.font)
        area = screen.get_bounding_rect()

        self.assertGreater(area.width, 0)
        self.assertAlmostEqual(area.centerx, SCREEN_WIDTH / 2, delta=2)


if __name__ == "__main__":
    unittest.main()
