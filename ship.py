import pygame
from pygame.locals import *

class Ship():
    def __init__(self, game_settings, screen):
        
        self.screen = screen
        self.game_settings = game_settings
        
        self.image = pygame.transform.scale(pygame.image.load_basic('images/ship2.bmp').convert_alpha(), (70,70))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        
        if self.moving_right:
            self.rect.centerx += self.game_settings.ship_speed_factor
        
        if self.moving_left:
            self.rect.centerx -= self.game_settings.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)