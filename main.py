import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, HUD_FONT_SIZE
from game import Game


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, HUD_FONT_SIZE)
    dt = 0

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            game.handle_event(event)

        game.update(dt)
        game.draw(screen, font)
        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
