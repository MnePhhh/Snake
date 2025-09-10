import pygame
import random
from settings import ROWS, COLS, CELL

class Food:
    def __init__(self):
        self.random_position()

    def random_position(self): #forbidden=None):

        #if forbidden is None:
        #    forbidden = set()

        #while True:
        col = random.randint(0, COLS - 1)
        row = random.randint(0, ROWS - 1)
        self.position = (col, row)

            # if (col, row) not in forbidden:
            #     self.position = (col, row)
            #     break

    def draw(self, surface):
        col, row = self.position
        x = col * CELL
        y = row * CELL
        pygame.draw.rect(surface, (255, 0, 0), (x, y, CELL, CELL))
