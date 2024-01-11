import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, game):
        """initialize the alien and set starting position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # load the image for alien and intialize rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start position near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store horizontal postion
        self.x = float(self.rect.x)

    def update(self):
        """move alien horizontally"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """returns true if alien has reached the end of the screen"""
        screen_rect = self.screen.get_rect()
        return ((self.rect.right >= screen_rect.right)
                or (self.rect.left <= 0))

    def check_bottom(self):
        """returns true if alien has reached bottom of screen"""
        return self.rect.bottom >= self.settings.screen_height
