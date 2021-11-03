import pygame
pygame.font.init()
class Settings():
    """A class to store all the game settings for alien invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        #ship settings
        self.ship_speed_factor = 1.5
        #screen settings
        self.screen_width = 1000
        self.screen_height = 630
        
        self.wave_length = 5
        self.enemy_vel = 0.2
        self.laser_vel = 0.4
        self.lost_count = 0
        self.player_vel = self.ship_speed_factor
        self.scoreboard = 0
        
        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 50
        self.bullet_height =100
        self.bullet_allowed = 3
        
       
        self.main_font = pygame.font.SysFont("comicsans", 30)
        self.lost_font = pygame.font.SysFont("comicsans", 70)
        self.scoreboard_font = pygame.font.SysFont("Arial", 25)
        self.startLevel = 0
        self.startLives = 10
        self.gameSpeed = 300
        