from constants import HUD_MARGIN


def draw_hud(screen, font, score):
    # The score sits in the top left corner
    text = font.render(f"Score: {score}", True, "white")
    screen.blit(text, (HUD_MARGIN, HUD_MARGIN))
