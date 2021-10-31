import pygame
from pygame.locals import *
import load_images
from pygame.sprite import Sprite

class Ship():
    def __init__(self, game_settings, screen):
        
        self.screen = screen
        self.game_settings = game_settings
        
        self.image = pygame.transform.scale(load_images.WAR_SHIP2, (70,70))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_bottom = False
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.game_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.game_settings.ship_speed_factor
        
        if self.moving_up and self.rect.centery - 0.5 > 0:
            self.rect.centery -= 0.5
            
        if self.moving_bottom and self.rect.centery + 0.5 + 40 < self.game_settings.screen_height:
            self.rect.centery += self.game_settings.ship_speed_factor
             
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

#alien ship class
class alien:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.laser = []
        self.cool_down_counter = 0
        