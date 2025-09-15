import pygame
import random
from settings import ROWS, COLS, CELL

class RandomFood:
    def __init__(self):
        self.random_position()
        # apple_img = pygame.image.load("apple_red.png").convert_alpha()
        # apple_gold_img = pygame.image.load("apple_gold.png").convert_alpha()

        # apple_img = pygame.transform.scale(apple_img, (CELL, CELL))
        # apple_gold_img = pygame.transform.scale(apple_gold_img, (CELL, CELL))

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
    def __init__(self, img):
        super().__init__()
        self.img = img

    def draw(self, surface):
        col, row = self.position
        x = col * CELL
        y = row * CELL
        surface.blit(self.img, (x, y))

class GoldApple(RandomFood):
    def __init__(self, img):
        super().__init__()
        self.img = img

    def draw(self, surface):
        col, row = self.position
        x = col * CELL
        y = row * CELL
        surface.blit(self.img, (x, y))