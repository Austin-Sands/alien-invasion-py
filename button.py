import pygame.font


class Button:
    """A class to build buttons for a game"""

    def __init__(self, game, msg):
        """Initialize button attributes"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # set button dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build rect object for button and center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # only need to prep message once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into rendered image to display on button"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message image"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
