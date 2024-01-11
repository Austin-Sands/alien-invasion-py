from typing import Any
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage player fired bullets"""

    def __init__(self, game):
        """Create a bullet object at ships current position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.bullet_speed = self.settings.bullet_speed

        # create rect for bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)

        # set to correct position and store as a float
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet vertically on the screen"""
        # update position of bullet
        self.y -= self.bullet_speed
        # update rect to position of bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """draws bullet onto the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
