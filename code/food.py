import pygame
import random
from settings import ROWS, COLS, CELL

class RandomFood:
    def __init__(self):
        self.random_position()

    def random_position(self):

        col = random.randint(0, COLS - 1)
        row = random.randint(0, ROWS - 1)
        self.position = (col, row)

    def random_food_number(self):
        random_apple = random.randint(1, 11)

        if random_apple != 1:
            return 1
        
        else : return 0

class Food(RandomFood):
    def __init__(self):
        super().__init__()

    def draw(self, surface):
        col, row = self.position
        x = col * CELL
        y = row * CELL
        pygame.draw.rect(surface, (255, 0, 0), (x, y, CELL, CELL)) 

class GoldApple(RandomFood):
    def __init__(self):
        super().__init__()

    def draw(self, surface):
        col, row = self.position
        x = col * CELL
        y = row * CELL
        pygame.draw.rect(surface, (255, 255, 0), (x, y, CELL, CELL))