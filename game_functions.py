import sys
import pygame
import controls as control
import  load_images
from pygame.locals import *

def check_events(game_settings, screen, ship, bullets):
    """Respond to keypres and mouse events"""
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            control.check_keydown_events(event, game_settings,screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            control.check_keyup_events(event, ship)
            
def update_screen(game_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    screen.blit(load_images.BG_1,(0,0))
    #screen.fill(game_settings.bg_color)
    
    #draw text
    lives_label = game_settings.main_font.render(f"Lives: {game_settings.startLives}", 1, (255,255,255))
    level_label = game_settings.main_font.render(f"Level: {game_settings.startLevel}", 1, (255,255,255))
    level_height = level_label.get_width()
    screen.blit(lives_label, (10,10))
    screen.blit(level_label, (game_settings.screen_width - level_height - 10, 10))
    
    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #Redraw the screen during each pass through the loop
    ship.blitme()
    
    #Make the most recently draw screen visible
    pygame.display.flip()
    
def update_bullets(bullets):
    """Update the position of the bullets and get rid of old bullets"""
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

