from constants import HUD_MARGIN


def draw_hud(screen, font, score, lives, high_score):
    # The score sits in the top left corner, the lives in the top right and
    # the high score between them
    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (HUD_MARGIN, HUD_MARGIN))

    lives_text = font.render(f"Lives: {lives}", True, "white")
    lives_x = screen.get_width() - lives_text.get_width() - HUD_MARGIN
    screen.blit(lives_text, (lives_x, HUD_MARGIN))

    best_text = font.render(f"Best: {high_score}", True, "white")
    best_x = (screen.get_width() - best_text.get_width()) / 2
    screen.blit(best_text, (best_x, HUD_MARGIN))


def draw_game_over(screen, font, score, new_high_score):
    lines = ["GAME OVER", f"Final score: {score}"]
    if new_high_score:
        lines.append("New high score!")
    lines.append("Press R to play again")
    draw_centred(screen, font, lines)


def draw_paused(screen, font):
    draw_centred(screen, font, ["PAUSED", "Press P to continue"])


def draw_centred(screen, font, lines):
    # A block of centred lines over the frozen game
    line_height = font.get_linesize()
    top = (screen.get_height() - line_height * len(lines)) / 2

    for index, line in enumerate(lines):
        text = font.render(line, True, "white")
        x = (screen.get_width() - text.get_width()) / 2
        screen.blit(text, (x, top + index * line_height))
