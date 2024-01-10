import pygame


class Ship:
    """Class to manage player space ship"""

    def __init__(self, game):
        """initialize ship and set starting position"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # load image of ship and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # set starting position of ship to bottom center
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)
