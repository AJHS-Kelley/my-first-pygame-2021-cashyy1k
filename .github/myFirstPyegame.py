# My First PyGame, Anthony Furlow, 11/30/21, 2:35 pm, v0.1

import pygame, sys
from pygame.locals import *

# Start Pygame
pygame.init()

#Setup the game window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Step color vaules.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
JAVO = (0, 255, 255)

