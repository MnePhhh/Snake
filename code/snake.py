import pygame
from settings import CELL, ROWS, COLS

class DrawSnake:
    def __init__(self):
        self.head = (COLS // 2, ROWS // 2)
        self.dir = (1, 0)

    def draw_snake(self, surface):
        cx, cy = self.head
        x = cx * CELL
        y = cy * CELL
        width = CELL
        height = CELL

        pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height))

    def change_dir(self, key):
        if (key == pygame.K_UP or key == pygame.K_w) and self.dir != (0, 1):
            self.dir = (0, -1)
        elif (key == pygame.K_DOWN or key == pygame.K_s) and self.dir != (0, -1):
            self.dir = (0, 1)
        elif (key == pygame.K_LEFT or key == pygame.K_a) and self.dir != (1, 0):
            self.dir = (-1, 0)
        elif (key == pygame.K_RIGHT or key == pygame.K_d) and self.dir != (-1, 0):
            self.dir = (1, 0)

    def step(self):
        cx, cy = self.head
        dx, dy = self.dir
        nx = (cx + dx) % COLS
        ny = (cy + dy) % ROWS
        self.head = (nx, ny)