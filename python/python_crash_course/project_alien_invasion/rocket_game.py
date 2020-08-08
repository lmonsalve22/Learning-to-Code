""" Make a game that begins with a rocket in the center of the screen. 
Allow the player to move the rocket up, down, left, or right using the
four arrow keys. Make sure the rocket never moves beyond any edge of the
screen. """

import sys
import pygame
from rocket import Rocket
from rocket_settings import Settings
import rocket_functions as rf

def run_game():
    pygame.init()
    config = Settings()
    screen = pygame.display.set_mode((config.screen_width,
    config.screen_height))
    pygame.display.set_caption('A Rocket Game')
    rocket = Rocket(config, screen)

    while True:
        rf.check_events(rocket)
        rocket.update()
        rf.update_screen(config, screen, rocket)

run_game()
