import pygame
from pygame.locals import *
import load_images
from pygame.sprite import Sprite
from settings import Settings

game_settings = Settings()

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Ships:
    COOLDOWN = game_settings.bullet_allowed #Number of bullet allow

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj, obj2):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(game_settings.screen_height):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 3 #if enempy bullet collede with player ship remove 5 from life.
                self.lasers.remove(laser)
            elif laser.collision(obj2):
                obj2.health -= 3
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

#define Player ship and inherent the Ships class
class Player(Ships):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = pygame.transform.scale(load_images.WAR_SHIP2, (70,70))
        self.laser_img = load_images.YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self, ship):
        """update player ship position base on movement flag"""
        if self.moving_right and ship.x + game_settings.player_vel + ship.get_width() < game_settings.screen_width:
            ship.x += game_settings.player_vel
        if self.moving_left  and ship.x - game_settings.player_vel > 0:
            ship.x -= game_settings.player_vel
        if self.moving_up and ship.y - game_settings.player_vel > 0:
            ship.y -= game_settings.player_vel
        if self.moving_down and ship.y + game_settings.player_vel + ship.get_height() + 15 < game_settings.screen_height:
            ship.y += game_settings.player_vel

    def move_lasers(self, vel, objs, settings):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(game_settings.screen_height):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        settings.scoreboard += 1
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                            

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


class Player2(Ships):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = pygame.transform.scale(load_images.WAR_SHIP, (70,70))
        self.laser_img = load_images.YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self, ship):
        """update player ship position base on movement flag"""
        if self.moving_right and ship.x + game_settings.player_vel + ship.get_width() < game_settings.screen_width:
            ship.x += game_settings.player_vel
        if self.moving_left  and ship.x - game_settings.player_vel > 0:
            ship.x -= game_settings.player_vel
        if self.moving_up and ship.y - game_settings.player_vel > 0:
            ship.y -= game_settings.player_vel
        if self.moving_down and ship.y + game_settings.player_vel + ship.get_height() + 15 < game_settings.screen_height:
            ship.y += game_settings.player_vel

    def move_lasers(self, vel, objs, settings):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(game_settings.screen_height):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        settings.scoreboard += 1
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                            

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


 
#define alien class and inherent the Ships class 
class alien_ships(Ships):    
    #get enempy ship color
    COLOR_MAP = {
        "red": (load_images.RED_SPACE_SHIP, load_images.RED_LASER),
        "green": (load_images.GREEN_SPACE_SHIP, load_images.GREEN_LASER),
        "blue": (load_images.BLUE_SPACE_SHIP, load_images.BLUE_LASER)
        
    }
    """alien  ship will inherent alien ship class"""
    def __init__(self, x, y,color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, vel):
        self.y += vel
        
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
           
    
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj2.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
        