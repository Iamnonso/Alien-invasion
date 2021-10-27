class Settings():
    """A class to store all the game settings for alien invasion"""
    
    def __init__(self):
        """Initialize the game's settings"""
        #ship settings
        self.ship_speed_factor = 1.5
        #screen settings
        self.screen_width = 1200
        self.screen_height = 630
        self.bg_color = (230, 230, 230)
        
        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3