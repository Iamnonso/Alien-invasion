import pygame
import os
from settings import Settings

game_settings = Settings()

#enemy ship
RED_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_red_small.bmp"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_green_small.bmp"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("images", "pixel_ship_blue_small.bmp"))

#lasers
RED_LASER = pygame.image.load(os.path.join("images", "pixel_laser_red.bmp"))
GREEN_LASER = pygame.image.load(os.path.join("images", "pixel_laser_green.bmp"))
BLUE_LASER = pygame.image.load(os.path.join("images", "pixel_laser_blue.bmp"))
YELLOW_LASER = pygame.image.load(os.path.join("images", "pixel_laser_yellow.bmp"))

#background Image
BG_1 =  pygame.transform.scale(pygame.image.load(os.path.join("images", "invader_space_bg1.bmp")), (game_settings.screen_width,game_settings.screen_height))

#My ships
WAR_SHIP2 = pygame.image.load(os.path.join("images","ship1.bmp"))