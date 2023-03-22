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


pygame.display.set_caption("Wordle!")
pygame.display.set_icon(ICON)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

# CORRECT_WORD = "coder" #random.choice(WORDS)

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pygame.font.Font("/Users/nehchal./Desktop/coding/python.py/wordle/assets_wordle/FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("/Users/nehchal./Desktop/coding/python.py/wordle/assets_wordle/FreeSansBold.otf", 25)

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75

# Global variables

guesses_count = 0

# guesses is a 2D list that will store guesses. A guess will be a list of letters.
# The list will be iterated through and each letter in each guess will be drawn on the screen.
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

# Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
indicators = []

game_result = ""
