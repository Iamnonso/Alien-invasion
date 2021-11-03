import sys
import pygame
from settings import Settings
from ship import Player
from ship import alien_ships
import game_functions as games
import random
import load_images

game_settings = Settings() #All Game settings
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height)) #create screen

#define main block
def run_game():
    #Initialize game and create a screen object
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    
    #GAME SPEED
    FBS = game_settings.gameSpeed
    clock = pygame.time.Clock()
   
    enemies = []  
    lost = False
    screen_rect = screen.get_rect()
    run = True
    player = Player(screen_rect.centerx, 500)
    
    #Start the main loop for the game.
    while run:     
        clock.tick(FBS)
        games.update_screen(game_settings, screen, player, lost, enemies)
        
        if int(game_settings.startLives) <= 0 or player.health <= 0:
            lost = True
            game_settings.lost_count += 1
        
        if lost:
            if game_settings.lost_count > FBS * 3:
                game_settings.startLevel = 0
                game_settings.scoreboard = 0
                run = False
            else:
                continue
        
        #increase game speed with level
        if int(game_settings.startLevel)/2 > game_settings.startLevel:
            game_settings.gameSpeed = 3
            print(game_settings.gameSpeed)
                   
        if len(enemies) == 0:
            game_settings.startLevel += 1
            game_settings.wave_length += 5 # ADD Number of starting aliens on the screen
            for i in range(game_settings.wave_length):
                enemy = alien_ships(random.randrange(50, game_settings.screen_width - 100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy) 
               
        #listen to EVENTS function.
        games.check_events(game_settings, player)
        player.update(player)
        
        games.shoot_alien_laser(enemies, game_settings, player) 
               
        player.move_lasers(-game_settings.bullet_speed_factor, enemies, game_settings)
        
def main_menu():
    title_font = pygame.font.SysFont("comicsans", 40)
    run = True
    while run:
        screen.blit(load_images.BG_1, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        screen.blit(title_label, (game_settings.screen_width/2 - title_label.get_width()/2, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run_game()
    pygame.quit()
        
        
main_menu()