# Simple Animation with PyGame, Anthony Furlow, 1/4/22, 2:34 pm, v0.0

import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.init()

# Setup the Window
WINDOWWITH = 400
WINDOWHEIGHT = 400
windowSurface = = pygame.display.set_mode((WINDOWWITH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')
