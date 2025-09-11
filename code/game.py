import pygame
from settings import WIDTH, HEIGHT, TITLE, FPS, MOVE_EVENT, MOVES_PER_SEC
from snake import DrawSnake
from food import Food, GoldApple, RandomFood

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.snake = DrawSnake()
        self.food = Food()
        self.gold_food = GoldApple()
        self.random_food = RandomFood()

        self.current_food = None
        self.is_gold = False
        self.spawn_food()

    def spawn_food(self):
        if self.random_food.random_food_number() == 1:
            self.current_food = Food()
            self.is_gold = False
        else:
            self.current_food = GoldApple()
            self.is_gold = True

    def run(self):

        runs = True
        
        pygame.time.set_timer(MOVE_EVENT, 1000 // MOVES_PER_SEC)

        while runs:

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    runs = False
                elif e.type == MOVE_EVENT:
                    self.snake.step()

                    if self.snake.head == self.current_food.position:
                        self.spawn_food()
                        
                elif e.type == pygame.KEYDOWN:
                    self.snake.change_dir(e.key)
                    
            self.window.fill((144, 255, 100))
            self.clock.tick(FPS)
            self.snake.draw_snake(self.window)

            if self.is_gold:
                self.current_food.draw(self.window)
            else:
                self.current_food.draw(self.window)

            pygame.display.flip()

        pygame.quit()

