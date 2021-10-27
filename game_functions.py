import sys
import pygame
import controls as control
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
    
    screen.fill(game_settings.bg_color)
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
        
    
