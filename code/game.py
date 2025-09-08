import pygame
from settings import WIDTH, HEIGHT, TITLE, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
    
    def run(self):

        runs = True

        while runs:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    runs = False

            self.window.fill((144, 255, 100))
            self.clock.tick(FPS)
            pygame.display.flip()

        pygame.quit()
