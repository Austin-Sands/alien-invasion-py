import pygame

from settings import Settings


class Ship:
    """Class to manage player space ship"""

    def __init__(self, game):
        """initialize ship and set starting position"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        # load image of ship and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # set starting position of ship to bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # store ships exact position
        self.x = float(self.rect.x)

        # initialize movement flag to false
        self.moving_right = False
        self.moving_right_alt = False
        self.moving_left = False
        self.moving_left_alt = False

    def update(self):
        """update position of ship based on movement flag"""
        # update x not rect. Do not update if at edge of screen
        if ((self.moving_right or self.moving_right_alt)
                and self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if ((self.moving_left or self.moving_left_alt)
                and self.rect.left > 0):
            self.x -= self.settings.ship_speed

        # update rect based on new position
        self.rect.x = self.x

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)
