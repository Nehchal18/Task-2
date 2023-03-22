import pygame
import sys
import random
from words import *

pygame.init()

# Constants

WIDTH, HEIGHT = 633, 880
# /Users/nehchal./Desktop/coding/python.py/wordle/assets_wordle/StartingTiles.png
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("/Users/nehchal./Desktop/coding/python.py/wordle/assets_wordle/StartingTiles.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300))
ICON = pygame.image.load("/Users/nehchal./Desktop/coding/python.py/wordle/assets_wordle/Icon.png")
easy_img = pygame.image.load("/Users/nehchal./Downloads/easy.gif").convert_alpha()
medium_img = pygame.image.load("/Users/nehchal./Downloads/medium.gif").convert_alpha()
hard_img = pygame.image.load("/Users/nehchal./Downloads/hard.gif").convert_alpha()

