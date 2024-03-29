class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, game):
        """initialize stats"""
        self.settings = game.settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change during gameplay"""
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1
