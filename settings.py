class Settings:
    """This class will store all settings for Alien Invasion game"""

    def __init__(self):
        """initialize default settings"""
        # Display settings
        self.screen_width = 1_200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # player ships settings
        self.ship_speed = 1.5
