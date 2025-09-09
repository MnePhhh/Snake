import pygame
from settings import WIDTH, HEIGHT, TITLE, FPS, MOVE_EVENT, MOVES_PER_SEC
from snake import DrawSnake

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.snake = DrawSnake()
    
    def run(self):

        runs = True
        
        pygame.time.set_timer(MOVE_EVENT, 1000 // MOVES_PER_SEC)

        while runs:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    runs = False
                elif e.type == MOVE_EVENT:
                    self.snake.step()
                elif e.type == pygame.KEYDOWN:
                    self.snake.change_dir(e.key)

            self.window.fill((144, 255, 100))
            self.clock.tick(FPS)
            self.snake.draw_snake(self.window)

            pygame.display.flip()

        pygame.quit()

