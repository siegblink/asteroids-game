from pathlib import Path

# Kept next to the game and ignored by git
HIGH_SCORE_FILE = Path(__file__).with_name(".highscore")


def load_high_score(path=HIGH_SCORE_FILE):
    # A missing or damaged file just means there is no high score yet
    try:
        return int(path.read_text().strip())
    except (OSError, ValueError):
        return 0


def save_high_score(score, path=HIGH_SCORE_FILE):
    path.write_text(f"{score}\n")
