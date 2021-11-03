import sys
import pygame

#controls ship movement 
def check_keydown_events(event, game_settings, player):
    if event.key == pygame.K_RIGHT:# right
        player.moving_right = True
        
    elif event.key == pygame.K_LEFT: # left
        player.moving_left = True
        
    elif event.key == pygame.K_UP: # up
        player.moving_up = True
            
    elif event.key == pygame.K_DOWN: # down
        player.moving_down = True
        
    elif event.key == pygame.K_SPACE:
        player.shoot()
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = False