import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.settings = ai_settings    # converting to the attribute for use in functions of class

        self.image = pygame.image.load('images/starship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)      # better change control for ship speed parameter

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:     # this implementation allows you to set equal priority
            self.rect.centerx -= self.settings.ship_speed_factor

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
