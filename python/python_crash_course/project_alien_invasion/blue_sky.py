"""  """

import sys
import pygame
from robot import Robot

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1366, 700))
    pygame.display.set_caption('Random Game')
    bg_color = (0, 0, 255)
    
    robot = Robot(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        robot.blitme()
        pygame.display.flip()

run_game()