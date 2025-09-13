import pygame
from settings import CELL, ROWS, COLS

class DrawSnake:
    def __init__(self, start_pos=None):
        if start_pos is None:
            start_pos = (COLS // 2, ROWS // 2)
        self.dir = (1, 0)
        self.body = [(start_pos[0], start_pos[1])]
        self.grow_amount = 0
    
    def lose(self):
        for my_body in self.body[1:]:
            if self.head == my_body:
                pygame.quit()

    @property
    def head(self):
        return self.body[0]

    def draw_snake(self, surface):
        for segment in self.body:
            x, y = segment
            rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
            pygame.draw.rect(surface, (0, 100, 0), rect)
            pygame.draw.rect(surface, (0, 0, 0), rect, 1)

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
        new_head = (nx, ny)
        self.body.insert(0, new_head)
        if self.grow_amount > 0:
            self.grow_amount -= 1
        else:
            self.body.pop()

    def grow(self, amount=1):
        self.grow_amount += amount
