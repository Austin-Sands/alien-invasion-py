import sys

import pygame

from settings import Settings

from ship import Ship


class AlienInvasion:
    """Class to manage game assets and main loop"""

    def __init__(self):
        """initialize game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # set background color
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """start games main loop"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # catch user input at mouse and keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # redraw screen after each logic update
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        # display most recently drawn screen
        pygame.display.flip()


if __name__ == '__main__':
    # make game instance and run
    game = AlienInvasion()
    game.run_game()
