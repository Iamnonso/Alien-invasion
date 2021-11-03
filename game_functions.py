import sys
import pygame
import controls as control
import  load_images
from pygame.locals import *
import random

def check_events(game_settings, player):
    """Respond to keypres and mouse events"""  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            control.check_keydown_events(event, game_settings, player)
        elif event.type == pygame.KEYUP:
            control.check_keyup_events(event, player)

           
def update_screen(game_settings, screen, player, lost, enemies):
    """Update images on the screen and flip to the new screen"""
    screen.blit(load_images.BG_1,(0,0))
    #screen.fill(game_settings.bg_color)
    
    #draw text
    lives_label = game_settings.main_font.render(f"Lives: {game_settings.startLives}", 1, (255,255,255))
    level_label = game_settings.main_font.render(f"Level: {game_settings.startLevel}", 1, (255,255,255))
    scoreBoard = game_settings.scoreboard_font.render(f"Score Board: {game_settings.scoreboard}", 1, (255,0,0))
    level_height = level_label.get_width()
    screen.blit(lives_label, (10,10))
    screen.blit(level_label, (game_settings.screen_width - level_height - 10, 10))
    screen.blit(scoreBoard, (game_settings.screen_width/2 - scoreBoard.get_width() - 10,10))
    
    for enemy in enemies:
        enemy.draw(screen)
    
    if lost:
        lost_label = game_settings.lost_font.render("You Lost!",1,(255,255,255))
        screen.blit(lost_label, (game_settings.screen_width/2 - lost_label.get_width()/2, 350 ))
        
    player.draw(screen)
    
    #Make the most recently draw screen visible
    pygame.display.flip()

#fire enemy lasers
def shoot_alien_laser(enemies,game_settings, player):
    for enemy in enemies[:]:
            enemy.move(game_settings.enemy_vel)
            enemy.move_lasers(game_settings.laser_vel, player)
            
            #Allow the enempy to shoot at randow
            if random.randrange(0, 2 * 700) == 1:
                enemy.shoot()
            
            if enemy.y + enemy.get_height() > game_settings.screen_height:
              game_settings.startLives -= 1
              enemies.remove(enemy)
   
    