import sys
import pygame
from settings import Settings

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion - OS_01 Assignments")
    
    #Start the main loop for the game.
    while True:
        #watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        #fill the screen with color
        screen.fill(game_settings.bg_color)      
        #Make the most recently draw screen visible
        pygame.display.flip()
        
run_game()