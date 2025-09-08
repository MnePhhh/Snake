import pygame
from settings import CELL, ROWS, COLS

class DrawSnake:
    def __init__(self):
        self.head = (COLS // 2, ROWS // 2)

    def draw_snake(self, surface):
        cx, cy = self.head
        x = cx * CELL
        y = cy * CELL
        width = CELL
        height = CELL

        pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height))