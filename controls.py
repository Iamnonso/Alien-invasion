import pygame
from bullet import Bullet
#controls ship movement 
def check_keydown_events(event, game_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Create a new bullet and add it to the bullets Group
        if len(bullets) < game_settings.bullet_allowed:
            new_bullet = Bullet(game_settings,screen,ship)
            bullets.add(new_bullet)
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False