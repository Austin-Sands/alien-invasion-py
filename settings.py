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
        self.ships_limit = 3

        # settings for bullets
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # direction of 1 represents right movement, -1 left
        self.fleet_direction = 1
