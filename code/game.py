import pygame
from settings import WIDTH, HEIGHT, TITLE, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            pygame.event.get()