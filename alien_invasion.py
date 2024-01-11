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

        # fullscreen toggle initialized as false
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # create ship and initialize
        self.ship = Ship(self)

        # set background color
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """start games main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """catch user input at mouse and keyboard"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event.key)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event.key)

    def _check_keydown_events(self, key):
        """respond to key presses"""
        if key == pygame.K_d:
            # move ship to right
            self.ship.moving_right = True
        if key == pygame.K_RIGHT:
            self.ship.moving_right_alt = True
        if key == pygame.K_a:
            # move ship to left
            self.ship.moving_left = True
        if key == pygame.K_LEFT:
            self.ship.moving_left_alt = True
        if key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, key):
        """respond to key releases"""
        if key == pygame.K_d:
            # stop moving ship right
            self.ship.moving_right = False
        if key == pygame.K_RIGHT:
            self.ship.moving_right_alt = False
        if key == pygame.K_a:
            # stop moving ship right
            self.ship.moving_left = False
        if key == pygame.K_LEFT:
            self.ship.moving_left_alt = False

    def _update_screen(self):
        """redraw screen after each logic update"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        # display most recently drawn screen
        pygame.display.flip()


if __name__ == '__main__':
    # make game instance and run
    game = AlienInvasion()
    game.run_game()
