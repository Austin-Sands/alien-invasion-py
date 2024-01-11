import sys
from time import sleep

import pygame

from settings import Settings

from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from alien import Alien


class AlienInvasion:
    """Class to manage game assets and main loop"""

    def __init__(self):
        """initialize game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.game_active = True

        # fullscreen toggle initialized as false
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # create storage for game stats
        self.stats = GameStats(self)

        # create ship and initialize
        self.ship = Ship(self)

        # create bullets group and initialize
        self.bullets = pygame.sprite.Group()

        # create aliens group and initialize
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet()

        # set background color
        self.bg_color = (self.settings.bg_color)

    def _create_alien_fleet(self):
        """creates the enemy alien fleet"""
        # create instance of alien and repeat until no space left
        # spacing is one instance width and height
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # new row; reset x value for next row and increment y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """create a new alien at x_position, y_position and add to group"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def run_game(self):
        """start games main loop"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
        if key == pygame.K_SPACE:
            # fire bullet
            self._fire_bullet()
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

    def _fire_bullet(self):
        """create a new bullet and add to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _cleanup_bullets(self):
        """destroy bullets that have reached the end of the screen"""
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_bullets(self):
        """cleanup bullets that have reached the end of the screen 
        and update the rest"""
        self._cleanup_bullets()
        self.bullets.update()

        self._detect_bullet_collisions()

    def _update_aliens(self):
        """check if fleet exists or is at edges and move aliens"""
        self._check_fleet_exists()
        self._check_fleet_edges()
        self._check_fleet_bottom()
        self.aliens.update()

        self._detect_ship_collisions()

    def _check_fleet_edges(self):
        """checks if alien fleet has hit edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_fleet_bottom(self):
        """check if alien fleet has reached bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_bottom():
                # treat as if alien and ship collided
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """drops fleet down and changes direction of movement"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_exists(self):
        """if no more aliens; destroy bullets,
        increment alien speed and create new fleet"""
        if not self.aliens:
            self.bullets.empty()
            self.settings.alien_speed += 0.25
            self._create_alien_fleet()

    def _detect_bullet_collisions(self):
        """check for bullet collisions and destroy both if so"""
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _detect_ship_collisions(self):
        """check for alien and player ship collisions"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """reset game and decrement ships left when ship and alien collide. 
        Game over if no ships left"""
        if self.stats.ships_left > 0:
            # decrement ships left
            self.stats.ships_left -= 1

            # clear game
            self.bullets.empty()
            self.aliens.empty()

            # reset fleet and player ship
            self._create_alien_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            # game over
            self.game_active = False

    def _update_screen(self):
        """redraw screen after each logic update"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # display most recently drawn screen
        pygame.display.flip()


if __name__ == '__main__':
    # make game instance and run
    game = AlienInvasion()
    game.run_game()
