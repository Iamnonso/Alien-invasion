import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion - OS_01 Assignments")
    
    #Make a ship
    ship = Ship(game_settings,screen)
    #make a group to store bullets in.
    bullets = Group()
    
    #Start the main loop for the game.
    while True:
        #listen to Game Quit.
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        #get rid of bullets that have disappeared
        gf.update_bullets(bullets)
        #Redraw screen
        gf.update_screen(game_settings, screen, ship, bullets)
        
run_game()