from constants import HUD_MARGIN


def draw_hud(screen, font, score, lives):
    # The score sits in the top left corner, the lives in the top right
    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (HUD_MARGIN, HUD_MARGIN))

    lives_text = font.render(f"Lives: {lives}", True, "white")
    lives_x = screen.get_width() - lives_text.get_width() - HUD_MARGIN
    screen.blit(lives_text, (lives_x, HUD_MARGIN))
