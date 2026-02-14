import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, HUD_FONT_SIZE
from game import Game


def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, HUD_FONT_SIZE)
    dt = 0

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        game.update(dt)

        if game.over:
            print(f"Game over! Final score: {game.score}")
            sys.exit()

        game.draw(screen, font)
        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
